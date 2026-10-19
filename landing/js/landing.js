/* WebCameraSki landing page. Mały skrypt: pisany nagłówek, animacje przy przewijaniu,
   przełącznik kamer i film. Wideo i plakaty ładują się dopiero, gdy sekcja jest blisko ekranu. */
(() => {
  document.documentElement.classList.add('js');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const whenNear = (el, fn) => {
    if (!el) return;
    const io = new IntersectionObserver(([e]) => { if (e.isIntersecting) { io.disconnect(); fn(); } }, { rootMargin: '300px' });
    io.observe(el);
  };

  // cień paska po przewinięciu
  const topbar = document.querySelector('.topbar');
  const onScroll = () => topbar.classList.toggle('scrolled', scrollY > 8);
  addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // nagłówek pisany jak w aplikacji (czerwony kursor)
  const h1 = document.querySelector('.type');
  if (h1 && !reduce) {
    // "|" = nowa linia; litery jednego słowa trzymają się razem (bez łamania w środku słowa)
    const lines = h1.dataset.text.split('|');
    h1.setAttribute('aria-label', lines.join(' '));
    const word = (w) => `<span class="word" aria-hidden="true">${Array.from(w).map((c) => `<span class="ch">${c}</span>`).join('')}</span>`;
    h1.innerHTML = lines.map((l) => l.split(' ').map(word).join(' ')).join('<br>') + '<span class="caret" aria-hidden="true"></span>';
    h1.querySelectorAll('.ch').forEach((c, i) => setTimeout(() => c.classList.add('on'), 200 + i * 55));
  }

  // pojawianie się sekcji
  const reveal = new IntersectionObserver((entries) => {
    for (const e of entries) if (e.isIntersecting) { e.target.classList.add('in'); reveal.unobserve(e.target); }
  }, { threshold: 0.12 });
  document.querySelectorAll('[data-reveal]').forEach((el) => reveal.observe(el));

  // przełącznik kamer
  const screen = document.querySelector('.land-screen');
  const video = document.querySelector('.cam-video');
  const info = document.querySelector('.cam-info');
  const tabs = [...document.querySelectorAll('.cam-switch button')];
  const setCam = (btn, instant) => {
    tabs.forEach((b) => b.setAttribute('aria-selected', String(b === btn)));
    const key = btn.dataset.cam;
    const apply = () => {
      screen.style.backgroundImage = `url(img/poster-${key}.webp)`;
      video.src = `media/loop-${key}.mp4`;
      info.querySelector('.cam-name').textContent = btn.dataset.name;
      info.querySelector('.cam-city').textContent = btn.dataset.city;
      info.querySelector('.cam-logo').src = `img/logo-${key}.webp`;
      if (!reduce) video.play().catch(() => {});
      video.style.opacity = 1;
      info.style.opacity = 1;
    };
    if (instant || reduce) { apply(); return; }
    video.style.opacity = 0;
    info.style.opacity = 0;
    setTimeout(apply, 380);
  };
  tabs.forEach((b) => b.addEventListener('click', () => setCam(b)));
  whenNear(screen, () => setCam(tabs[0], true));

  // film: poziomy na komputerze, pionowy na telefonie
  const film = document.querySelector('.film-video');
  whenNear(film, () => {
    const tall = matchMedia('(max-width: 640px)').matches;
    film.poster = tall ? film.dataset.posterTall : film.dataset.posterWide;
    film.src = tall ? film.dataset.srcTall : film.dataset.srcWide;
    if (tall) film.parentElement.classList.add('tall');
  });

  // rok w stopce
  const y = document.querySelector('.year');
  if (y) y.textContent = new Date().getFullYear();
})();
