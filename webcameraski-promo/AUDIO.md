# Audio do App Preview — prompty i znaczniki czasu

Film ma dokładnie **20,0 s**. Gotową ścieżkę zapisz jako `assets/audio.mp3` (albo `.wav`/`.m4a`) —
`npm run render` sam ją doda, przytnie do 20 s i wyciszy w ostatnich 1,2 s.
Bez pliku audio render dodaje cichą ścieżkę stereo (App Store wymaga ścieżki audio).

> Uwaga: w App Store podgląd startuje **bez dźwięku** — muzyka to dodatek, cały przekaz niesie obraz.

---

## 1. Muzyka — Suno

**Style of Music** (wklej w pole stylu):

```
uplifting winter electronic pop, 120 BPM, bright plucks, airy synth pads, soft sub bass, crisp claps, icy shimmer, build-up then drop, modern app commercial, instrumental
```

**Lyrics:** `[Instrumental]`

**Tytuł (opcjonalnie):** `Zawsze bliżej gór`

Wskazówki:
- Suno generuje dłuższe utwory — wytnij 20 s tak, żeby **drop (wejście bitu)** wypadł na **7,65 s**
  (moment, gdy telefon kończy obrót do poziomu i startuje kamera na żywo).
- 120 BPM = 1 takt co 2 s, więc cięcia scen (3,4 / 6,8 / 10,3 / 14,3 / 17,3 s) wypadają blisko taktów.
- Wersja spokojniejsza: zamień początek promptu na `cinematic ambient electronic, 100 BPM, warm piano, soft snow textures, gentle build`.

## 2. Muzyka — ElevenLabs (Eleven Music) — z podziałem na sekcje

Prompt:

```
20-second instrumental for a mobile app commercial about live ski-slope webcams in Polish mountains. Crisp, bright, wintry, premium. 120 BPM.
0:00-0:03 intro: airy pads, icy shimmer, soft plucks.
0:03-0:07 build: add claps and rising filtered synth, riser into the drop.
0:07.6 drop: full beat, warm sub bass, bright lead pluck hook.
0:10-0:17 groove continues, slightly lighter, positive and confident.
0:17-0:20 outro: beat stops, sparkling shimmer and one clean final chord that rings out.
No vocals.
```

## 3. Efekty dźwiękowe — ElevenLabs (Sound Effects)

Wygeneruj każdy osobno (długość w nawiasie) i ułóż w montażu wg tabeli niżej.

| # | Prompt (EN — działa najlepiej) | Długość |
|---|---|---|
| A | `soft iPhone screen tap, subtle glassy click, clean, close mic` | 0.3 s |
| B | `iOS keyboard typing, 6 soft quick key clicks, clean, no room` | 0.8 s |
| C | `soft UI swoosh, quick screen slide transition, airy, subtle` | 0.5 s |
| D | `smooth cinematic whoosh with rising shimmer, phone rotating, premium commercial` | 1.0 s |
| E | `fast horizontal swipe whoosh, light and clean` | 0.5 s |
| F | `reverse whoosh settling down, soft landing` | 0.9 s |
| G | `tiny digital counter ticks speeding up, subtle, UI` | 0.9 s |
| H | `magical icy sparkle chime, logo reveal, bright and short` | 1.5 s |
| I | `gentle wind over snowy mountain, soft ambience, loopable` | 20 s |

### Znaczniki czasu (cue sheet)

| Czas [s] | Co się dzieje w filmie | Dźwięk |
|---|---|---|
| 0.00 | fade in, telefon wjeżdża | I (wiatr, cicho, cały film) + start muzyki |
| 0.35 | pisanie hasła „Znajdź swój stok” | B (bardzo cicho) |
| 1.15 | tap w wyszukiwarkę | A |
| 1.30 | przejście do listy ośrodków | C |
| 1.95 – 2.60 | wpisywanie „Kasina” (6 znaków co 0,11 s) | B |
| 2.85 | tap w „Kasina Ski” | A |
| 3.00 | przejście do ośrodka | C |
| 3.65 | liczniki: 75 cm / 4 trasy / 2 wyciągi | G |
| 5.72 | tap „Kamery” | A |
| 6.64 | tap „▶” (kamera na żywo) | A |
| 6.78 – 7.65 | obrót telefonu do poziomu, wideo na pełny ekran | D → **drop muzyki na 7.65** |
| 8.85 – 9.40 | przesunięcie na kamerę Kotelnicy | E |
| 10.30 – 11.15 | powrót do pionu, „Pogoda na stoku” | F |
| 10.95 | liczniki: 65 cm / 18 tras / 11 wyciągów | G |
| 14.28 | tap „Start” | A |
| 14.38 | przejście do „Aktualności” | C |
| 15.35 | liczniki „W liczbach” (110 / 96 / 619) | G |
| 17.25 – 18.25 | telefon odjeżdża w dół | C (dłuższy, cichszy) |
| 18.30 | logo + czerwona kreska | H |
| 19.45 – 20.00 | fade out | wyciszenie |

## 4. Lektor (opcjonalnie) — ElevenLabs, język polski

Głos: ciepły, energiczny, naturalny (np. męski/żeński „narrator”, stability ~40%, style ~30%).

| Start [s] | Tekst |
|---|---|
| 0.40 | Znajdź swój stok. |
| 3.50 | Sprawdź warunki na żywo. |
| 7.10 | Kamery na żywo z niemal wszystkich stoków w Polsce. |
| 10.80 | Pogoda na stoku… |
| 14.60 | …i kanał dla narciarzy. |
| 18.40 | WebCameraSki. Zawsze bliżej gór. |

Zmiksuj: muzyka −14 LUFS, lektor ok. 6 dB nad muzyką, efekty cicho (−6…−10 dB pod lektorem).
Eksportuj jeden plik stereo 48 kHz → `assets/audio.wav` → `npm run render`.
