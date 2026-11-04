# Lingaria: 10 scenariuszy do trybu „Mówienie"

Wszystkie teksty są po polsku (model tłumaczy rozmowę na język nauki przy pierwszym otwarciu). Scenariusze są uniwersalne,
bez pola `jezyki`, więc pojawią się dla każdego języka nauki, zgodnie z regułami rozmów Lingarii (punkt 10 ściągi).

## Pliki
- `scenariusze/{klucz}.json`: pełna rozmowa (dane z formularza „Opis rozmowy" plus `drzewo`).
- `drzewa/{klucz}.drzewo.json`: samo drzewo (`start`, `wezly`, `uklad`), gotowe do wklejenia w polu „JSON drzewa" (Zaawansowane, potem JSON, potem „Zastosuj JSON na kanwie").
- `narzedzia/waliduj.py`: walidator reguł ze ściągi (`python3 waliduj.py plik.json`; dla samego drzewa dodaj `--lingaria`).
- `narzedzia/generuj_scenariusze.py`: źródło, z którego wygenerowano pliki (krótki zapis pomaga przy poprawkach).

## Scenariusze
| Klucz | Tytuł | CEFR | Głos | Klocki | Odpowiedzi (widoczne+ukryte) | Miejsca `{...}` |
|---|---|---|---|---|---|---|
| `lingaria_droga_do_dworca_a1` | Jak dojść do dworca? | A1 | kobiecy | 17 | 5+1 | - |
| `lingaria_hotel_zameldowanie_a2` | Zameldowanie w hotelu | A2 | kobiecy | 20 | 9+1 | nazwisko |
| `lingaria_kawiarnia_a1` | Kawa i ciasto w kawiarni | A1 | kobiecy | 17 | 11+1 | imie |
| `lingaria_lekarz_bol_gardla_b1` | U lekarza: ból gardła | B1 | kobiecy | 18 | 9+1 | - |
| `lingaria_lotnisko_odprawa_a2` | Odprawa na lotnisku | A2 | męski | 17 | 8+1 | miasto |
| `lingaria_pociag_bilet_a2` | Bilet na pociąg | A2 | kobiecy | 17 | 9+1 | miasto |
| `lingaria_poznajemy_sie_a1` | Poznajemy się na przyjęciu | A1 | męski | 14 | 7+1 | imie, miasto |
| `lingaria_restauracja_kolacja_a2` | Kolacja w restauracji | A2 | męski | 18 | 9+2 | danie |
| `lingaria_rozmowa_o_prace_b1` | Rozmowa o pracę | B1 | męski | 18 | 9+1 | zawod |
| `lingaria_wynajem_mieszkania_b2` | Wynajem mieszkania | B2 | męski | 17 | 6+1 | - |

Każdy scenariusz ma wszystkie klocki palety (opis, pytanie, kwestia, uczeń, na pamięć, swobodna, opis w języku ucznia i dwa końce),
co najmniej jedną gałąź ukrytą i `uklad` z położeniem klocków na kanwie.

## Ustalenia, które warto zatwierdzić
- `status` jest ustawiony na `szkic`, żeby nic nie trafiło na żywo przed Twoim przeglądem. Zmień na `gotowy`.
- Brak pola `kolejnosc`, więc zostaje taka, jaka jest w bazie.
- Płeć bota jest zgodna z głosem (`auto:feminine` albo `auto:masculine`), a wypowiedzi ucznia nie mają form zależnych od płci.
- Bot zwraca się do ucznia na „ty" również w hotelu, na lotnisku i u lekarza, bo uczeń może być kobietą lub mężczyzną, a forma „Pan/Pani" zależy od płci.

## Co sprawdzono, a czego nie
- Walidator to moja reimplementacja reguł ze ściągi (punkty 3 do 10). Przepuszcza przykład z punktu 11 i wykrywa wstrzyknięte usterki (martwe `dalej`, pauzę, strzałkę, więcej niż 4 gałęzie, miejsce bez wzoru, za długi tekst, jeden koniec, ucznia mówiącego dwa razy, swobodną bez zwykłej kwestii bota przed nią).
- Nie uruchamiałem kodu PHP Lingarii. Przed zapisem warto puścić `php scripts/mowienie_lingaria_rozmowy.php` na sucho.
- Polszczyzna i naturalność kwestii wymagają Twojego przeglądu, szczególnie wskazówki w klockach „w języku ucznia".
