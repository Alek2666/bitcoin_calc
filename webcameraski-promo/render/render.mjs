// Render animacji klatka po klatce -> MP4 (H.264 High, 886×1920, 30 fps, AAC 256 kb/s)
// zgodny ze specyfikacją App Preview dla iPhone 6.5"/6.7"/6.9".
//
//   npm run render                       -> out/webcameraski-app-preview.mp4
//   npm run render -- --audio muzyka.mp3 -> z Twoją ścieżką audio (inaczej: assets/audio.* lub cisza)
//   npm run render -- --draft            -> szybki podgląd (15 fps)
//   npm run render -- --stills 1,5.2,9   -> tylko wybrane klatki PNG do out/
//   npm run render -- --browser chromium -> przeglądarka Playwright zamiast Chrome/Edge
import { spawn } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import { once } from 'node:events';
import { fileURLToPath, pathToFileURL } from 'node:url';
import ffmpegPath from 'ffmpeg-static';
import { chromium } from 'playwright';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const argv = process.argv.slice(2);
const opt = (name, def) => {
  const i = argv.indexOf('--' + name);
  if (i < 0) return def;
  const v = argv[i + 1];
  return v === undefined || v.startsWith('--') ? true : v;
};
const outDir = path.join(root, 'out');
fs.mkdirSync(outDir, { recursive: true });

async function launch() {
  const pref = opt('browser', null);
  const tries = pref ? [pref] : ['chrome', 'msedge', 'chromium'];
  for (const b of tries) {
    try {
      const o = { args: ['--autoplay-policy=no-user-gesture-required', '--allow-file-access-from-files', '--hide-scrollbars'] };
      if (b !== 'chromium') o.channel = b;
      const browser = await chromium.launch(o);
      console.log(`Przeglądarka: ${b}`);
      return browser;
    } catch (e) {
      if (pref) throw e;
    }
  }
  throw new Error('Nie znaleziono Chrome/Edge. Zainstaluj Chrome albo uruchom: npx playwright install chromium');
}

const browser = await launch();
const page = await browser.newPage({ viewport: { width: 886, height: 1920 }, deviceScaleFactor: 1 });
page.on('console', (m) => { if (m.type() === 'error') console.log('  [strona]', m.text()); });
page.on('pageerror', (e) => console.log('  [strona]', e.message));
await page.goto(pathToFileURL(path.join(root, 'index.html')).href + '?render=1');
const info = await page.evaluate(() => window.__ready);
if (info.missing.length && !opt('allow-missing', false)) {
  console.error('\n✗ Brakuje plików: ' + info.missing.join(', ') + '\n  Uruchom najpierw: npm run assets  (albo dodaj --allow-missing)');
  await browser.close();
  process.exit(1);
}

const frame = async (t) => {
  await page.evaluate((tt) => window.__seek(tt), t);
  return page.screenshot({ type: 'png', animations: 'allow', caret: 'initial' });
};

// --- pojedyncze klatki
const stills = opt('stills', null);
if (stills) {
  for (const s of String(stills).split(',').map(Number)) {
    const f = path.join(outDir, `still-${s.toFixed(2).padStart(5, '0')}s.png`);
    fs.writeFileSync(f, await frame(s));
    console.log('  ✓', path.relative(root, f));
  }
  await browser.close();
  process.exit(0);
}

// --- pełny film
const fps = opt('draft', false) ? 15 : info.fps;
const dur = info.duration;
const total = Math.round(dur * fps);
const out = path.resolve(opt('out', path.join(outDir, opt('draft', false) ? 'webcameraski-draft.mp4' : 'webcameraski-app-preview.mp4')));

let audio = opt('audio', null);
if (!audio) {
  const found = fs.readdirSync(path.join(root, 'assets')).find((f) => /^audio\.(mp3|wav|m4a|aac|flac|ogg)$/i.test(f));
  if (found) audio = path.join(root, 'assets', found);
}
if (audio === true) audio = null;
const aIn = audio ? ['-i', path.resolve(audio)] : ['-f', 'lavfi', '-t', String(dur), '-i', 'anullsrc=r=48000:cl=stereo'];
const aFx = audio ? ['-af', `atrim=0:${dur},afade=t=in:st=0:d=0.2,afade=t=out:st=${(dur - 1.2).toFixed(2)}:d=1.2,aresample=48000`] : [];

const args = [
  '-hide_banner', '-loglevel', 'error', '-y',
  '-f', 'image2pipe', '-framerate', String(fps), '-c:v', 'png', '-i', '-',
  ...aIn,
  '-map', '0:v', '-map', '1:a',
  '-c:v', 'libx264', '-profile:v', 'high', '-level', '4.0', '-pix_fmt', 'yuv420p',
  '-preset', 'slow', '-crf', '16', '-maxrate', '12M', '-bufsize', '24M', '-r', String(fps),
  '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709',
  ...aFx, '-c:a', 'aac', '-b:a', '256k', '-ar', '48000', '-ac', '2',
  '-t', String(dur), '-movflags', '+faststart', out,
];
const ff = spawn(ffmpegPath, args, { stdio: ['pipe', 'inherit', 'inherit'] });
const ffDone = once(ff, 'close');

console.log(`Render ${total} klatek (${fps} fps) -> ${path.relative(process.cwd(), out)}${audio ? '  + audio: ' + audio : '  (cicha ścieżka audio)'}`);
const t0 = Date.now();
for (let i = 0; i < total; i++) {
  const buf = await frame(i / fps);
  if (!ff.stdin.write(buf)) await once(ff.stdin, 'drain');
  if (i % 10 === 0 || i === total - 1) {
    const el = (Date.now() - t0) / 1000;
    const eta = (el / (i + 1)) * (total - i - 1);
    process.stdout.write(`\r  klatka ${i + 1}/${total}  (${el.toFixed(0)} s, zostało ~${eta.toFixed(0)} s)   `);
  }
}
ff.stdin.end();
const [code] = await ffDone;
await browser.close();
process.stdout.write('\n');
if (code !== 0) { console.error('✗ ffmpeg zakończył się błędem'); process.exit(1); }
console.log(`✓ Gotowe: ${out}`);
