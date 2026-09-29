# WebCameraSki — App Preview (20 s, HTML/CSS/JS)

Krótki film do App Store (App Preview) pokazujący, jak działa aplikacja **WebCameraSki**:
kamery na żywo z niemal wszystkich stoków w Polsce, aktualne warunki, pogoda na stoku i kanał dla narciarzy.
Całość to animacja HTML/CSS/JS, renderowana klatka po klatce do MP4.

- **Rozdzielczość:** 886 × 1920 (App Preview iPhone 6.5" / 6.7" / 6.9")
- **Klatki:** 30 fps, dokładnie 20,0 s (Apple: min. 15 s, maks. 30 s)
- **Plik:** H.264 High 4.0, yuv420p, AAC 256 kb/s stereo 48 kHz, `+faststart`

## Scenariusz

| Czas | Scena | Hasło |
|---|---|---|
| 0 – 3,4 s | Start → wyszukiwarka, wpisywanie „Kasina” | **Znajdź swój stok** — ponad 100 ośrodków w jednej aplikacji |
| 3,4 – 6,8 s | Kasina Ski: 75 cm, 4/4 trasy, 2/2 wyciągi, pogoda, zakładka „Kamery” | **Warunki na żywo** — śnieg, trasy i wyciągi |
| 6,8 – 10,3 s | tap ▶ → telefon obraca się do poziomu, kamera NA ŻYWO, przesunięcie na Kotelnicę | **Kamery na żywo** — z niemal wszystkich stoków w Polsce |
| 10,3 – 14,3 s | Kotelnica Białczańska: 65 cm, 18/18 tras, 11/11 wyciągów, prognoza | **Pogoda na stoku** — prognoza i kamery pogodowe |
| 14,3 – 17,3 s | Start: Aktualności + „W liczbach” | **Kanał dla narciarzy** — aktualności prosto ze stoków |
| 17,3 – 20 s | logo, „Zawsze bliżej gór”, fade out | |

Wszystkie przejścia i ruchy kamery używają krzywych *Easy Ease* (jak w After Effects).

## Szybki start (Windows)

1. Zainstaluj **Node.js LTS** (https://nodejs.org) i miej zainstalowanego **Chrome** albo **Edge**.
2. W tym folderze:

   ```bash
   npm install
   npm run assets     # nagrania + logo ze ścieżek w promo.config.json -> assets/
   ```

   `promo.config.json` wskazuje już Twoje pliki:
   - `C:\Users\Alek\Desktop\nowy_layout\preview\WEBC1_2024-12-26-11-50.h265.mp4` → Kasina Ski
   - `C:\Users\Alek\Desktop\nowy_layout\elementy\tlo-kotelnica-bialczanska.mp4` → Kotelnica Białczańska
   - `...\preview\20.png` i `...\preview\resortlogo-21.png` → logo ośrodków

   Skrypt przerabia wideo (także H.265/HEVC) na VP9 `.webm`, które odtworzy każda przeglądarka.
   Pole `start` pozwala wybrać, od której sekundy nagrania zacząć.

3. **Podgląd:** otwórz `index.html` w Chrome/Edge.
   Spacja — start/pauza, ← → — klatka, Shift+← → — sekunda, R — od początku, H — ukryj panel.
   Adres z `?t=8.5&pause` otwiera konkretną chwilę.

4. **Render do MP4:**

   ```bash
   npm run render          # -> out/webcameraski-app-preview.mp4  (~4 min)
   npm run draft           # szybki podgląd 15 fps
   npm run stills          # kilka klatek PNG do out/
   ```

   Z muzyką: zapisz ścieżkę jako `assets/audio.mp3` (lub `.wav`) albo `npm run render -- --audio C:\muzyka.mp3`.
   Prompty do Suno / ElevenLabs i znaczniki czasu: **[AUDIO.md](AUDIO.md)**.

## Co zmieniono względem screenów

- Pasek statusu: **9:41, bateria 100%**, bez trybu oszczędzania.
- **Usunięte reklamy** (banery AdMob) ze wszystkich ekranów.
- Dane **zimowe**: Kasina Ski — 75 cm, trasy 4/4, wyciągi 2/2; Kotelnica Białczańska — 65 cm, trasy 18/18, wyciągi 11/11;
  status „Czynny” zamiast „Sezon zamknięty”, ujemne temperatury, zimowe tytuły aktualności.
- Kolory, ikony (Material Icons — te same co w aplikacji), układ i odstępy skalibrowane nakładką 1:1 na Twoje screeny.
- Logo WebCameraSki zwektoryzowane ze screena (`js/logo.js`) — jeśli masz oficjalny SVG, podmień `LOGO_SVG`.
- Font: **Inter** (dołączony, najbliższy odpowiednik SF Pro z iOS), rozmiary dopasowane do screenów —
  dzięki temu render wygląda tak samo na każdym komputerze.

## Do sprawdzenia przed publikacją

Wszystko jest w `js/data.js`:

- **Pogoda** (temperatury, opis, ikony) — dopasuj do tego, co widać na nagraniach (np. jeśli pada śnieg: `icon: 'snow'`).
- `stillAt` — sekunda nagrania, z której powstaje zdjęcie ośrodka/podgląd kamery i od której startuje „na żywo”.
- Nazwa kamery Kasiny i liczba kamer, odległości „Blisko Ciebie”, daty aktualności, liczba „czynnych” w „W liczbach” (96).
- `marquee` — nazwy ośrodków przesuwające się pod telefonem; zostaw tylko te, które mają kamery w aplikacji.

Czasy scen i ruchy kamery: obiekt `T` i tablica `CAM` w `js/promo.js`.

## Wytyczne Apple

Wytyczna 2.3.4 mówi, że App Preview ma pokazywać głównie nagranie ekranu aplikacji. Wersja z ramką telefonu
i ruchem kamery świetnie sprawdzi się w reklamach i social media, ale w App Store może zostać odrzucona —
wtedy warto przygotować wariant bez ramki (ekran aplikacji na pełnym kadrze + te same hasła).

## Struktura

```
index.html            scena 886×1920
css/promo.css         paleta i typografia aplikacji
js/data.js            teksty i dane (edytuj tutaj)
js/screens.js         ekrany aplikacji (Start, Ośrodki, szczegóły, kamera na żywo, Aktualności)
js/promo.js           oś czasu, kamera, pisanie tekstu, przejścia, synchronizacja wideo
js/icons.js, logo.js  ikony Material i logo
assets/ui/            fragmenty Twoich screenów (hero, miniatury, zdjęcia aktualności)
render/               przygotowanie zasobów i render do MP4 (Playwright + ffmpeg)
```
