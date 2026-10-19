# Landing WebCameraSki: analiza prawdziwości treści

Stan na 19 października 2026. Porównanie obecnej strony
https://www.webcamera.pl/Lp/aplikacja-narty-snowboard-kamery z danymi z:

- API aplikacji (`https://www.webcamera.pl/api/webcameraski_ios_android/data.json.php`, to samo źródło, z którego korzysta aplikacja w wersji 5.0.6),
- App Store (WebCamera.SKI, id1488342079) i Google Play (com.webcamera.webcameraski),
- webcamera.pl.

Liczby można w każdej chwili odświeżyć skryptem `python3 tools/sprawdz-liczby.py`.

## Twierdzenia z obecnej strony

| Twierdzenie | Werdykt | Fakty | Nowa strona |
|---|---|---|---|
| „350 kamer z ośrodków narciarskich w Polsce” (2 razy) | **Nieprawda, zawyżone** | 280 kamer przypisanych do ośrodków, 276 aktywnych. Sklepy piszą „ponad 200”. | „270+ kamer na stokach” |
| „Jedyna aplikacja dla narciarzy” (3 razy) | **Nieprawda** | Na rynku są m.in. iSKI Polska i Skiinfo. iSKI w App Store reklamuje „Live Cameras and Webcams”. | usunięte |
| Opis meta: „Jedyna aplikacja w Polsce z kamerami na żywo w jakości telewizyjnej” | **„Jedyna”: nie do obrony; „jakość TV”: prawda dla większości** | 274 z 280 kamer ma co najmniej 720p, 225 ma Full HD lub więcej. | „Większość nadaje w Full HD” |
| „Ponad 100 ośrodków narciarskich w Polsce” | **Prawda, ale niepełna** | 111 ośrodków: 107 w Polsce i 4 na Słowacji. | „110+ ośrodków w Polsce i na Słowacji” |
| „200 km tras narciarskich” | **Nieaktualne, zaniżone** | 636 tras o łącznej długości 364 km. | „360+ km tras” |
| „Warunki pogodowe, czynne trasy i wyciągi” | **Prawda** | Pogoda bieżąca i prognoza, liczba czynnych tras i wyciągów. | zostaje |
| „Mapki dojazdu do stacji” | **Prawda w innej formie** | Przycisk „Nawiguj (GPS)” otwiera Mapy Google, w aplikacji jest też mapa. | opisane jako „Nawiguj (GPS)” |
| „Trasy dla zaawansowanych i początkujących” | **Prawda** | Trasy mają 4 poziomy trudności. | zostaje w opisie |
| „Koleje linowe, gondolowe i orczyki” | **Prawda** | Orczyki w 89 ośrodkach, koleje krzesełkowe w 68, gondole w 5. | zostaje |
| „Newsy, oferty i wydarzenia” | **Częściowo** | 50 aktualności (najnowsza z 24.09.2026) i 6 promocji. Osobnej sekcji wydarzeń nie ma. | „Aktualności, ski passy” |
| „Aplikacja na Android i iOS” | **Prawda** | App Store: wersja 5.0.6 z 7.10.2026. Google Play: aktualizacja z 6.10.2026. | zostaje, z poprawnymi linkami |
| Wygląd i ekrany aplikacji | **Nieaktualne** | Makiety z 2019 roku (stara wersja aplikacji, iPhone z przyciskiem Home, jasny interfejs). Obecna aplikacja ma ciemny interfejs. | prawdziwe ekrany obecnej wersji |
| Słowacja | **Brak na stronie** | 4 ośrodki na Słowacji. | dodane |

## Opisy w sklepach (do poprawy)

- Oba sklepy podają „ponad 200 widoków live” (aktualnie 280 kamer) i „200 km tras” (aktualnie 364 km).
- Nazwa aplikacji różni się w każdym miejscu: „WebCamera.SKI” (App Store), „WebCamera Ski - Dla narciarzy” (Google Play), „WebCameraSki” (landing i aplikacja).
- Inny wydawca w każdym sklepie: Webcamera Media Sp. z o.o. (App Store) i ZINK SERWIS SP Z O O (Google Play).
- Kategoria: Lifestyle (App Store) i Sport (Google Play).
- Oceny: 3,56 przy 16 ocenach (App Store), 3,6 i ponad 10 tys. pobrań (Google Play). Google Play oznacza aplikację jako „Zawiera reklamy”.

## Błędy w danych aplikacji

- **Bachledka Ski & Sun** ma kraj „Polska”, choć leży w Ždiarze na Słowacji. Dlatego aplikacja pokazuje przy niej polską flagę.
- **20 ośrodków bez żadnej kamery**: Baba Korbielów, Bobliwo, Chyrowa - Ski, Góra Kamieńsk, Jacnia, Jaworki Arena Narciarska Szczawnica, Karpacz Ski Arena, Kolorowa, Niestachów, Pilsko Jontek, Podstolice, Sabat Krajno, Siglany, Skocznia Wielka Krokiew, Stajkowa, Stożek, Trzepowo, Wisła Malinka, Małastów, Zwyrtlik.
- 4 kamery są wyłączone.
- 277 kamer ma flagę `android_premium = 1`, a żadna nie ma `apple_premium`. Warto sprawdzić, czy użytkownicy Androida nie trafiają na płatną ścianę, o której landing nie mówi.
- Pole `buy_url` (zakup karnetu) jest puste we wszystkich ośrodkach. Zapowiadany w 2022 roku zakup karnetów w aplikacji nie działa. Link grupy Tatry Super Ski prowadzi do sklepu „lato”.

## Nasze materiały (filmy) po weryfikacji

Poprawione według API:

- Kasina: miejscowość „Kasina Wielka” (było „Mszana Dolna”), nazwa „Kasina SKI”, liczba kamer 3 (było 1), kamera „KASINA - ski dolna stacja wyciągu”.
- Nazwy: „Master-Ski”, „Kasprowy Wierch - PKL”, „Zieleniec Sport Arena”.
- Z paska ośrodków z kamerami usunięto Babę Korbielów, bo nie ma kamery.
- „W liczbach”: 111 ośrodków, 636 tras.

Wartości przykładowe, które warto znać:

- Pogoda, grubość śniegu i liczba czynnych wyciągów oraz tras pokazują przykładowy dzień zimy. Poza sezonem API ma wszędzie 0.
- „96 czynnych” w sekcji „W liczbach” to wartość przykładowa.
- Hasło „z niemal wszystkich stoków w Polsce” jest ryzykowne: kamery ma 91 ośrodków w aplikacji. Bezpieczniej: „z ponad 90 ośrodków”.
