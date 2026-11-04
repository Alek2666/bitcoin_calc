# DODATKI DO TEJ PACZKI (obowiązują razem z przewodnikiem poniżej)

- Dzisiejsza data to 2026-11-04: wpisz ją w `data` i `zaktualizowano`.
- Istniejące artykuły serwisu (nie dubluj tematów): jak-dziala-lingaria-fiszki-z-piosenek-filmow-i-twoich-notatek, nauka-angielskiego-z-piosenek, powtorki-rozlozone-w-czasie, wloska-wymowa-pulapki, wloski-w-kawiarni, wloski-w-restauracji, wloskie-rodzajniki.
- SŁOWA-KLUCZE SKŁADNI zostają ZAWSZE takie, jak w przewodniku, także w artykule pisanym w innym języku: nazwy bloków (`:frazy`, `:koniec`, `:uwaga`, `:cta`, `:cwiczenie`, `:::fiszki`, `:::quiz`, `:::sluchanie`, `:::smart-czytanie`, `:::modal-trigger`), etykiety `wymowa:`, `Pytanie:`, `Wyjaśnienie:` i znacznik `[correct]`, a także klucze nagłówka (`tytul`, `opis`, `dzial`...). Tłumaczysz tylko treść: zwroty, objaśnienia, tytuły sekcji, pytania i odpowiedzi.
- NOWA ZASADA JĘZYKOWA tej paczki: prawie wszystkie artykuły NIE są po polsku. Piszesz w `jezyk_tekstu` podanym w temacie (język czytelnika), a uczysz `jezyk_docelowy`. Tytuł, opis, nagłówki, objaśnienia, notki, tłumaczenia, pytania i odpowiedzi quizu, treść `:uwaga` i wszystko inne poza zwrotami w języku docelowym piszesz po natywnemu w języku czytelnika, nie jako przekład z polskiego. Zapis wymowy: w pisowni języka czytelnika; akcent wielkimi literami tylko tam, gdzie język docelowy ma akcent wyrazowy (dla japońskiego i koreańskiego pisz bez wielkich liter).
- Pole `tresc` w liście tematów to krótki opis po angielsku, co ma być w artykule. To tylko wskazówka co do zakresu, tytuł i frazę z Google wymyśl i napisz natywnie w języku czytelnika.
- Nie używaj bloku `:::film` (nie ma jak sprawdzić identyfikatora).
- FAKTY: wpisuj tylko to, czego jesteś pewien. Ceny, liczby, zwyczaje i szczegóły językowe sprawdzaj w WebSearch albo WebFetch (jeśli narzędzia nie są załadowane, wczytaj je przez ToolSearch). Nie masz pewności: usuń fakt albo napisz ogólniej. Nie wymyślaj kwot ani przepisów. Prawdziwy szczegół jest cenny, zmyślony szkodzi.
- Pisz jak człowiek, nie jak model: obowiązują zasady z punktu 4 przewodnika oraz z pliku /root/.claude/plugins/synced/889de98e-bb01-413f-a209-f51ff4b2058e_532fd002-07ef-475f-9a5d-b76cc423418c/8522bbee-a491-445e-9400-615770e76ef5/SKILL.md (humanizer; stosuj jego wzorce do języka, w którym piszesz). W praktyce: zero morałów na końcu sekcji, zero „nie tylko X, ale Y", zero sztucznych trójek, zero patosu i języka reklamy, zero pauz.
- Każdy artykuł o konkretnym języku ma blok `:frazy` (8 do 12 zwrotów, każdy z notką w czwartej kolumnie) ALBO `:::fiszki`, do tego `:::quiz` z trzema pytaniami, `:uwaga` (1 lub 2 razy), dokładnie jedno `:cta` mniej więcej w połowie tekstu, a przy `:frazy` najwyżej jedno `:cwiczenie fiszki`. Artykuł o metodzie (bez języka docelowego) nie ma `:frazy` ani `:::fiszki`; może mieć quiz, `:uwaga` i `:cta`.
- DŁUGOŚĆ jest różna dla różnych artykułów: każdy temat ma w liście orientacyjny cel `slowa_cel` (od ok. 650 do ok. 1600 słów). Trzymaj się go z grubsza, dokładna liczba nie jest potrzebna (ani słów, ani znaków). Krótszy tekst ma być zwarty i konkretny, dłuższy ma mieć więcej treści, nie waty. Nie rozciągaj i nie przycinaj na siłę. Jedyny twardy próg to 600 słów.
- Zrób z każdego artykułu osobny plik `{slug}.txt` w katalogu podanym w zadaniu. Slug dostajesz w liście tematów. Wypełnij `powiazane` slugami podanymi w liście tematów.

# Lingaria: jak pisać artykuły (kontekst dla autora)

Ten plik opisuje WSZYSTKO, czego potrzebujesz, żeby napisać artykuły do serwisu Lingaria (lingaria.com). Przeczytaj go w całości przed pierwszym tekstem. Każda reguła poniżej ma powód. Gdy reguła wydaje się dziwna, to zwykle dlatego, że łamanie jej kiedyś coś zepsuło.

## 1. Czym jest Lingaria i po co te artykuły

Lingaria to serwis i aplikacja do nauki słówek: fiszki z powtórkami rozłożonymi w czasie, mini quizy, Czytanie (teksty z tłumaczeniem zdanie po zdaniu), Słuchanie (filmy z YouTube z napisami i quizami), Mówienie (rozmowy z postacią, ocena wypowiedzi), zdjęcia notatek zamieniane na fiszki i Społeczność (gotowe zestawy innych uczniów). Interfejs ma 25 języków, a najwięcej użytkowników jest z Polski.

Artykuły leżą pod adresem `https://lingaria.com/article/{slug}` i są jedyną treścią serwisu, którą można przeczytać BEZ zakładania konta. Dla Google reszta serwisu prawie nie istnieje. Wcześniej Google AdSense odrzucił serwis z powodem „treść o niskiej wartości". Artykuły mają to odwrócić i przyciągać ludzi z wyszukiwarki.

Z tego wynika najważniejsza zasada: artykuł, który mógłby stać w stu innych serwisach, jest bezwartościowy. Ratuje go konkret, którego nie ma w rozmówkach: wymowa przy każdym zwrocie, notka „kiedy tak się mówi" i szczegóły, o których nikt inny nie pisze (np. włoskie coperto, czyli opłata za nakrycie 1,50-3 euro od osoby; convalidare il biglietto, czyli skasowanie biletu, za którego brak jest mandat; un etto = 10 dag). Tekst bez takich szczegółów nie jest wart publikacji, nawet jeśli ma dobrą gramatykę i 1500 słów.

Sprawdź istniejące teksty na `https://lingaria.com/article/` i nie dubluj ich tematów.

## 2. Co oddajesz: jeden artykuł = jeden plik .txt

- Kodowanie UTF-8 bez BOM.
- Nazwa pliku = adres artykułu (slug) + `.txt`. Slug: tylko małe litery a-z, cyfry i łącznik „-", zaczyna się literą albo cyfrą, najwyżej 81 znaków, bez polskich liter. Przykład: `hiszpanski-w-restauracji.txt` daje adres `/article/hiszpanski-w-restauracji`.
- Plik ma nagłówek, linię `---` i treść.

### Nagłówek (wszystko przed `---`)

```
tytul: Konkretna obietnica, a nie „Poradnik o X" (trafia do <title> i do wyników Google)
opis: Jedno zdanie do wyników wyszukiwania, najwyżej 175 znaków (dłuższe Google utnie)
data: RRRR-MM-DD
zaktualizowano: RRRR-MM-DD
status: szkic
dzial: praktyka
poziom: A1-A2
autor:
tagi: hiszpański, restauracja, zwroty
powiazane: slug-innego-artykulu, slug-drugiego
jezyk_docelowy: es
jezyk_tekstu: pl
---
```

Zasady pól:

- `status: szkic` ZAWSZE. Publikuje człowiek po przeczytaniu.
- `autor:` ZAWSZE puste. Podpisuje człowiek, który tekst przeczytał. Podpis ma być prawdziwy.
- `data` i `zaktualizowano`: wpisz dzisiejszą datę. Termin publikacji ustali redakcja.
- `dzial`: dokładnie jedno z trzech:
  - `praktyka` (W praktyce): gotowe zwroty na konkretne sytuacje, z wymową i uwagą, kiedy tak się mówi;
  - `gramatyka` (Gramatyka bez wkuwania): reguły wyjaśnione tak, żeby dało się ich użyć;
  - `metoda` (Jak się uczyć): co naprawdę działa w nauce słówek i ile to zajmuje. Nigdy `wloski` (to dział tylko dla starych tekstów, zapis go odrzuci).
- `jezyk_docelowy`: kod języka, którego artykuł UCZY. Puste = tekst uniwersalny (np. o metodzie nauki), widoczny dla wszystkich. Z kodem tekst widzą tylko uczący się tego języka, więc temat musi być dla nich.
- `jezyk_tekstu`: kod języka, w którym artykuł jest NAPISANY (objaśnienia, tłumaczenia). Domyślnie `pl`. Tekst po szwedzku o chorwackim to `jezyk_docelowy: hr` i `jezyk_tekstu: sv`, nigdy odwrotnie. Pomylone pola każą wyciągać słówka w złym języku i uczeń dostaje do talii nie te słowa.
- `powiazane`: slugi istniejących artykułów (albo innych plików z tej samej paczki), po przecinku. Nie wskazuj artykułu samego na siebie. Puste = strona dobierze trzy teksty sama.
- `poziom`: A1, A2, B1, B2, C1 albo zakres („A1-A2").

Kody języków (25): `pl` polski, `en` angielski, `de` niemiecki, `es` hiszpański, `it` włoski, `fr` francuski, `pt` portugalski, `nl` niderlandzki, `sv` szwedzki, `no` norweski, `da` duński, `fi` fiński, `cs` czeski, `sk` słowacki, `hr` chorwacki, `ro` rumuński, `el` grecki, `tr` turecki, `ru` rosyjski, `uk` ukraiński, `ar` arabski, `hi` hindi, `ja` japoński, `ko` koreański, `zh` chiński.

Nie generuj obrazów. Zdjęcie główne dobiera redakcja. Jeśli masz pomysł na zdjęcie, dopisz w nagłówku linię `zdjecie_pomysl: …` (parser ją pominie, redakcja ją przeczyta).

### Długość

- Poniżej 600 słów tekst nie wejdzie do wyszukiwarki (dostaje noindex). To twardy próg.
- Cel: różnie, zależnie od tematu (patrz `slowa_cel` w liście tematów); dokładna liczba nie jest wymagana. Liczą się słowa treści. Znaczniki bloków i znaki składni się nie liczą.

## 3. Składnia treści

Parser rozumie DOKŁADNIE to, co poniżej, i nic więcej:

- `## Nagłówek` i `### Podnagłówek` (`##` wchodzi do spisu treści),
- listy `- punkt` i `1. punkt`,
- cytat `> tekst`,
- `**pogrubienie**`, `*kursywa*`, ``kod``, `[napis](https://adres)`,
- bloki opisane niżej.

HTML wpisany w treść NIE zadziała, pokaże się jako tekst.

Pogrubienie nie może mieć w środku kursywy. `**wybór między *il* a *lo***` wyjdzie na stronie z gołymi gwiazdkami. Zwrot w pogrubieniu pisz bez kursywy albo wyjmij go poza pogrubienie.

### Stare bloki (w użyciu)

```
:frazy
target | wymowa | tłumaczenie w języku tekstu | kiedy tak się mówi
Il conto, per favore | il KON-to per fa-WO-re | Rachunek, proszę | Na koniec posiłku. Kelner sam go nie przyniesie.
:koniec
```

Cztery kolumny w TEJ kolejności. Czwarta kolumna (notka) jest obowiązkowa: to ona odróżnia artykuł od rozmówek i to ona staje się przykładem na fiszce. Komórka bez notki zostaje pusta (`… | rachunek |`), nigdy z kreską, bo kreska wyszłaby na fiszce.

```
:uwaga
Ramka „warto wiedzieć": jedna myśl, której nie wypada rozwadniać w akapicie.
:koniec
```

```
:cta
```

Samo w linii, mniej więcej w połowie tekstu: miejsce na zaproszenie do aplikacji.

```
:cwiczenie fiszki
```

(albo `:cwiczenie tekst`, `:cwiczenie sluchanie`) Nakładka-próbka dla niezalogowanego, budowana ze zwrotów `:frazy` tego artykułu. Pozycja znacznika = wysokość, na której wyskoczy. Najwyżej jedna.

### Bloki interaktywne

Każdy zaczyna się wierszem `:::nazwa[atrybuty]` i kończy samotnym `:::`. Wartości atrybutów ZAWSZE w cudzysłowie prostym `"…"`.

Fiszki (kolumny: obcy | tłumaczenie | wymowa: … | notka; to INNA kolejność niż w `:frazy`, rozstrzyga etykieta `wymowa:`):

```
:::fiszki[title="Kluczowe zwroty w restauracji"]
la cuenta | rachunek | wymowa: la KŁEN-ta | Na koniec posiłku, kelnera woła się gestem.
:::
```

Quiz (każde pytanie MUSI mieć dokładnie jedną odpowiedź z `[correct]`, inaczej konsola wstrzyma publikację; `id` unikalne w artykule):

```
:::quiz[id="restauracja_q1" title="Sprawdź, co pamiętasz"]
Pytanie: Jak poprosisz o rachunek?
- La cuenta, por favor. [correct]
- La carta, por favor.
Wyjaśnienie: „La carta" to karta dań. Rachunek to „la cuenta".
Pytanie: …
- …
:::
```

Pytania mają się rozstrzygać z treści artykułu. Trzy pytania na quiz wystarczą.

Słuchanie (tekst zakryty do kliknięcia „Pokaż tekst", bez nagrania każdy wiersz dostaje głos):

```
:::sluchanie[title="Posłuchaj dialogu"]
Buenas noches, una mesa para dos. | Dobry wieczór, stolik dla dwóch osób.
:::
```

Czytanie ze słownikiem (słowo w nawiasie staje się klikalne):

```
:::smart-czytanie[title="Dialog w kawiarni"]
Quiero un [café|kawa|wymowa: ka-FE], por favor.
:::
```

Film (tylko gdy naprawdę coś pokazuje; w tej paczce NIE używaj).

Przycisk na pełny ekran (powtarza quiz w miejscu, gdzie czytelnik zwalnia; blok o tym `id` musi być w tym samym artykule, inaczej przycisk się nie pokaże):

```
:::modal-trigger[target="quiz" id="restauracja_q1" label="Przetestuj wiedzę"]
:::
```

### Które bloki dobrać

- Artykuł o konkretnym języku: ZAWSZE `:::fiszki` albo `:frazy` (z nich czytelnik jednym kliknięciem bierze słówka do swojej talii, więc para obcy i tłumaczenie musi być poprawna samodzielnie, bez zdania).
- Tekst, który czegoś uczy: `:::quiz` (trzy pytania).
- Dialog (zamawianie, meldunek, pytanie o drogę): `:::sluchanie`.
- Krótki tekst ciągły do przeczytania ze słownikiem: `:::smart-czytanie`.
- Dłuższy tekst: `:::modal-trigger` przy quizie.
- Każdy blok zamknięty. Niezamknięty `:::`, literówka w nazwie bloku albo quiz bez `[correct]` sprawiają, że blok znika ze strony bez śladu.

### Wymowa

Zapis fonetyczny w języku czytelnika (dla Polaka gl jako „lj", gn jako „ń"), sylaba akcentowana WIELKIMI literami: `PREN-do`, `la KŁEN-ta`.

## 4. Głos: jak pisać, żeby NIE brzmiało jak AI

1. Zacznij od napięcia albo konkretnej tezy, nigdy od ogólnika. Nie: „W dzisiejszych czasach nauka języków…". Tak: „Większość rozmówek uczy zdań, których nikt nie mówi." albo „W polskim rodzajników nie ma i to jest cały problem."
2. Każdy zwrot ma wymowę I notkę, której nie ma w rozmówkach. Sama para „słowo, tłumaczenie" jest wszędzie. Wartość jest w notce: „Prego | PRE-go | proszę | najbardziej wieloznaczne słowo. Tu znaczy »proszę bardzo«."
3. Tłumacz regułę przez powód, nie przez tabelę do wykucia. Zamiast „przed s+spółgłoska używamy lo": „Powiedz na głos »il studente«. Trzy spółgłoski pod rząd, język się potyka. Dlatego włoski wstawia »lo«."
4. Fakty sprawdzalne, nie ogólniki. Liczba i szczegół budują zaufanie. „Warto pamiętać o lokalnych zwyczajach" nie znaczy nic.
5. Rzeczy, które zdradzają obcego. Cappuccino po obiedzie, „spaghetti bolognese", którego we Włoszech nie ma, parmezan do ryby. To treść, którą ludzie zapisują i podsyłają dalej.
6. Krótkie zdania oznajmujące, przeplatane uzasadnieniem. Bez „z jednej strony… z drugiej strony", bez „podsumowując", bez wyliczania oczywistości, bez sztucznej symetrii akapitów. Jeśli akapit dałoby się wygenerować z samego tytułu, wytnij go.
7. Zero obietnic o wyniku. Nie „płynnie w 3 miesiące". Opisuj, jak jest, nie sprzedawaj efektu.
8. Typowe zdania AI do wycięcia: „to nie tylko X, ale Y", zdanie-puenta w osobnym akapicie po każdej sekcji („I o to właśnie chodzi."), trójki na siłę („szybko, skutecznie i z przyjemnością"), „kluczowy", „niezwykle ważny", „w dzisiejszym świecie", „zanurzmy się", „podróż", „odkryj".

Szybki test akapitu: czy mógł go napisać ktoś, kto nigdy nie był w tym miejscu i nie mówi tym językiem? Jeśli tak, brakuje konkretu z punktów 2, 4 i 5.

## 5. Znaki ZAKAZANE (twarda reguła serwisu)

- Pauza, czyli długa kreska (znak U+2014). Nigdzie: ani w tytule, opisie, treści, notkach, pytaniach quizu. Konsola WSTRZYMUJE publikację tekstu z pauzą. Zamiast niej przebuduj zdanie:
  - dwa zdania: kropka;
  - wyjaśnienie albo wyliczenie: dwukropek;
  - dopowiedzenie: przecinek;
  - wtrącenie: nawias;
  - definicja w liście: „to" albo dwukropek. Zwykły łącznik „-" zostaje tylko tam, gdzie kreska jest naprawdę potrzebna (kwestie dialogu: `- *Avete prenotato?* - *No.*`).
- Kropka środkowa (znak U+00B7) jako separator. Zamiast niej przecinek albo dwukropek.
- Strzałki jako tekst: znaki U+2192 i U+2190 oraz strzałka złożona z łącznika i znaku „większe niż". Pisz słowami („potem", „czyli").
- Półpauza bez odstępów w przedziałach („A1–A2", „12–15 euro") jest dozwolona, ale łącznik „A1-A2" też jest dobry. Półpauza (znak U+2013) z odstępami po obu stronach, wstawiona między dwa człony zdania, to już pauza w przebraniu: zakazana.

## 6. Prawda o Lingarii (gdy artykuł o niej wspomina)

- Pisz tylko o tym, co serwis naprawdę robi (lista w punkcie 1). Gdy nie masz pewności, czy funkcja istnieje, nie pisz o niej.
- Nie podawaj cen, limitów konta darmowego, liczby dni ani godzin (zmieniają się).
- Nie pisz „darmowe Premium", „bez reklam", „subskrypcja".
- Nie pisz, że aplikację można pobrać ze sklepu App Store albo Google Play (wydanie w toku). Wystarczy „Lingaria działa w przeglądarce, aplikacja na telefon jest w drodze" albo nic.
- Najwyżej jedno lub dwa naturalne odniesienia do Lingarii w tekście (plus `:cta`). Artykuł ma uczyć, nie reklamować.

## 7. Teksty w innych językach

- Artykuł w innym języku (np. po hiszpańsku dla Hiszpana uczącego się angielskiego) to ZAWSZE osobno napisany tekst z realiami tego czytelnika, nigdy przekład polskiego artykułu. Przekład tych samych tekstów na wiele języków wygląda dla Google jak treść masowa i był już powodem odmowy.
- Wymowa w takim tekście jest zapisana w pisowni języka czytelnika, nie po polsku.
- Ustaw wtedy `jezyk_tekstu` na język czytelnika i `jezyk_docelowy` na język, którego tekst uczy.

## 8. Dobór tematów

- Trzy działy: sytuacje z życia (praktyka), gramatyka bez wkuwania, metoda nauki.
- Temat nie musi być gramatyczny. „Na targu", „u lekarza", „przejażdżka rowerem", „wynajem mieszkania" są równie dobre: liczy się gęstość użytecznych zwrotów.
- Myśl zapytaniami, które ludzie wpisują w Google: długie i konkretne („jak zamówić kawę po hiszpańsku", „X co to znaczy", „nauka angielskiego z piosenek", „fiszki online"), a nie ogólne („nauka hiszpańskiego").
- Tytuł: konkretna obietnica z frazą z zapytania. Opis: jedno zdanie z tą frazą, do 175 znaków.

## 9. Lista kontrolna przed oddaniem (ta sama, którą sprawdza konsola)

Czerwone (wstrzymują publikację, więc MUSZĄ być spełnione):

- Każde pytanie każdego quizu ma dokładnie jedną odpowiedź z `[correct]`.
- Każdy blok `:::` jest zamknięty, nazwa bloku bez literówki, atrybuty w cudzysłowie, `modal-trigger` wskazuje istniejący `id`.
- Ani jednej pauzy (U+2014) w tytule, opisie i treści.

Żółte (nic nie blokują, ale mają być spełnione):

- Co najmniej 600 słów (górnej granicy nie ma; długość dopasuj do tematu).
- Każdy zwrot w `:frazy` ma notkę w czwartej kolumnie.
- Opis jest i ma najwyżej 175 znaków.
- `dzial` to `praktyka`, `gramatyka` albo `metoda`.
- `powiazane` wskazują istniejące artykuły, nie ten sam.

Dodatkowo:

- `status: szkic`, `autor:` puste.
- Bez kropki środkowej i strzałek jako tekstu.
- Bez HTML, bez kursywy wewnątrz pogrubienia.
- Pierwsze zdanie nie pasuje do dowolnego innego artykułu o nauce języków.
- Każdy fakt (cena, zwyczaj, liczba) jest prawdziwy. Jeśli nie jesteś pewien, usuń go.

## 10. Jak oddać paczkę

- Każdy artykuł w osobnym pliku `{slug}.txt` według punktu 2.
- Nie dziel jednego tematu na kilka podobnych tekstów w tym samym języku. Dwa podobne teksty konkurują ze sobą w Google.
