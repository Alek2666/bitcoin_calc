# Landing WebCameraSki (nowa wersja)

Odświeżona strona https://www.webcamera.pl/Lp/aplikacja-narty-snowboard-kamery.
Jasny motyw, prawdziwe ekrany obecnej aplikacji i zweryfikowane liczby (październik 2026).

## Pliki

```
index.html            cała strona (bez zależności zewnętrznych, bez frameworków)
css/landing.css       style
js/landing.js         pisany nagłówek, przełącznik kamer, film, animacje (ok. 3 KB)
fonts/                Inter (licencja OFL w Inter-LICENSE.txt)
img/                  ekrany aplikacji, logotypy, plakaty
media/                pętle z kamer i film reklamowy (ładowane dopiero po przewinięciu)
tools/sprawdz-liczby.py   liczby z API aplikacji, uruchom przed każdym sezonem
ANALIZA-PRAWDY.md     porównanie starej strony z faktami
```

## Waga strony

Na start ładuje się około 0,5 MB: HTML, CSS, JS, font, logo, ekrany telefonu i kadr z kamery.
Filmy i ich plakaty pobierają się dopiero, gdy użytkownik przewinie do danej sekcji.

## Wdrożenie

Folder można wgrać w całości pod `/Lp/aplikacja-narty-snowboard-kamery/`. Wszystkie ścieżki są względne.

## Do aktualizacji co sezon

1. `python3 tools/sprawdz-liczby.py`
2. Popraw liczby w `index.html`: sekcja `LICZBY`, opis meta, JSON-LD, sekcje Kamery, Ośrodki i FAQ.
3. Popraw datę w zdaniu „Dane z aplikacji WebCameraSki, ...”.

Logo: oryginalne kolory (`img/wcs-logo-full.png`, `img/webcamera-pl-logo.svg`) albo wersja biała, bez innych przeróbek.
W treściach nie używamy półpauz ani pauz (–, —).
