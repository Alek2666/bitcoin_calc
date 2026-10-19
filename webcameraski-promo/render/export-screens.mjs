// Eksport ekranów aplikacji (płasko, 1179×2556 jak iPhone 15 Pro, przezroczyste rogi) z animacji.
// Każdy kadr to konkretna chwila filmu, więc ekrany mają te same dane i nagrania co reklama.
//   node render/export-screens.mjs [katalog-docelowy]
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { chromium } from 'playwright';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const outDir = path.resolve(process.argv[2] || path.join(root, 'out', 'screens'));
fs.mkdirSync(outDir, { recursive: true });

// [plik, strona, czas w filmie, poziomo?]
const SHOTS = [
  ['home', 'index.html', 0.9],
  ['search', 'index.html', 2.7],
  ['resort', 'index.html', 4.6],
  ['cameras', 'index.html', 6.47],
  ['live', 'index.html', 8.3, true],
  ['weather', 'index-16x9.html', 13.5],
  ['feed', 'index.html', 16.95],
  ['resort-master', 'index-16x9.html', 4.6],
  ['live-kasprowy', 'index-16x9.html', 9.9, true],
];

const launch = async () => {
  for (const channel of ['chrome', 'msedge', undefined]) {
    try { return await chromium.launch(channel ? { channel } : {}); } catch { /* następna */ }
  }
  throw new Error('Brak przeglądarki (Chrome/Edge) — npx playwright install chromium');
};
const browser = await launch();
const pages = {};
for (const [name, file, t, landscape] of SHOTS) {
  if (!pages[file]) {
    const p = await browser.newPage({ viewport: { width: 1400, height: 2800 }, deviceScaleFactor: 1 });
    await p.goto(pathToFileURL(path.join(root, file)).href + '?render=1');
    await p.evaluate(() => window.__ready);
    pages[file] = p;
  }
  const page = pages[file];
  await page.evaluate((tt) => window.__seek(tt), t);
  const box = await page.evaluate((land) => {
    // statyczny kadr: liczniki z pełnymi wartościami (w filmie są animowane)
    document.querySelectorAll('[data-count]').forEach((e) => { e.textContent = e.dataset.count; });
    const hide = ['#captions', '#marquee', '#outro', '#snow', '#snow-front', '#bg-glow', '#fade', '#touch'];
    hide.forEach((s) => { const e = document.querySelector(s); if (e) e.style.display = 'none'; });
    document.documentElement.style.background = document.body.style.background = 'transparent';
    const stage = document.querySelector('#stage');
    Object.assign(stage.style, { width: '1400px', height: '2800px', background: 'transparent', overflow: 'visible' });
    const phone = document.querySelector('#phone');
    phone.style.opacity = 1;
    phone.style.transformOrigin = '0 0';
    // telefon renderowany w 2× (zoom), skala 1.5 => ekran 393 pt = 1179 px
    phone.style.transform = land ? 'translate(20px, 1283px) rotate(-90deg) scale(1.5)' : 'translate(20px, 20px) scale(1.5)';
    const r = document.querySelector('#screen').getBoundingClientRect();
    return { x: Math.round(r.left), y: Math.round(r.top), width: Math.round(r.width), height: Math.round(r.height) };
  }, !!landscape);
  await page.evaluate(() => new Promise((r) => requestAnimationFrame(() => requestAnimationFrame(r))));
  const f = path.join(outDir, `${name}.png`);
  await page.screenshot({ path: f, clip: box, omitBackground: true });
  console.log(`  ✓ ${path.relative(process.cwd(), f)}  ${box.width}×${box.height}`);
}
await browser.close();
