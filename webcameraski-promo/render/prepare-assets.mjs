// Przygotowuje nagrania i logo dla animacji:
//  - wideo (także H.265/HEVC) -> assets/<klucz>.webm (VP9, max 1920 px, 30 fps, bez dźwięku)
//  - logo -> assets/<klucz>-logo.png
// Użycie: npm run assets            (czyta promo.config.json)
//         node render/prepare-assets.mjs inny.config.json
import { spawn } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import ffmpegPath from 'ffmpeg-static';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const cfgPath = path.resolve(process.argv[2] || path.join(root, 'promo.config.json'));
const cfg = JSON.parse(fs.readFileSync(cfgPath, 'utf8'));
const assets = path.join(root, 'assets');
fs.mkdirSync(assets, { recursive: true });

function ffmpeg(args, label) {
  return new Promise((resolve, reject) => {
    const p = spawn(ffmpegPath, ['-hide_banner', '-loglevel', 'error', '-stats', ...args], { stdio: ['ignore', 'inherit', 'pipe'] });
    let err = '';
    p.stderr.on('data', (d) => {
      const s = d.toString();
      err += s;
      const m = s.match(/time=(\S+)/);
      if (m) process.stdout.write(`\r  ${label}: ${m[1]}   `);
    });
    p.on('close', (code) => {
      process.stdout.write('\n');
      code === 0 ? resolve() : reject(new Error(`${label}: ffmpeg zakończył się kodem ${code}\n${err.slice(-2000)}`));
    });
  });
}

const resolveSrc = (src) => path.resolve(path.dirname(cfgPath), src);

for (const [key, v] of Object.entries(cfg.videos || {})) {
  const src = resolveSrc(v.src);
  if (!fs.existsSync(src)) { console.error(`✗ Nie znaleziono nagrania "${key}": ${src}`); process.exitCode = 1; continue; }
  const out = path.join(assets, `${key}.webm`);
  console.log(`→ ${key}: ${src}`);
  const args = [];
  if (v.start) args.push('-ss', String(v.start));
  args.push('-i', src, '-t', String(v.duration ?? 20), '-an',
    '-vf', "scale='min(1920,iw)':-2:flags=lanczos,fps=30,format=yuv420p",
    '-c:v', 'libvpx-vp9', '-crf', '22', '-b:v', '0', '-row-mt', '1', '-deadline', 'good', '-cpu-used', '3',
    '-g', '15', '-keyint_min', '15', '-y', out);
  await ffmpeg(args, key);
  console.log(`  ✓ ${path.relative(root, out)}`);
}

for (const [key, src0] of Object.entries(cfg.logos || {})) {
  const src = resolveSrc(src0);
  if (!fs.existsSync(src)) { console.error(`✗ Nie znaleziono logo "${key}": ${src}`); process.exitCode = 1; continue; }
  const out = path.join(assets, `${key}-logo.png`);
  if (src.toLowerCase().endsWith('.png')) fs.copyFileSync(src, out);
  else await ffmpeg(['-i', src, '-y', out], `${key}-logo`);
  console.log(`  ✓ ${path.relative(root, out)}`);
}

if (!process.exitCode) console.log('\nGotowe. Otwórz index.html w przeglądarce albo uruchom: npm run render');
