/* Budowa ekranów aplikacji (DOM w punktach iOS 393×852). */
(() => {
  const P = window.PROMO;
  const IP = window.ICON_PATHS;

  const ic = (name, size, color, style = '') =>
    `<svg class="i" viewBox="0 0 24 24" width="${size}" height="${size}" fill="${color}" style="${style}">${IP[name]}</svg>`;

  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const fmtT = (v) => (v > 0 ? '+' : '') + v;

  function weatherIcon(kind, size = 30) {
    if (kind === 'sun') {
      let rays = '';
      for (let k = 0; k < 8; k++) {
        const a = (k * Math.PI) / 4;
        const x1 = 15 + Math.cos(a) * 9, y1 = 15 + Math.sin(a) * 9;
        const x2 = 15 + Math.cos(a) * 12.5, y2 = 15 + Math.sin(a) * 12.5;
        rays += `<line x1="${x1.toFixed(2)}" y1="${y1.toFixed(2)}" x2="${x2.toFixed(2)}" y2="${y2.toFixed(2)}"/>`;
      }
      return `<svg class="wi" viewBox="0 0 30 30" width="${size}" height="${size}"><g stroke="rgba(255,204,1,.16)" stroke-width=".8" stroke-linecap="round">${rays}</g><circle cx="15" cy="15" r="5.6" fill="#ffcc01"/></svg>`;
    }
    if (kind === 'snow') {
      return `<svg class="wi" viewBox="0 0 30 30" width="${size}" height="${size}"><g transform="translate(3 1) scale(1)"><path fill="#c9d6ea" d="${cloudD()}"/></g>` +
        `<g fill="#ffffff"><circle cx="10" cy="25" r="1.5"/><circle cx="15.5" cy="27" r="1.5"/><circle cx="21" cy="25" r="1.5"/></g></svg>`;
    }
    return `<svg class="wi" viewBox="0 0 30 30" width="${size}" height="${size}"><g transform="translate(3 3)"><path fill="#c9d6ea" d="${cloudD()}"/></g></svg>`;
  }
  function cloudD() {
    return 'M19.35 10.04A7.49 7.49 0 0 0 12 4C9.11 4 6.6 5.64 5.35 8.04A5.994 5.994 0 0 0 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96z';
  }

  // Flagi jak emoji w aplikacji (Słowacja z herbem — bez niego wyglądałaby jak inna flaga)
  function flag(code, w = 12, h = 8) {
    const svg = code === 'sk'
      ? '<rect width="30" height="20" fill="#fff"/><rect y="6.67" width="30" height="6.67" fill="#0b4ea2"/><rect y="13.33" width="30" height="6.67" fill="#ee1c25"/>' +
        '<path d="M5 4h8.6v6.8c0 3-2.2 4.8-4.3 5.7C7.2 15.6 5 13.8 5 10.8z" fill="#ee1c25" stroke="#fff" stroke-width="1"/>' +
        '<rect x="8.75" y="5.6" width="1.1" height="8" fill="#fff"/><rect x="7.3" y="7.1" width="4" height="1" fill="#fff"/><rect x="6.7" y="9.2" width="5.2" height="1.1" fill="#fff"/>' +
        '<path d="M5.7 13.4c1-1.5 2.4-1.3 3.6-.2 1.2-1.1 2.6-1.3 3.6.2-.9 1.5-2.2 2.4-3.6 3-1.4-.6-2.7-1.5-3.6-3z" fill="#0b4ea2"/>'
      : '<rect width="30" height="20" fill="#fff"/><rect y="10" width="30" height="10" fill="#dc143c"/>';
    return `<svg class="flag" viewBox="0 0 30 20" width="${w}" height="${h}" preserveAspectRatio="none">${svg}</svg>`;
  }

  // ---------- pasek statusu / nawigacja ----------
  function statusBar() {
    const signal = `<svg viewBox="0 0 19 12" width="19" height="12" fill="#fff"><rect x="0" y="8" width="3.2" height="4" rx="1"/><rect x="5.2" y="5.5" width="3.2" height="6.5" rx="1"/><rect x="10.4" y="3" width="3.2" height="9" rx="1"/><rect x="15.6" y="0" width="3.2" height="12" rx="1"/></svg>`;
    const wifi = `<svg viewBox="0 0 17 12.5" width="17" height="12.5" fill="#fff"><path d="M8.5 2.3c2.4 0 4.6.9 6.3 2.5l1.3-1.3C14.1 1.5 11.4.4 8.5.4S2.9 1.5.9 3.5l1.3 1.3C3.9 3.2 6.1 2.3 8.5 2.3z"/><path d="M8.5 5.9c1.4 0 2.7.5 3.7 1.4l1.3-1.3c-1.3-1.2-3.1-2-5-2s-3.7.8-5 2l1.3 1.3c1-.9 2.3-1.4 3.7-1.4z"/><path d="M8.5 9.4c.5 0 1 .2 1.3.5L8.5 12.5 7.2 9.9c.3-.3.8-.5 1.3-.5z"/></svg>`;
    return `<div class="statusbar">
      <div class="sb-time">${esc(P.statusTime)}</div>
      <div class="sb-icons">${signal}${wifi}
        <div class="battery"><div class="shell"></div><div class="pct">100</div><div class="cap"></div></div>
      </div></div>`;
  }

  function navBar() {
    const items = [
      ['home', 'Start', true], ['terrain_o', 'Ośrodki'], ['map_o', 'Mapa'], ['heart_o', 'Ulubione'], ['person_o', 'Konto'],
    ];
    return `<div class="navbar">${items.map(([i, l, on]) =>
      `<div class="nav-item${on ? ' active' : ''}">${ic(i, 23, on ? '#fff' : 'var(--nav-icon)')}<span>${l}</span></div>`).join('')}</div>`;
  }

  // ---------- Start (góra) ----------
  function homeScreen() {
    const R = P.resorts;
    const near = [
      ['r1', R.r1, 20],
      ['r2', R.r2, 225.4],
    ].map(([key, r, x]) => `
      <div class="near-card" style="left:${x}px;top:512.5px">
        <div class="near-img"><canvas class="still" data-media="${key}" data-at="${r.stillAt}"></canvas>
          <div class="near-km">${ic('near_me', 14, '#fff')}${esc(r.distance)}</div>
          <div class="near-status">${esc(P.statusOpen)}</div>
          <div class="near-heart">${ic('heart_o', 19, '#fff')}</div>
        </div>
        <div class="near-name">${esc(r.name)}</div>
        <div class="near-meta">${ic('snow', 15, 'var(--t3)')}${r.snow} cm<span class="gap"></span>${ic('route', 15, 'var(--t3)')}${r.runs} tras</div>
      </div>`).join('');
    return `<div class="scr" id="s-home"><div class="content">
        <img class="home-hero" src="assets/ui/home-hero.jpg" alt="">
        <div class="sec-title" style="top:465.6px">Blisko Ciebie</div>
        <div class="abs" style="left:338px;top:466px">${ic('refresh', 24.5, '#fff')}</div>
        ${near}
      </div><div class="dim"></div></div>`;
  }

  // ---------- Start (przewinięty: Aktualności + W liczbach) ----------
  function feedScreen() {
    const n = P.news;
    const news = n.slice(0, 2).map((a, k) => `
      <div class="news-card" style="left:${k ? 225.4 : 20}px;top:287.1px">
        <div class="news-img"><img src="${esc(a.img)}" alt=""></div>
        <div class="news-title">${esc(a.title)}</div>
        <div class="news-date">${ic('calendar_o', 16, 'var(--t3)')}${esc(a.date)}</div>
      </div>`).join('');
    return `<div class="scr" id="s-feed">
        <div class="status-bg"></div>
        <div class="hbar">${ic('menu', 26, '#fff', 'position:absolute;left:15px;top:15.5px')}${window.LOGO_SVG}</div>
        <div class="content">
          <img src="assets/ui/skipass-strip.jpg" alt="" style="position:absolute;left:0;top:103.8px;width:393px;height:70.6px">
          <div class="sec-title" style="top:240.5px">Aktualności</div>
          <div class="abs" style="left:342.5px;top:244px">${ic('list_alt', 24, '#fff')}</div>
          ${news}
          <div class="sec-title" style="top:526.5px">W liczbach</div>
          <div class="stats-card" style="top:567.9px">
            <div class="col">${ic('terrain', 22, '#fff')}<div class="num" data-count="${P.stats.resorts}">${P.stats.resorts}</div><div class="lbl">ośrodków</div></div>
            <div class="col">${ic('check_circle_o', 22, '#fff')}<div class="num" data-count="${P.stats.open}">${P.stats.open}</div><div class="lbl">czynnych</div></div>
            <div class="col">${ic('route', 22, '#fff')}<div class="num" data-count="${P.stats.runs}">${P.stats.runs}</div><div class="lbl">tras łącznie</div></div>
          </div>
        </div><div class="dim"></div></div>`;
  }

  // ---------- Ośrodki narciarskie (wyszukiwanie) ----------
  function listCard(r, thumbHtml) {
    return `<div class="l-card">
      <div class="l-thumb">${thumbHtml}</div>
      <div class="l-name">${esc(r.name)}</div>
      <div class="l-loc">${flag(r.flag || 'pl')}<span>${esc(r.loc)}</span></div>
      <div class="l-meta">${ic('snow', 14.5, 'var(--t3)')}${r.snow} cm<span class="gap"></span>${ic('route', 14.5, 'var(--t3)')}${r.runs} tras</div>
      <div class="l-status">${ic('check_circle_o', 14.5, 'var(--t3)')}${esc(P.statusOpen)}</div>
      <div class="l-heart">${ic('heart_o', 20.5, '#fff')}</div>
    </div>`;
  }
  function listScreen() {
    const all = P.list.map((r) => listCard(r, `<img src="${esc(r.img)}" alt="">`)).join('');
    const k = P.resorts.r1;
    const res = listCard(
      { name: k.name, loc: `${k.city}, ${k.region}`, flag: 'pl', snow: k.snow, runs: k.runs },
      `<canvas class="still" data-media="r1" data-at="${k.stillAt}"></canvas>`);
    return `<div class="scr" id="s-list"><div class="content">
        <div class="l-head">${ic('chevron_back', 22, '#fff', 'position:absolute;left:19px;top:18px')}<h1>Ośrodki narciarskie</h1></div>
        <div class="l-search">${ic('search', 24, '#e8ecf3', 'position:absolute;left:15px;top:14px')}
          <span class="ph">Szukaj ośrodka, regionu...</span><span class="typed"></span><i class="caret"></i></div>
        <div class="l-chips">
          <div class="chip sel">${ic('check', 15, 'var(--red)')}Wszystkie</div>
          <div class="chip">${flag('pl', 15, 10)}Polska</div>
          <div class="chip">${flag('sk', 15, 10)}Słowacja</div>
        </div>
        <div class="l-filters">
          <div class="fbtn">${ic('map_o', 19, '#fff')}Województwo</div>
          <div class="fbtn">${ic('sort', 19, '#fff')}Nazwa A-Z</div>
        </div>
        <div class="l-count">Liczba ośrodków: <span class="cnt">${P.listTotal}</span></div>
        <div class="l-list l-all">${all}</div>
        <div class="l-list l-res">${res}</div>
      </div><div class="dim"></div></div>`;
  }

  // ---------- Szczegóły ośrodka ----------
  const TAB_X = [16.2, 122, 209.7, 279, 365.8];
  const TAB_W = [73, 54, 36, 53.6, 38];
  function detailScreen(key) {
    const r = P.resorts[key];
    const w = r.weather;
    const cams = (r.cams || []).map((c, k) => `
      <div class="cam-card" style="top:${56 + k * 285.5}px">
        <div class="cam-img"><canvas class="still" data-media="${key}" data-at="${r.stillAt}"></canvas>
          ${c.live ? '<div class="live-badge"><i></i>NA ŻYWO</div><div class="play-circ">' + ic('play', 24, '#1c2a3f') + '</div>' : ''}
        </div>
        <div class="cam-body">${esc(c.title)}</div>
      </div>`).join('');
    const tabs = ['Informacje', 'Kamery', 'Trasy', 'Wyciągi', 'Mapa'];
    return `<div class="scr detail" id="s-${key}"><div class="content">
        <div class="d-hero"><canvas class="still hero" data-media="${key}" data-at="${r.heroAt ?? r.stillAt}"></canvas><div class="topfade"></div><div class="grad"></div></div>
        <div class="d-top">
          ${ic('arrow_back', 27, '#fff', 'position:absolute;left:14px;top:6.5px')}
          <div class="circ" style="left:276px">${ic('heart_o', 24, '#fff')}</div>
          <div class="circ" style="left:341px">${ic('share', 24, '#fff')}</div>
        </div>
        <div class="d-logo${r.logoFit === 'cover' ? ' fill' : ''}"><img src="${esc(r.logo)}" alt="" onerror="this.replaceWith(Object.assign(document.createElement('b'),{textContent:'${esc(r.name).slice(0, 1)}',style:'font:800 44px var(--font-display);color:#0b1c34'}))"></div>
        <div class="d-country">${flag('pl')}POLSKA</div>
        <div class="d-name">${esc(r.name)}</div>
        <div class="d-loc">${esc(r.city)}, ${esc(r.region)} • ${esc(r.country)}</div>
        <div class="d-pill">${esc(P.statusOpen)}</div>
        <div class="d-div"></div>
        <div class="d-stats">
          <div class="d-stat">${ic('snow', 26.5, '#fff')}<div class="v"><div class="n"><span data-count="${r.snow}">${r.snow}</span> cm</div><div class="l">śnieg</div></div></div>
          <div class="d-stat">${ic('route', 26.5, '#fff')}<div class="v"><div class="n" data-count="${r.runs}">${r.runs}</div><div class="l">tras</div></div></div>
          <div class="d-stat">${ic('lift', 26.5, '#fff')}<div class="v"><div class="n" data-count="${r.lifts}">${r.lifts}</div><div class="l">wyciągów</div></div></div>
        </div>
        <div class="d-btns">
          <div class="d-btn">${ic('near_me_o', 19, '#fff')}Nawiguj (GPS)</div>
          <div class="d-btn">${ic('heart_o', 19, '#fff')}Dodaj do ulubionych</div>
        </div>
        <div class="wcard">
          <div class="w-title">Pogoda na stoku</div>
          <div class="w-now">${ic('thermo', 32, 'var(--red)')}<span class="w-temp">${fmtT(w.temp)}°C</span><span class="w-cond">${esc(w.cond)}</span></div>
          <div class="w-extra">${ic('air', 17, 'var(--t3)')}${w.wind} km/h<span class="gap"></span>${ic('drop_o', 16, 'var(--t3)')}${w.humidity}% wilgotność</div>
          <div class="w-open l"><div class="num"><span data-count="${r.liftsOpen}">${r.liftsOpen}</span>/${r.lifts}</div><div class="lbl">wyciągi czynne</div></div>
          <div class="w-open r"><div class="num"><span data-count="${r.runsOpen}">${r.runsOpen}</span>/${r.runs}</div><div class="lbl">trasy czynne</div></div>
          <div class="w-div"></div>
          <div class="w-days">${w.days.map((d) => `
            <div class="w-day"><div class="d">${esc(d.label)}</div>${weatherIcon(d.icon)}
              <div class="t">${d.hi}°/${d.lo}°</div>
              <div class="p">${ic('drop_o', 15, 'var(--t3)')}${d.precip}%</div></div>`).join('')}
          </div>
        </div>
        <div class="tabs" style="top:940.5px">
          ${tabs.map((t, k) => `<div class="tab${k === 0 ? ' on' : ''}" style="left:${TAB_X[k]}px">${t}</div>`).join('')}
          <div class="tl"></div><div class="ul" style="left:${TAB_X[0]}px;width:${TAB_W[0]}px"></div>
        </div>
        <div class="cams-pane" style="top:988.5px;opacity:0">
          <div class="cams-title">Kamery (${(r.cams || []).length})</div>
          ${cams}
        </div>
      </div><div class="d-statusbg"></div><div class="dim"></div></div>`;
  }

  // ---------- Pełny ekran: kamera na żywo ----------
  function livePane(key) {
    const r = P.resorts[key];
    return `<div class="live-pane" data-key="${key}">
      <video muted playsinline preload="auto" data-media="${key}"></video>
      <div class="ov-grad"></div>
      <div class="live-badge"><i></i>NA ŻYWO</div>
      <div class="ov-info">
        <div class="ov-logo${r.logoFit === 'cover' ? ' fill' : ''}"><img src="${esc(r.logo)}" alt="" onerror="this.remove()"></div>
        <div><div class="ov-name">${esc(r.name)}</div><div class="ov-loc">${esc(r.city)} • ${fmtT(r.weather.temp)}°C</div></div>
      </div>
      <div class="ov-cond">
        <div class="ov-chip">${ic('snow', 15, '#fff')}${r.snow} cm</div>
        <div class="ov-chip">${ic('route', 15, '#fff')}${r.runsOpen}/${r.runs}</div>
        <div class="ov-chip">${ic('lift', 15, '#fff')}${r.liftsOpen}/${r.lifts}</div>
      </div>
    </div>`;
  }
  function liveLayer() {
    return `<div class="live-backdrop"></div><div class="live" id="live"><div class="live-track">${livePane('r1')}${livePane('r2')}</div></div>`;
  }

  function phone() {
    return `<div id="phone"><div class="phone-body">
      <i class="btn-side b-action"></i><i class="btn-side b-volup"></i><i class="btn-side b-voldn"></i><i class="btn-side b-power"></i>
      <div class="screen" id="screen">
        ${homeScreen()}${listScreen()}${detailScreen('r1')}${detailScreen('r2')}${feedScreen()}
        ${navBar()}
        ${liveLayer()}
        ${statusBar()}
        <div class="island"></div>
        <div class="touch" id="touch"></div>
      </div>
    </div></div>`;
  }

  window.Screens = { phone, ic, weatherIcon, TAB_X, TAB_W, fmtT, esc };
})();
