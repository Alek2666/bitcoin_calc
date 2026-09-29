/*
 * WebCameraSki — App Preview
 * Wszystkie teksty i dane widoczne w filmie. Edytuj śmiało — układ się dopasuje.
 *
 * WAŻNE (zima!): wartości pogody poniżej są przykładowe. Sprawdź je z nagraniami:
 * jeśli na wideo pada śnieg — ustaw icon: 'snow' i cond: 'Opady śniegu', itd.
 * Dostępne ikony pogody: 'sun' | 'cloud' | 'snow'.
 */
window.PROMO = {
  fps: 30,
  duration: 20,          // App Store: min 15 s, max 30 s
  statusTime: '9:41',

  // Hasła (nagłówek pisany "na maszynie" + podtytuł)
  captions: {
    search:     { title: 'Znajdź swój stok',     sub: 'ponad 100 ośrodków w jednej aplikacji' },
    conditions: { title: 'Warunki na żywo',      sub: 'śnieg, trasy i wyciągi' },
    live:       { title: 'Kamery na żywo',       sub: 'z niemal wszystkich stoków w Polsce' },
    weather:    { title: 'Pogoda na stoku',      sub: 'prognoza i kamery pogodowe' },
    feed:       { title: 'Kanał dla narciarzy',  sub: 'aktualności prosto ze stoków' },
    outro:      { title: 'Zawsze bliżej gór',    sub: 'OŚRODKI • TRASY • WYCIĄGI • KAMERY • POGODA' },
  },

  // Logo na końcu filmu: plik kopiowany przez `npm run assets` (pole "outroLogo" w promo.config.json).
  // Gdy pliku brak, używane jest logo wektorowe z js/logo.js.
  outroLogo: { src: 'assets/logo-outro.png', maxWidth: 640, maxHeight: 300 },

  // Status ośrodka (w aplikacji zimą)
  statusOpen: 'Czynny',

  resorts: {
    kasina: {
      name: 'Kasina Ski',
      city: 'Mszana Dolna', region: 'woj. małopolskie', country: 'Polska',
      logo: 'assets/kasina-logo.png',
      video: 'assets/kasina',            // szuka assets/kasina.webm, potem assets/kasina.mp4
      snow: 75, runs: 4, runsOpen: 4, lifts: 2, liftsOpen: 2,
      distance: '14.2 km',
      stillAt: 2.0,                      // sekunda nagrania użyta jako zdjęcie ośrodka / podgląd kamery
      logoFit: 'cover',                  // logo z własnym tłem wypełnia całe pole
      // nagranie: bezchmurne niebo, oszronione drzewa
      weather: {
        temp: -5, cond: 'Bezchmurnie', icon: 'sun', wind: 6, humidity: 78,
        days: [
          { label: 'Dziś',  hi: -2, lo: -9, precip: 0, icon: 'sun' },
          { label: 'Jutro', hi: -3, lo: -10, precip: 0, icon: 'sun' },
        ],
      },
      cams: [
        { title: 'Kasina Ski - widok na stok i dolną stację kolei', live: true },
      ],
    },
    kotelnica: {
      name: 'Kotelnica Białczańska',
      city: 'Białka Tatrzańska', region: 'woj. małopolskie', country: 'Polska',
      logo: 'assets/kotelnica-logo.png',
      video: 'assets/kotelnica',
      snow: 65, runs: 18, runsOpen: 18, lifts: 11, liftsOpen: 11,
      distance: '61.8 km',
      stillAt: 1.0,                      // start odtwarzania na żywo (sekunda nagrania)
      logoFit: 'cover',
      // nagranie: słońce, niewielkie chmury
      weather: {
        temp: -4, cond: 'Małe zachmurzenie', icon: 'sun', wind: 9, humidity: 70,
        days: [
          { label: 'Dziś',  hi: -2, lo: -10, precip: 0, icon: 'sun' },
          { label: 'Jutro', hi: -3, lo: -11, precip: 10, icon: 'cloud' },
        ],
      },
    },
  },

  // Lista "Ośrodki narciarskie" przed wpisaniem frazy (miniatury ze screenów aplikacji)
  list: [
    { name: 'Baba Korbielów',       loc: 'Korbielów, woj. śląskie',                  flag: 'pl', snow: 60, runs: 2,  img: 'assets/ui/thumb-baba-korbielow.jpg' },
    { name: 'Bachledka Ski & Sun',  loc: 'Ždiar, woj. Słowacja - kraj preszowski',   flag: 'sk', snow: 70, runs: 15, img: 'assets/ui/thumb-bachledka.jpg' },
    { name: 'Bania Ski & Fun',      loc: 'Białka Tatrzańska, woj. małopolskie',      flag: 'pl', snow: 55, runs: 4,  img: 'assets/ui/thumb-bania.jpg' },
    { name: 'Beskid Sport Arena',   loc: 'Szczyrk, woj. śląskie',                    flag: 'pl', snow: 80, runs: 4,  img: 'assets/ui/thumb-beskid.jpg' },
  ],
  listTotal: 113,
  searchQuery: 'Kasina',

  // "Aktualności" — kanał dla narciarzy
  news: [
    { title: 'Nowy sezon w Zieleńcu! Sprawdź warunki na stokach', date: '12 grudnia 2026', img: 'assets/ui/news-1.jpg' },
    { title: 'Jak skutecznie chronić skórę przed słońcem na stoku?', date: '10 grudnia 2026', img: 'assets/ui/news-2.jpg' },
  ],

  // "W liczbach"
  stats: { resorts: 110, open: 96, runs: 619 },

  // Przesuwające się "chipy" z nazwami ośrodków pod telefonem w scenie z kamerą na żywo.
  // Zostaw tylko ośrodki, które faktycznie mają kamery w aplikacji.
  marquee: [
    ['Kasina Ski', 'Czarny Groń - Rzyki', 'Bania Ski & Fun', 'Baba Korbielów', 'Góra Żar Międzybrodzie'],
    ['Kotelnica Białczańska', 'Beskid Sport Arena', 'Bachledka Ski & Sun', 'Zieleniec'],
  ],
};
