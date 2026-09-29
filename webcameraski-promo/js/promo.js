/*
 * WebCameraSki — App Preview (9:16 886×1920 lub 16:9 1920×1080, 30 fps, 20 s)
 * Cała animacja jest funkcją czasu: render(t). Dzięki temu podgląd w przeglądarce
 * i render klatka-po-klatce (render/render.mjs) dają identyczny obraz.
 */
(() => {
  const P = window.PROMO;
  const S = window.Screens;
  const params = new URLSearchParams(location.search);
  const RENDER = params.has('render');
  const FPS = P.fps, DUR = P.duration;

  // ---------------------------------------------------------------- easing
  function bezier(x1, y1, x2, y2) {
    const cx = 3 * x1, bx = 3 * (x2 - x1) - cx, ax = 1 - cx - bx;
    const cy = 3 * y1, by = 3 * (y2 - y1) - cy, ay = 1 - cy - by;
    const sx = (t) => ((ax * t + bx) * t + cx) * t;
    const sy = (t) => ((ay * t + by) * t + cy) * t;
    const dx = (t) => (3 * ax * t + 2 * bx) * t + cx;
    return (x) => {
      if (x <= 0) return 0;
      if (x >= 1) return 1;
      let t = x;
      for (let i = 0; i < 8; i++) {
        const e = sx(t) - x;
        if (Math.abs(e) < 1e-6) return sy(t);
        const d = dx(t);
        if (Math.abs(d) < 1e-6) break;
        t -= e / d;
      }
      let lo = 0, hi = 1;
      t = x;
      while (hi - lo > 1e-6) { if (sx(t) < x) lo = t; else hi = t; t = (lo + hi) / 2; }
      return sy(t);
    };
  }
  const ease = {
    easy: bezier(0.33, 0, 0.67, 1),     // After Effects "Easy Ease"
    smooth: bezier(0.45, 0, 0.15, 1),   // Easy Ease z mocniejszym wyhamowaniem (ruchy kamery)
    out: bezier(0.22, 1, 0.36, 1),      // wejścia elementów
    in: bezier(0.55, 0, 0.85, 0.35),
    linear: (x) => x,
  };
  const clamp01 = (v) => (v < 0 ? 0 : v > 1 ? 1 : v);
  const lerp = (a, b, k) => a + (b - a) * k;
  const prog = (t, a, b, e = ease.easy) => e(clamp01((t - a) / (b - a)));
  const range = (t, [a, b], e) => prog(t, a, b, e);

  // ---------------------------------------------------------------- oś czasu (s)
  const T = {
    fadeIn: [0, 0.6],
    capSearch: [0.35, 3.05],
    tapSearch: 1.15,
    pushList: [1.3, 1.8],
    typeStart: 1.95, typeDt: 0.11,
    filterAt: 2.3,
    tapResult: 2.85,
    pushDetail: [3.0, 3.5],
    capConditions: [3.45, 6.45],
    countR1: [3.65, 4.55],
    scroll1: [4.65, 5.35],
    countOpenR1: [4.95, 5.65],
    tapCams: 5.72,
    tabSlide: [5.78, 6.12],
    scroll2: [5.98, 6.46],
    tapPlay: 6.64,
    expand: [6.78, 7.65],
    capLive: [7.05, 10.1],
    marquee: [7.25, 10.25],
    swipe: [8.85, 9.4],
    collapse: [10.3, 11.15],
    capWeather: [10.8, 14.0],
    countR2: [10.95, 11.85],
    scroll3: [12.1, 12.85],
    tapStart: 14.28,
    pop: [14.38, 14.93],
    capFeed: [14.6, 17.2],
    feedScroll: [15.05, 15.85],
    countFeed: [15.35, 16.45],
    newsSwipe: [16.0, 16.7],
    phoneOut: [17.25, 18.25],
    logoIn: [17.75, 18.6],
    logoBar: [18.3, 18.9],
    outroType: 18.45,
    outroSub: [18.95, 19.45],
    fadeOut: [19.45, 20.0],
  };

  // ---------------------------------------------------------------- układ kadru
  // Kamera (telefon): x/y przesunięcie od pozycji bazowej, s skala, rx/ry obrót 3D (stopnie)
  const LAYOUTS = {
    '9x16': {
      W: 886, H: 1920,
      phone: { s0: 1.55, cx: 443, cy: 1150 }, persp: [443, 1100],
      cam: [
        [0.0,   { x: 0, y: 560, s: 0.9,   rx: 34, ry: -26 }],
        [1.55,  { x: 0, y: 0,   s: 1.0,   rx: 9,  ry: -13 }, ease.out],
        [3.3,   { x: 0, y: 0,   s: 1.0,   rx: 6,  ry: -7 }],
        [4.6,   { x: 0, y: 30,  s: 1.05,  rx: 4,  ry: 7 }],
        [5.6,   { x: 0, y: 30,  s: 1.05,  rx: 3,  ry: 5 }],
        [6.62,  { x: 0, y: 10,  s: 1.02,  rx: 4,  ry: -3 }],
        [7.65,  { x: 0, y: -150, s: 0.745, rx: 0, ry: 0 }],
        [10.3,  { x: 0, y: -150, s: 0.79, rx: 2,  ry: -3 }, ease.easy],
        [11.15, { x: 0, y: 20,  s: 1.0,   rx: 8,  ry: 11 }],
        [12.85, { x: 0, y: 40,  s: 1.06,  rx: 4,  ry: 6 }],
        [14.28, { x: 0, y: 40,  s: 1.07,  rx: 3,  ry: 3 }],
        [14.95, { x: 0, y: 0,   s: 1.0,   rx: 7,  ry: -8 }],
        [17.25, { x: 0, y: 10,  s: 1.03,  rx: 4,  ry: -2 }],
        [18.3,  { x: 0, y: 860, s: 0.86,  rx: 30, ry: 6 }, ease.in],
      ],
      caps: { search: { top: 150 }, conditions: { top: 150 }, live: { top: 420 }, weather: { top: 150 }, feed: { top: 150 } },
      capMax: 820,
      marquee: { top: 1318, rowGap: 86, merge: false },
      outro: { logoBottom: 945, svgTop: 790, titleTop: 985, subTop: 1140, subMax: 840 },
    },
    '16x9': {
      W: 1920, H: 1080,
      phone: { s0: 1.04, cx: 1370, cy: 540 }, persp: [960, 540],
      cam: [
        [0.0,   { x: 260, y: 300, s: 0.9,  rx: 22, ry: -34 }],
        [1.55,  { x: 0,   y: 0,   s: 1.0,  rx: 6,  ry: -18 }, ease.out],
        [3.3,   { x: 0,   y: 0,   s: 1.0,  rx: 4,  ry: -12 }],
        [4.6,   { x: -10, y: 0,   s: 1.035, rx: 3, ry: -5 }],
        [5.6,   { x: -10, y: 0,   s: 1.035, rx: 3, ry: -7 }],
        [6.62,  { x: 0,   y: 0,   s: 1.02, rx: 3,  ry: -10 }],
        [7.65,  { x: -410, y: 60, s: 1.455, rx: 0, ry: 0 }],
        [10.3,  { x: -410, y: 60, s: 1.498, rx: 1.5, ry: -2 }, ease.easy],
        [11.15, { x: 0,   y: 0,   s: 1.0,  rx: 5,  ry: -20 }],
        [12.85, { x: 0,   y: 0,   s: 1.035, rx: 3, ry: -13 }],
        [14.28, { x: 0,   y: 0,   s: 1.04, rx: 3,  ry: -11 }],
        [14.95, { x: 0,   y: 0,   s: 1.0,  rx: 5,  ry: -17 }],
        [17.25, { x: 0,   y: 0,   s: 1.02, rx: 3,  ry: -11 }],
        [18.3,  { x: 120, y: 780, s: 0.86, rx: 24, ry: -8 }, ease.in],
      ],
      // hasła w lewej kolumnie obok telefonu; "Kamery na żywo" wyśrodkowane nad telefonem w poziomie
      caps: {
        search: { top: 432, left: 250 }, conditions: { top: 432, left: 250 }, live: { top: 44 },
        weather: { top: 432, left: 250 }, feed: { top: 432, left: 250 },
      },
      capMax: 840,
      marquee: { top: 962, rowGap: 0, merge: true },
      outro: { logoBottom: 500, svgTop: 360, titleTop: 540, subTop: 690, subMax: 1200 },
    },
  };
  const LAY = LAYOUTS[P.format] || LAYOUTS['9x16'];
  const { W, H } = LAY;
  const PHONE_S0 = LAY.phone.s0, PHONE_CX = LAY.phone.cx, PHONE_CY = LAY.phone.cy;
  const CAM = LAY.cam;
  const camAt = (() => {
    const props = ['x', 'y', 's', 'rx', 'ry'];
    const keys = [];
    let prev = {};
    for (const [t, v, e] of CAM) { prev = { ...prev, ...v }; keys.push([t, prev, e || ease.smooth]); }
    return (t) => {
      if (t <= keys[0][0]) return keys[0][1];
      for (let i = 1; i < keys.length; i++) {
        const [t1, v1, e] = keys[i];
        if (t <= t1) {
          const [t0, v0] = keys[i - 1];
          const k = e((t - t0) / (t1 - t0));
          const o = {};
          for (const p of props) o[p] = lerp(v0[p], v1[p], k);
          return o;
        }
      }
      return keys[keys.length - 1][1];
    };
  })();

  // ---------------------------------------------------------------- DOM
  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];
  const stage = $('#stage');
  document.body.classList.add('fmt-' + (LAYOUTS[P.format] ? P.format : '9x16'));
  stage.style.width = W + 'px';
  stage.style.height = H + 'px';
  $('#camera').style.perspectiveOrigin = `${LAY.persp[0]}px ${LAY.persp[1]}px`;
  $('#camera').innerHTML = S.phone();
  const phone = $('#phone');
  const screen = $('#screen');
  const scr = {
    home: $('#s-home'), list: $('#s-list'), r1: $('#s-r1'), r2: $('#s-r2'), feed: $('#s-feed'),
  };
  const statusbar = $('.statusbar', screen);
  const touch = $('#touch');
  const live = $('#live');
  const liveTrack = $('.live-track', live);
  const livePanes = $$('.live-pane', live);
  const liveBackdrop = $('.live-backdrop', screen);
  const R1 = P.resorts.r1, R2 = P.resorts.r2;
  // kadr zdjęcia 2. ośrodka = dokładnie ta klatka, na której kończy się "zwijanie" wideo na żywo
  $('#s-r2 canvas.hero').dataset.at = (R2.stillAt + (T.collapse[1] - T.swipe[0])).toFixed(3);

  // live — przycisk play (znika po dotknięciu)
  livePanes.forEach((pane) => {
    const pc = document.createElement('div');
    pc.className = 'play-circ';
    pc.innerHTML = S.ic('play', 24, '#1c2a3f');
    pane.appendChild(pc);
  });

  // ---------------------------------------------------------------- hasła
  const capRoot = $('#captions');
  function buildCaption(c, pos) {
    const el = document.createElement('div');
    el.className = 'cap';
    el.style.top = pos.top + 'px';
    if (pos.left != null) { el.classList.add('cap-left'); el.style.left = pos.left + 'px'; }
    const chars = Array.from(c.title).map((ch) => `<span class="ch">${S.esc(ch)}</span>`).join('');
    const words = c.sub ? c.sub.split(' ').map((w, i, a) => `<span class="w">${S.esc(w)}${i < a.length - 1 ? ' ' : ''}</span>`).join('') : '';
    el.innerHTML = `<div class="cap-bar"></div><div class="cap-title">${chars}<i class="cap-caret"></i></div>${words ? `<div class="cap-sub">${words}</div>` : ''}`;
    capRoot.appendChild(el);
    return el;
  }
  const CAPS = [
    { key: 'search', at: T.capSearch },
    { key: 'conditions', at: T.capConditions },
    { key: 'live', at: T.capLive },
    { key: 'weather', at: T.capWeather },
    { key: 'feed', at: T.capFeed },
  ].map((c) => ({ ...c, el: buildCaption(P.captions[c.key], LAY.caps[c.key]) }));

  // outro
  const outro = $('#outro');
  outro.innerHTML = `<div class="o-logo">${window.LOGO_SVG}</div><div class="o-sub">${S.esc(P.captions.outro.sub)}</div>`;
  const outroLogo = $('.o-logo', outro);
  outroLogo.style.top = LAY.outro.svgTop + 'px';
  let outroBar = $('.logo-bar', outro);
  outroBar.style.transformBox = 'fill-box';
  outroBar.style.transformOrigin = '0% 50%';
  // Logo na koniec z pliku (assets/logo-outro.png, białe z przezroczystością) — jeśli jest, zastępuje wektor.
  const outroImg = new Image();
  const outroImgReady = new Promise((resolve) => {
    outroImg.onload = () => {
      const a = outroImg.naturalWidth / outroImg.naturalHeight;
      const w = Math.min(P.outroLogo?.maxWidth ?? 640, (P.outroLogo?.maxHeight ?? 300) * a);
      const h = w / a;
      outroLogo.classList.add('o-logo-img');
      outroLogo.style.width = w + 'px';
      outroLogo.style.height = h + 'px';
      outroLogo.style.marginLeft = -w / 2 + 'px';
      outroLogo.style.top = LAY.outro.logoBottom - h + 'px'; // dół logo zawsze nad hasłem
      outroLogo.replaceChildren(outroImg);
      outroBar = null;
      resolve();
    };
    outroImg.onerror = () => resolve(); // brak pliku -> zostaje logo wektorowe
  });
  outroImg.alt = '';
  outroImg.src = P.outroLogo?.src ?? 'assets/logo-outro.png';
  const outroSub = $('.o-sub', outro);
  outroSub.style.top = LAY.outro.subTop + 'px';
  const outroCap = { key: 'outro', at: [T.outroType - 0.15, 99] };
  {
    const el = buildCaption({ title: P.captions.outro.title, sub: '' }, { top: LAY.outro.titleTop });
    el.classList.add('cap-outro');
    $('.cap-bar', el).style.display = 'none';
    outro.appendChild(el);
    outroCap.el = el;
  }

  // marquee
  const marquee = $('#marquee');
  marquee.style.top = LAY.marquee.top + 'px';
  const mqLists = LAY.marquee.merge ? [P.marquee.flat()] : P.marquee;
  const mqRows = mqLists.map((names, r) => {
    const row = document.createElement('div');
    row.className = 'mq-row';
    row.style.top = r * LAY.marquee.rowGap + 'px';
    const set = names.map((n) => `<div class="mq-chip"><i></i>${S.esc(n)}</div>`).join('');
    row.innerHTML = set + set + set + set;
    marquee.appendChild(row);
    return row;
  });

  function measureCaption(C) {
    const title = $('.cap-title', C.el);
    // dopasuj szerokość (kolumna hasła; wyśrodkowane hasło może być szersze)
    const max = C.el.classList.contains('cap-left') ? LAY.capMax : Math.min(W - 120, 1500);
    title.style.fontSize = '';
    const w = title.scrollWidth;
    if (w > max) title.style.fontSize = (86 * max) / w + 'px';
    const sub = $('.cap-sub', C.el);
    if (sub) {
      sub.style.fontSize = '';
      if (sub.scrollWidth > max) sub.style.fontSize = (38 * max) / sub.scrollWidth + 'px';
    }
    C.title = title;
    C.chars = $$('.ch', title);
    C.rights = C.chars.map((ch) => ch.offsetLeft + ch.offsetWidth);
    C.caret = $('.cap-caret', title);
    const fs = parseFloat(getComputedStyle(title).fontSize);
    C.caret.style.height = fs * 0.74 + 'px';
    C.caret.style.top = fs * 0.18 + 'px';
    C.words = $$('.w', C.el);
    C.bar = $('.cap-bar', C.el);
    C.dt = Math.min(0.055, 0.85 / Math.max(1, C.chars.length));
  }

  function renderCaption(C, t) {
    const [t0, t1] = C.at;
    const el = C.el;
    if (t < t0 - 0.001 || t > t1 + 0.4) { el.style.opacity = 0; el.style.visibility = 'hidden'; return; }
    el.style.visibility = 'visible';
    const out = prog(t, t1, t1 + 0.35, ease.easy);
    el.style.opacity = 1 - out;
    el.style.transform = `translateY(${-28 * out}px)`;
    el.style.filter = out > 0.001 ? `blur(${(7 * out).toFixed(2)}px)` : 'none';
    const pb = prog(t, t0, t0 + 0.45, ease.out);
    C.bar.style.transform = `scaleX(${pb})`;
    C.bar.style.opacity = clamp01(pb * 3);
    const start = t0 + 0.14;
    let last = -1;
    C.chars.forEach((ch, i) => {
      const ti = start + i * C.dt;
      const p = prog(t, ti, ti + 0.26, ease.out);
      ch.style.opacity = p;
      ch.style.transform = `translateY(${((1 - p) * 0.2).toFixed(4)}em)`;
      if (t >= ti) last = i;
    });
    const typingEnd = start + C.chars.length * C.dt;
    const on = t >= t0 + 0.06 && t < typingEnd + 0.95;
    const blink = t <= typingEnd || Math.floor((t - typingEnd) / 0.42) % 2 === 1;
    C.caret.style.opacity = on && blink ? 1 : 0;
    const x = last >= 0 ? C.rights[last] + 7 : -12;
    C.caret.style.transform = `translateX(${x}px)`;
    const ws = typingEnd - 0.08;
    C.words.forEach((w, i) => {
      const a = ws + i * 0.065;
      const p = prog(t, a, a + 0.42, ease.out);
      w.style.opacity = p;
      w.style.transform = `translateY(${((1 - p) * 16).toFixed(2)}px)`;
    });
  }

  // ---------------------------------------------------------------- media (wideo + kadry)
  const missing = [];
  const media = {}; // key -> { url, dur }
  function probe(base) {
    return new Promise((resolve) => {
      const exts = ['.webm', '.mp4', '.mov'];
      let i = 0;
      const v = document.createElement('video');
      v.muted = true;
      v.preload = 'auto';
      const next = () => {
        if (i >= exts.length) { resolve(null); return; }
        const url = base + exts[i++];
        v.onloadeddata = () => resolve({ url, dur: v.duration, video: v });
        v.onerror = next;
        v.src = url;
      };
      next();
    });
  }
  function seekVideo(v, time) {
    return new Promise((resolve) => {
      if (Math.abs(v.currentTime - time) < 0.001 && v.readyState >= 2) { resolve(); return; }
      const done = () => { v.removeEventListener('seeked', done); clearTimeout(to); resolve(); };
      const to = setTimeout(done, 4000);
      v.addEventListener('seeked', done);
      v.currentTime = time;
    });
  }
  function drawCover(canvas, src, sw, sh) {
    const cw = canvas.width, ch = canvas.height;
    const ctx = canvas.getContext('2d');
    const k = Math.max(cw / sw, ch / sh);
    const w = sw * k, h = sh * k;
    ctx.imageSmoothingQuality = 'high';
    ctx.drawImage(src, (cw - w) / 2, (ch - h) / 2, w, h);
  }
  function paintFallback(canvas, key) {
    const ctx = canvas.getContext('2d');
    const { width: w, height: h } = canvas;
    const g = ctx.createLinearGradient(0, 0, 0, h);
    g.addColorStop(0, '#8fa9c9'); g.addColorStop(0.45, '#d9e4f1'); g.addColorStop(0.46, '#f4f7fb'); g.addColorStop(1, '#e3ebf5');
    ctx.fillStyle = g; ctx.fillRect(0, 0, w, h);
    if (!RENDER) {
      ctx.fillStyle = 'rgba(11,28,52,.65)';
      ctx.font = `600 ${Math.round(w / 22)}px sans-serif`;
      ctx.fillText('brak pliku: ' + P.resorts[key].video + '.webm/.mp4', w * 0.05, h * 0.9);
    }
  }
  function sizeCanvas(c) {
    // rozdzielczość kadru = rozmiar CSS × 3 (telefon jest powiększony ~1.6×)
    const cw = c.parentElement.offsetWidth || 393, ch = c.parentElement.offsetHeight || 340;
    const k = Math.min(3, 1400 / cw);
    c.width = Math.round(cw * k);
    c.height = Math.round(ch * k);
  }
  async function loadMedia() {
    for (const key of Object.keys(P.resorts)) {
      const m = await probe(P.resorts[key].video);
      if (!m) missing.push(P.resorts[key].video + '.webm / .mp4');
      media[key] = m;
    }
    // kadry (canvas.still)
    for (const c of $$('canvas.still')) {
      sizeCanvas(c);
      const key = c.dataset.media;
      const m = media[key];
      if (!m) { paintFallback(c, key); continue; }
      const at = Math.min(parseFloat(c.dataset.at) || 0, Math.max(0, m.dur - 0.05));
      await seekVideo(m.video, at);
      drawCover(c, m.video, m.video.videoWidth, m.video.videoHeight);
    }
    // wideo w pełnym ekranie
    for (const pane of livePanes) {
      const key = pane.dataset.key;
      const v = $('video', pane);
      const m = media[key];
      if (!m) {
        const c = document.createElement('canvas');
        c.className = 'fallback';
        c.width = 852 * 2; c.height = 393 * 2;
        paintFallback(c, key);
        v.replaceWith(c);
        continue;
      }
      v.src = m.url;
      v.loop = false;
      await new Promise((r) => { if (v.readyState >= 2) r(); else { v.onloadeddata = r; v.onerror = r; } });
      pane.videoEl = v;
      pane.dur = m.dur;
    }
  }
  // czas w nagraniu dla danej chwili filmu
  const liveClock = {
    r1: { start: T.expand[0], from: R1.stillAt, active: [T.expand[0] - 0.2, T.swipe[1] + 0.05] },
    r2: { start: T.swipe[0], from: R2.stillAt, active: [T.swipe[0] - 0.05, T.collapse[1] + 0.05] },
  };
  function videoTime(key, t, dur) {
    const c = liveClock[key];
    const vt = c.from + Math.max(0, t - c.start);
    return dur ? Math.min(vt, dur - 0.05) : vt; // krótkie nagranie: zatrzymaj na ostatniej klatce
  }

  // ---------------------------------------------------------------- śnieg
  const snowBack = $('#snow'), snowFront = $('#snow-front');
  snowBack.width = snowFront.width = W;
  snowBack.height = snowFront.height = H;
  function rng(seed) { return () => ((seed = (seed * 16807) % 2147483647) - 1) / 2147483646; }
  const flakes = (() => {
    const r = rng(1234);
    const back = [], front = [];
    const n = Math.round((110 * W * H) / (886 * 1920));
    for (let i = 0; i < n; i++) {
      const z = r();
      back.push({ x: r() * W, y: r() * H, r: 1 + z * 2.6, vy: 35 + z * 85, a: 8 + r() * 26, f: 0.15 + r() * 0.35, ph: r() * 6.28, dr: -6 + r() * 12, o: 0.18 + z * 0.4 });
    }
    for (let i = 0; i < 9; i++) {
      front.push({ x: r() * W, y: r() * H, r: 7 + r() * 9, vy: 140 + r() * 90, a: 20 + r() * 30, f: 0.1 + r() * 0.2, ph: r() * 6.28, dr: -10 + r() * 20, o: 0.07 + r() * 0.08 });
    }
    return { back, front };
  })();
  function drawSnow(canvas, list, t, soft, alpha) {
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, W, H);
    if (alpha <= 0) return;
    for (const f of list) {
      const y = ((f.y + f.vy * t) % (H + 40)) - 20;
      const x = (((f.x + f.dr * t + f.a * Math.sin(f.ph + t * f.f * 6.283)) % (W + 40)) + W + 40) % (W + 40) - 20;
      if (soft) {
        const g = ctx.createRadialGradient(x, y, 0, x, y, f.r);
        g.addColorStop(0, `rgba(255,255,255,${f.o * alpha})`);
        g.addColorStop(1, 'rgba(255,255,255,0)');
        ctx.fillStyle = g;
      } else {
        ctx.fillStyle = `rgba(255,255,255,${f.o * alpha})`;
      }
      ctx.beginPath();
      ctx.arc(x, y, f.r, 0, 6.2832);
      ctx.fill();
    }
  }

  // ---------------------------------------------------------------- helpers ekranów
  function showScreen(el, on) { el.style.visibility = on ? 'visible' : 'hidden'; }
  function slide(el, x, dimAmt = 0, shadow = false) {
    el.style.transform = `translate3d(${x.toFixed(2)}px,0,0)`;
    $('.dim', el).style.opacity = dimAmt;
    el.style.boxShadow = shadow ? '-10px 0 30px rgba(0,0,0,.35)' : 'none';
  }
  function setCount(root, k) {
    for (const el of $$('[data-count]', root)) el.textContent = Math.round(parseFloat(el.dataset.count) * k);
  }
  function tapAt(t, t0, x, y, dur = 0.34) {
    // zwraca {o, s} kółka dotyku (wciśnięcie -> puszczenie)
    const a = t0 - 0.16, b = t0 + dur;
    if (t < a || t > b) return null;
    const pIn = prog(t, a, t0, ease.out);
    const pOut = prog(t, t0 + 0.06, b, ease.easy);
    return { x, y, o: pIn * (1 - pOut), s: lerp(0.7, 1, pIn) + pOut * 0.35 };
  }

  const detail = (key) => {
    const root = scr[key];
    return {
      root,
      content: $('.content', root),
      tabs: $('.tabs', root),
      tabEls: $$('.tab', root),
      ul: $('.ul', root),
      cams: $('.cams-pane', root),
      fadeOnScroll: [$('.d-logo', root), $('.d-country', root), $('.d-top', root)],
      statusBg: $('.d-statusbg', root),
      wcard: $('.wcard', root),
      statsBlock: $('.d-stats', root),
    };
  };
  const D1 = detail('r1');
  const D2 = detail('r2');
  function renderDetail(D, scroll, t, countK, openK) {
    D.content.style.transform = `translate3d(0,${(-scroll).toFixed(2)}px,0)`;
    const tabTop = 940.5;
    D.tabs.style.transform = `translateY(${Math.max(0, scroll + 35 - tabTop).toFixed(2)}px)`;
    const fo = 1 - clamp01((scroll - 120) / 140);
    D.fadeOnScroll.forEach((e) => { e.style.opacity = fo; });
    D.statusBg.style.opacity = clamp01((scroll - 200) / 100);
    for (const el of $$('[data-count]', D.statsBlock)) el.textContent = Math.round(parseFloat(el.dataset.count) * countK);
    for (const el of $$('.w-open [data-count]', D.wcard)) el.textContent = Math.round(parseFloat(el.dataset.count) * openK);
  }

  // stan list
  const L = {
    typed: $('.typed', scr.list), ph: $('.ph', scr.list), caret: $('.caret', scr.list),
    all: $('.l-all', scr.list), res: $('.l-res', scr.list), cnt: $('.cnt', scr.list),
  };
  const feed = { content: $('.content', scr.feed), news: $$('.news-card', scr.feed) };

  // ---------------------------------------------------------------- render(t)
  function render(t) {
    // tło / śnieg
    const fadeIn = range(t, T.fadeIn, ease.easy);
    const fadeOut = range(t, T.fadeOut, ease.easy);
    $('#fade').style.opacity = (1 - fadeIn) + fadeOut;
    drawSnow(snowBack, flakes.back, t, false, 1);
    drawSnow(snowFront, flakes.front, t, true, 1 - prog(t, 7.0, 7.6) + prog(t, 10.2, 10.9));

    // ---- telefon / kamera
    const c = camAt(t);
    const L_in = range(t, T.expand, ease.smooth);
    const L_out = range(t, T.collapse, ease.smooth);
    const land = t < T.collapse[0] ? L_in : 1 - L_out; // 0 = pion, 1 = poziom
    const rz = -90 * land;
    const pOp = prog(t, 0.05, 0.75) * (1 - prog(t, 17.4, 18.0));
    phone.style.opacity = pOp;
    phone.style.visibility = pOp > 0.001 ? 'visible' : 'hidden';
    phone.style.transform =
      `translate3d(${(PHONE_CX - 421 + c.x).toFixed(2)}px, ${(PHONE_CY - 880 + c.y).toFixed(2)}px, 0) ` +
      `rotateX(${c.rx.toFixed(3)}deg) rotateY(${c.ry.toFixed(3)}deg) rotateZ(${rz.toFixed(3)}deg) scale(${(PHONE_S0 / 2 * c.s).toFixed(4)})`;

    // ---- ekrany
    const pList = range(t, T.pushList, ease.out);
    const pDet = range(t, T.pushDetail, ease.out);
    const pPop = range(t, T.pop, ease.out);
    const underR2 = t >= (T.swipe[0] + T.swipe[1]) / 2;

    showScreen(scr.home, t < T.pushList[1] + 0.01);
    slide(scr.home, -118 * pList, 0.18 * pList);

    showScreen(scr.list, t >= T.pushList[0] && t < T.pushDetail[1] + 0.01);
    slide(scr.list, 393 * (1 - pList) - 118 * pDet, 0.18 * pDet, pList < 1);

    showScreen(scr.r1, t >= T.pushDetail[0] && !underR2);
    slide(scr.r1, 393 * (1 - pDet), 0, pDet < 1);

    showScreen(scr.r2, underR2 && t < T.pop[1] + 0.01);
    slide(scr.r2, 393 * pPop, 0, pPop > 0);

    showScreen(scr.feed, t >= T.pop[0]);
    slide(scr.feed, -118 * (1 - pPop), 0.18 * (1 - pPop));

    // ---- lista: wpisywanie
    const qs = Array.from(P.searchQuery);
    const nTyped = t < T.typeStart ? 0 : Math.min(qs.length, 1 + Math.floor((t - T.typeStart) / T.typeDt));
    L.typed.textContent = qs.slice(0, nTyped).join('');
    L.ph.style.opacity = nTyped ? 0 : 1;
    const focused = t >= T.pushList[1] - 0.05;
    const typingEnd = T.typeStart + qs.length * T.typeDt;
    const caretBlink = t < T.typeStart || t > typingEnd ? Math.floor((t - T.pushList[1]) / 0.5) % 2 === 0 : true;
    L.caret.style.opacity = focused && caretBlink && t < T.tapResult ? 1 : 0;
    L.caret.style.left = (53.5 + (nTyped ? L.typed.offsetWidth + 1.5 : 0)) + 'px';
    const pf = prog(t, T.filterAt, T.filterAt + 0.22, ease.easy);
    L.all.style.opacity = 1 - pf;
    L.all.style.transform = `translateY(${10 * pf}px)`;
    const pr = prog(t, T.filterAt + 0.08, T.filterAt + 0.4, ease.out);
    L.res.style.opacity = pr;
    L.res.style.transform = `translateY(${14 * (1 - pr)}px)`;
    L.cnt.textContent = t >= T.filterAt ? 1 : P.listTotal;

    // ---- 1. ośrodek: szczegóły
    const s1 = range(t, T.scroll1, ease.smooth), s2 = range(t, T.scroll2, ease.smooth);
    const kScroll = 309 * s1 + (905.5 - 309) * s2;
    renderDetail(D1, kScroll, t, range(t, T.countR1, ease.out), range(t, T.countOpenR1, ease.out));
    const ts = range(t, T.tabSlide, ease.smooth);
    D1.ul.style.left = lerp(S.TAB_X[0], S.TAB_X[1], ts) + 'px';
    D1.ul.style.width = lerp(S.TAB_W[0], S.TAB_W[1], ts) + 'px';
    D1.tabEls.forEach((e, i) => e.classList.toggle('on', ts < 0.5 ? i === 0 : i === 1));
    D1.cams.style.opacity = prog(t, T.tabSlide[0] + 0.05, T.tabSlide[1] + 0.05);
    const playCirc = $('.play-circ', D1.cams);
    if (playCirc) playCirc.style.transform = `scale(${1 - 0.12 * prog(t, T.tapPlay - 0.12, T.tapPlay, ease.out) * (1 - prog(t, T.tapPlay, T.tapPlay + 0.2))})`;

    // ---- 2. ośrodek: szczegóły
    const r2Scroll = 309 * range(t, T.scroll3, ease.smooth);
    renderDetail(D2, r2Scroll, t, range(t, T.countR2, ease.out), range(t, [T.countR2[0] + 0.2, T.countR2[1] + 0.3], ease.out));

    // ---- Start: kanał
    const fs = range(t, T.feedScroll, ease.smooth);
    feed.content.style.transform = `translate3d(0,${(-36 * fs).toFixed(2)}px,0)`;
    setCount(scr.feed, range(t, T.countFeed, ease.out));
    const ns = range(t, T.newsSwipe, ease.smooth);
    feed.news.forEach((n) => { n.style.transform = `translateX(${(-38 * ns).toFixed(2)}px)`; });

    // ---- pełny ekran na żywo
    const liveOn = t >= T.expand[0] && t <= T.collapse[1];
    live.style.visibility = liveOn ? 'visible' : 'hidden';
    liveBackdrop.style.opacity = liveOn ? land : 0;
    statusbar.style.opacity = 1 - land;
    if (liveOn) {
      const expanding = t < T.collapse[0];
      // prostokąt startowy (karta kamery) i końcowy (hero 2. ośrodka)
      const from = expanding ? { cx: 20.4 + 176.25, cy: 139 + 99.1, w: 352.5, h: 198.2, r: 20 } : { cx: 196.5, cy: 170, w: 393, h: 340, r: 0 };
      const k = land;
      const w = lerp(from.w, 852, k), h = lerp(from.h, 393, k);
      const cx = lerp(from.cx, 196.5, k), cy = lerp(from.cy, 426, k);
      live.style.width = w + 'px';
      live.style.height = h + 'px';
      live.style.transform = `translate(${(cx - w / 2).toFixed(2)}px, ${(cy - h / 2).toFixed(2)}px) rotate(${(90 * k).toFixed(3)}deg)`;
      const rr = from.r * (1 - k);
      live.style.borderRadius = `${rr}px ${rr}px 0 0`;
      const sw = range(t, T.swipe, ease.smooth);
      livePanes.forEach((p) => { p.style.width = w + 'px'; });
      liveTrack.style.transform = `translateX(${(-w * sw).toFixed(2)}px)`;
      // nakładki
      const ovIn = prog(t, T.expand[1] - 0.15, T.expand[1] + 0.35, ease.out);
      const ovOut = prog(t, T.collapse[0], T.collapse[0] + 0.25);
      livePanes.forEach((p) => {
        const b = $('.live-badge', p);
        b.style.left = lerp(9.5, 64, expanding ? k : 1) + 'px';
        b.style.top = lerp(10.5, 20, expanding ? k : 1) + 'px';
        b.style.opacity = expanding ? 1 : 1 - ovOut;
        const o = expanding ? ovIn : 1 - ovOut;
        for (const e of $$('.ov-grad, .ov-info, .ov-cond', p)) {
          e.style.opacity = o;
          e.style.transform = e.classList.contains('ov-grad') ? '' : `translateY(${(1 - o) * 12}px)`;
        }
        $('.play-circ', p).style.opacity = expanding ? 1 - prog(t, T.expand[0], T.expand[0] + 0.18) : 0;
      });
      // koniec zwijania: wideo przechodzi w kadr zdjęcia (ta sama klatka)
      live.style.opacity = expanding ? 1 : 1 - prog(t, T.collapse[1] - 0.28, T.collapse[1]);
    }

    // ---- dotyk
    const taps = [
      tapAt(t, T.tapSearch, 196, 298),
      tapAt(t, T.tapResult, 196, 366),
      tapAt(t, T.tapCams, 150, 655.5, 0.28),
      tapAt(t, T.tapPlay, 196.5, 238),
      tapAt(t, T.tapStart, 39, 778),
    ].filter(Boolean);
    // przeciągnięcie (zmiana kamery) — w układzie telefonu: z dołu do góry = w poziomie z prawej do lewej
    const sw0 = T.swipe[0] - 0.12, sw1 = T.swipe[1] - 0.05;
    if (t >= sw0 - 0.1 && t <= sw1 + 0.25) {
      const pIn = prog(t, sw0 - 0.1, sw0, ease.out);
      const pm = prog(t, sw0, sw1, ease.smooth);
      const pOut = prog(t, sw1, sw1 + 0.25);
      taps.push({ x: 196.5, y: lerp(640, 230, pm), o: pIn * (1 - pOut), s: 1 });
    }
    const tp = taps[0];
    if (tp) {
      touch.style.opacity = tp.o;
      touch.style.transform = `translate(${tp.x}px, ${tp.y}px) scale(${tp.s})`;
    } else touch.style.opacity = 0;

    // ---- hasła
    for (const C of CAPS) renderCaption(C, t);
    const mq = prog(t, T.marquee[0], T.marquee[0] + 0.45) * (1 - prog(t, T.marquee[1] - 0.35, T.marquee[1]));
    marquee.style.opacity = mq;
    marquee.style.visibility = mq > 0 ? 'visible' : 'hidden';
    mqRows.forEach((row, i) => {
      const dir = i % 2 ? 1 : -1;
      const x = (i % 2 ? -row.scrollWidth / 2 : 0) + dir * 62 * (t - T.marquee[0]) + (1 - mq) * 30 * dir;
      row.style.transform = `translateX(${x.toFixed(2)}px)`;
    });

    // ---- outro
    const oOn = t >= T.logoIn[0] - 0.01;
    outro.style.opacity = oOn ? 1 : 0;
    if (oOn) {
      const pl = range(t, T.logoIn, ease.out);
      outroLogo.style.opacity = pl;
      outroLogo.style.transform = `translateY(${(1 - pl) * 30}px) scale(${lerp(0.92, 1, pl)})`;
      outroLogo.style.filter = pl < 0.999 ? `blur(${((1 - pl) * 12).toFixed(2)}px)` : 'none';
      if (outroBar) outroBar.style.transform = `scaleX(${range(t, T.logoBar, ease.smooth)})`;
      renderCaption(outroCap, t);
      const ps = range(t, T.outroSub, ease.out);
      outroSub.style.opacity = ps;
      outroSub.style.letterSpacing = lerp(8, 4, ps) + 'px';
    }
  }

  // ---------------------------------------------------------------- synchronizacja wideo
  function liveNeeds(t) {
    const out = [];
    for (const pane of livePanes) {
      const v = pane.videoEl;
      if (!v) continue;
      const a = liveClock[pane.dataset.key].active;
      if (t >= a[0] && t <= a[1]) out.push({ v, target: videoTime(pane.dataset.key, t, pane.dur) });
    }
    return out;
  }
  async function syncVideosExact(t) {
    await Promise.all(liveNeeds(t).map(({ v, target }) => seekVideo(v, target)));
  }
  function syncVideosLive(t, playing) {
    const need = liveNeeds(t);
    for (const pane of livePanes) {
      const v = pane.videoEl;
      if (!v) continue;
      const n = need.find((x) => x.v === v);
      if (!n) { if (!v.paused) v.pause(); continue; }
      if (!playing) { if (!v.paused) v.pause(); if (Math.abs(v.currentTime - n.target) > 0.02) v.currentTime = n.target; continue; }
      if (Math.abs(v.currentTime - n.target) > 0.25) v.currentTime = n.target;
      if (v.paused) v.play().catch(() => {});
    }
  }

  // ---------------------------------------------------------------- start
  const raf2 = () => new Promise((r) => requestAnimationFrame(() => requestAnimationFrame(r)));
  async function init() {
    if (RENDER) document.body.classList.add('render');
    await document.fonts.load('800 86px InterPromo');
    await document.fonts.load('500 38px InterPromo');
    await document.fonts.load('400 16px InterPromo');
    await document.fonts.load('700 16px InterPromo');
    await document.fonts.ready;
    CAPS.forEach(measureCaption);
    measureCaption(outroCap);
    await outroImgReady;
    // dopasuj podpis w outro
    outroSub.style.letterSpacing = '8px';
    if (outroSub.scrollWidth > LAY.outro.subMax) outroSub.style.fontSize = (25 * LAY.outro.subMax) / outroSub.scrollWidth + 'px';
    await loadMedia();
    // obrazki UI
    await Promise.all($$('img').map((im) => (im.complete ? 0 : new Promise((r) => { im.onload = im.onerror = r; }))));
    render(0);
    await raf2();
  }
  const ready = init();

  window.__info = { fps: FPS, duration: DUR, width: W, height: H, missing };
  window.__ready = ready.then(() => window.__info);
  window.__seek = async (t) => {
    render(t);
    await syncVideosExact(t);
    await raf2();
    return true;
  };

  if (RENDER) return;

  // ---------------------------------------------------------------- podgląd w przeglądarce
  const hud = document.createElement('div');
  hud.id = 'hud';
  hud.innerHTML = `<button id="pp">▶︎ / ❚❚</button><button id="rs">⟲</button>
    <input id="scrub" type="range" min="0" max="${DUR}" step="${1 / FPS}" value="0"><span class="t" id="tt">0.00 s</span><span class="warn" id="warn"></span>`;
  document.body.appendChild(hud);
  const scrub = $('#scrub'), tt = $('#tt');
  let playing = !params.has('pause');
  let t = parseFloat(params.get('t')) || 0;
  let last = null;
  function fit() {
    const k = Math.min(innerWidth / W, (innerHeight - 70) / H);
    stage.style.transformOrigin = '0 0';
    stage.style.position = 'absolute';
    stage.style.left = (innerWidth - W * k) / 2 + 'px';
    stage.style.top = Math.max(0, (innerHeight - 70 - H * k) / 2) + 'px';
    stage.style.transform = `scale(${k})`;
  }
  $('#viewport').style.display = 'block';
  addEventListener('resize', fit);
  fit();
  $('#pp').onclick = () => { playing = !playing; last = null; };
  $('#rs').onclick = () => { t = 0; playing = true; last = null; };
  scrub.oninput = () => { t = parseFloat(scrub.value); playing = false; };
  addEventListener('keydown', (e) => {
    if (e.code === 'Space') { playing = !playing; last = null; e.preventDefault(); }
    if (e.key === 'r' || e.key === 'R') { t = 0; playing = true; last = null; }
    if (e.key === 'ArrowRight') { playing = false; t = Math.min(DUR, t + (e.shiftKey ? 1 : 1 / FPS)); }
    if (e.key === 'ArrowLeft') { playing = false; t = Math.max(0, t - (e.shiftKey ? 1 : 1 / FPS)); }
    if (e.key === 'h' || e.key === 'H') hud.style.display = hud.style.display === 'none' ? '' : 'none';
  });
  ready.then(() => {
    if (missing.length) $('#warn').textContent = 'Brak: ' + missing.join(', ') + ' — patrz README';
    const loop = (now) => {
      if (playing) {
        if (last != null) t += (now - last) / 1000;
        last = now;
        if (t >= DUR) { t = params.has('loop') ? 0 : DUR; if (!params.has('loop')) playing = false; }
      } else last = null;
      render(t);
      syncVideosLive(t, playing);
      scrub.value = t;
      tt.textContent = t.toFixed(2) + ' s';
      requestAnimationFrame(loop);
    };
    requestAnimationFrame(loop);
  });
})();
