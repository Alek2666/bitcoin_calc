/*
 * Wersja pozioma 16:9 (1920×1080) — nadpisuje wybrane pola z js/data.js.
 * Inne ośrodki niż w wersji pionowej: Master Ski i Kasprowy Wierch.
 */
Object.assign(window.PROMO, {
  format: '16x9',

  resorts: {
    r1: {
      name: 'Master-Ski',
      city: 'Tylicz', region: 'woj. małopolskie', country: 'Polska',
      logo: 'assets/masterski-logo.png', logoFit: 'cover',
      video: 'assets/masterski',          // nagranie WEBC1_2026-02-12-12-55
      snow: 80, runs: 11, runsOpen: 11, lifts: 6, liftsOpen: 6,
      distance: '18.6 km',
      stillAt: 2.0,
      // nagranie: słońce, duża chmura, luty w południe
      weather: {
        temp: -2, cond: 'Małe zachmurzenie', icon: 'sun', wind: 11, humidity: 74,
        days: [
          { label: 'Dziś',  hi: -1, lo: -7, precip: 0, icon: 'sun' },
          { label: 'Jutro', hi: -3, lo: -8, precip: 20, icon: 'cloud' },
        ],
      },
      camsTotal: 7,
      cams: [
        { title: 'MASTER SKI Tylicz', live: true },
        { title: 'MASTER SKI Tylicz', placeholder: true },
      ],
    },
    r2: {
      name: 'Kasprowy Wierch - PKL',
      city: 'Zakopane', region: 'woj. małopolskie', country: 'Polska',
      logo: 'assets/kasprowy-logo.png', logoFit: 'cover',
      video: 'assets/kasprowy',           // nagranie WEBC1_2025-03-19-09-25
      snow: 110, runs: 3, runsOpen: 3, lifts: 3, liftsOpen: 3,
      distance: '96.4 km',
      stillAt: 1.0,
      // nagranie: Tatry, bezchmurnie, poranek
      weather: {
        temp: -8, cond: 'Bezchmurnie', icon: 'sun', wind: 18, humidity: 55,
        days: [
          { label: 'Dziś',  hi: -5, lo: -12, precip: 0, icon: 'sun' },
          { label: 'Jutro', hi: -6, lo: -13, precip: 0, icon: 'sun' },
        ],
      },
    },
  },

  searchQuery: 'Master',
  stats: { resorts: 111, open: 96, runs: 636 },

  marquee: [
    ['Master-Ski', 'Czarny Groń - Rzyki', 'Bania Ski & Fun', 'Beskid Sport Arena', 'Kasina SKI'],
    ['Kasprowy Wierch - PKL', 'Kotelnica Białczańska', 'Bachledka Ski & Sun', 'Zieleniec Sport Arena'],
  ],
});
