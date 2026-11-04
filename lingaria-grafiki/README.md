# Lingaria – grafiki do wgrywania ręcznie

Zdjęcia-plansze ze słówkami (styl: zdjęcia odręcznych notatek, kartek, tablic).
Wgrywasz je w Lingarii z konta w języku ucznia; aplikacja sama odczytuje słówka i tłumaczy.

## Nazwy plików
`{KONTO}_NA_{SŁOWA}_{temat}[_fonetyka].jpg`
- Czytaj od lewej: logujesz się na koncie w pierwszym języku i wgrywasz słowa w drugim.
- `HISZPANSKI_NA_NIEMIECKI_owoce.jpg` = konto hiszpańskie, wgrywasz niemieckie słowa.
- `_fonetyka` = nad każdym słowem jest wymowa zapisana „po uczniowsku" (pisownia języka ucznia).

## Foldery
- `probne/` – 13 obrazów próbnych (po ręcznej kontroli).
- `seria-50/` – 50 obrazów: po 2 na każdy z 25 języków (tablica tematyczna + przeciwieństwa), 5–35 słówek na obraz,
  osiem języków w innym alfabecie ma nad słowem fonetykę w pisowni języka konta. Zestawienie: `manifest-seria-50.csv`.
- `prompty/` – dokładne prompty użyte do generowania (model: gemini-3-pro-image, rozmiar 2K).

## Kontrola jakości
Każdy obraz z serii przeszedł automatyczną kontrolę: drugi model odczytał cały widoczny tekst i porównał go z listą
słów (braki, powtórzenia, obce napisy); przy błędzie obraz generowano od nowa (do 3 prób). Dodatkowo część obrazów
obejrzano ręcznie. Fonetyka i tłumaczenia to wersje robocze – warto je dać do rzutu oka osobie znającej język.
