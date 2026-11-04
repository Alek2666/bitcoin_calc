# Lingaria: 30 scenariuszy do trybu „Mówienie"

Wszystkie teksty są po polsku (model tłumaczy rozmowę na język nauki przy pierwszym otwarciu). Scenariusze są uniwersalne,
bez pola `jezyki`, więc pojawią się dla każdego języka nauki, zgodnie z regułami rozmów Lingarii (punkt 10 ściągi).

- Seria 1 (10 scenariuszy): zawiera miejsca na własną odpowiedź `{imie}`, `{miasto}` itp. (kolumna „Zmienne" = tak).
- Seria 2 (20 scenariuszy): bez żadnych zmiennych w zdaniach, wszystkie zdania ucznia są stałe.

## Pliki
- `scenariusze/{klucz}.json`: pełna rozmowa (dane z formularza „Opis rozmowy" plus `drzewo`).
- `drzewa/{klucz}.drzewo.json`: samo drzewo (`start`, `wezly`, `uklad`) do wklejenia w polu „JSON drzewa" (Zaawansowane, potem JSON, potem „Zastosuj JSON na kanwie").
- `narzedzia/`: `waliduj.py` (walidator reguł ze ściągi), `zbuduj.py` (buduje i sprawdza paczkę scenariuszy, w tym brak zmiennych i rodzaj bota), `sciezki.py` (wypisuje rozmowy ścieżka po ścieżce do czytania), `dsl.py` (skrót do pisania drzew), `zrodla/` (źródła w Pythonie, z których wygenerowano pliki).

## Scenariusze
| Poziom | Klucz | Tytuł | Głos | Klocki | Odpowiedzi (widoczne+ukryte) | Zmienne |
|---|---|---|---|---|---|---|
| A1 | `lingaria_autobus_miejski_a1` | Autobus miejski | kobiecy | 17 | 6+1 | nie |
| A1 | `lingaria_droga_do_dworca_a1` | Jak dojść do dworca? | kobiecy | 17 | 5+1 | nie |
| A1 | `lingaria_kawiarnia_a1` | Kawa i ciasto w kawiarni | kobiecy | 17 | 11+1 | tak |
| A1 | `lingaria_kino_bilety_a1` | Bilety do kina | męski | 15 | 12+1 | nie |
| A1 | `lingaria_nowy_sasiad_a1` | Spotkanie z sąsiadką na klatce schodowej | kobiecy | 20 | 6+1 | nie |
| A1 | `lingaria_poznajemy_sie_a1` | Poznajemy się na przyjęciu | męski | 14 | 7+1 | tak |
| A1 | `lingaria_rodzina_zdjecie_a1` | Rodzina na zdjęciu | męski | 18 | 11+4 | nie |
| A1 | `lingaria_supermarket_a1` | Zakupy w supermarkecie | kobiecy | 20 | 8+1 | nie |
| A1 | `lingaria_taksowka_a1` | Taksówką do hotelu | męski | 20 | 6+1 | nie |
| A2 | `lingaria_apteka_lek_a2` | W aptece | kobiecy | 17 | 10+3 | nie |
| A2 | `lingaria_biblioteka_karta_a2` | Karta w bibliotece | kobiecy | 17 | 8+2 | nie |
| A2 | `lingaria_fryzjer_a2` | U fryzjera | męski | 19 | 10+2 | nie |
| A2 | `lingaria_hotel_zameldowanie_a2` | Zameldowanie w hotelu | kobiecy | 20 | 9+1 | tak |
| A2 | `lingaria_kurs_jezykowy_a2` | Zapis na kurs językowy | męski | 18 | 13+1 | nie |
| A2 | `lingaria_lotnisko_odprawa_a2` | Odprawa na lotnisku | męski | 17 | 8+1 | tak |
| A2 | `lingaria_pociag_bilet_a2` | Bilet na pociąg | kobiecy | 17 | 9+1 | tak |
| A2 | `lingaria_poczta_paczka_a2` | Wysyłamy paczkę | kobiecy | 19 | 8+2 | nie |
| A2 | `lingaria_prezent_urodzinowy_a2` | Prezent na urodziny | kobiecy | 17 | 9+3 | nie |
| A2 | `lingaria_przymierzalnia_a2` | Ubrania w przymierzalni | męski | 18 | 8+1 | nie |
| A2 | `lingaria_restauracja_kolacja_a2` | Kolacja w restauracji | męski | 18 | 9+2 | tak |
| A2 | `lingaria_rezerwacja_stolika_a2` | Rezerwacja stolika przez telefon | kobiecy | 20 | 10+2 | nie |
| B1 | `lingaria_bank_konto_b1` | Zakładanie konta w banku | kobiecy | 20 | 10+2 | nie |
| B1 | `lingaria_lekarz_bol_gardla_b1` | U lekarza: ból gardła | kobiecy | 18 | 9+1 | nie |
| B1 | `lingaria_rozmowa_o_prace_b1` | Rozmowa o pracę | męski | 18 | 9+1 | tak |
| B1 | `lingaria_silownia_karnet_b1` | Karnet na siłownię | kobiecy | 19 | 9+1 | nie |
| B1 | `lingaria_wypozyczalnia_auta_b1` | Wynajem samochodu | męski | 19 | 9+1 | nie |
| B1 | `lingaria_zgubiona_torba_b1` | Zgubiona torba | męski | 16 | 9+1 | nie |
| B2 | `lingaria_biuro_podrozy_b2` | Planowanie wycieczki w biurze podróży | męski | 19 | 15+1 | nie |
| B2 | `lingaria_reklamacja_sluchawki_b2` | Reklamacja słuchawek | kobiecy | 20 | 11+2 | nie |
| B2 | `lingaria_wynajem_mieszkania_b2` | Wynajem mieszkania | męski | 17 | 6+1 | nie |

Każdy scenariusz ma wszystkie klocki palety (opis, pytanie, kwestia, uczeń, na pamięć, swobodna i dwa końce), co najmniej jedną gałąź ukrytą oraz `uklad` z położeniem klocków na kanwie.

## Ustalenia, które warto zatwierdzić
- `status` jest ustawiony na `szkic`, żeby nic nie trafiło na żywo przed przeglądem. Zmień na `gotowy`.
- Brak pola `kolejnosc`, więc zostaje taka, jaka jest w bazie.
- Płeć bota jest zgodna z głosem (`auto:feminine` albo `auto:masculine`), a wypowiedzi ucznia nie mają form zależnych od płci.
- Bot zwraca się do ucznia na „ty" lub bezosobowo (nigdy „Pan/Pani"), bo uczeń może być kobietą lub mężczyzną.
- Kwoty podawane są w euro, a ceny są wymyślone. W serii 2 większość scenariuszy w ogóle nie podaje cen.

## Co sprawdzono, a czego nie
- Walidator to moja reimplementacja reguł ze ściągi (punkty 3 do 10), sprawdzona na Waszym przykładzie z punktu 11 i na celowo zepsutych drzewach. Nie uruchamiałem kodu PHP Lingarii.
- Seria 2 przeszła dodatkowo niezależną recenzję polszczyzny i spójności ścieżek (każdy scenariusz czytano ścieżka po ścieżce) i zbiorcze kontrole: brak zmiennych, pauz i strzałek, uczeń nie mówi dwa razy z rzędu, przed odpowiedzią swobodną stoi zwykła kwestia bota.
- Recenzje wykonał model, nie native speaker języka polskiego. Przejrzyjcie sami, szczególnie tony kwestii i wskazówki w klockach „w języku ucznia".
- Przed zapisem warto puścić `php scripts/mowienie_lingaria_rozmowy.php` na sucho.
