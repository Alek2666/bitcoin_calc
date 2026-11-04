# Lingaria: 30 artykułów w 25 językach (szkice)

30 gotowych szkiców artykułów w formacie z przewodnika „Lingaria: jak pisać artykuły”. Tylko 2 są po polsku. Pozostałe 28 napisano
od razu w językach czytelników (25 języków interfejsu), a nie przetłumaczono z polskiego. Każdy uczy jednego z 13 języków
(cs, de, el, en, es, fr, it, ja, ko, pl, pt, sv, tr) albo jest artykułem o metodzie nauki bez języka docelowego.
Pełna lista, z tytułami, poziomami, liczbą słów i frazą z Google, jest w [SPIS.md](SPIS.md).

## Co jest w środku
- `artykuly/{slug}.txt`: artykuł w całości (nagłówek, `---`, treść). Nazwa pliku to slug.
- `narzedzia/waliduj_artykul.py`: walidator reguł z przewodnika (czerwone błędy wstrzymują publikację, żółte to ostrzeżenia).
  Sprawdza m.in. pola nagłówka, długość `opis` (do 175), brak U+2014 i kropki środkowej U+00B7, strzałki, półpauzy w tekście,
  bloki `:frazy…:koniec` (4 kolumny), `:::quiz` (dokładnie jedna odpowiedź `[correct]` na pytanie), jedno `:cta` w środku tekstu,
  zgodność języka tekstu z nagłówkiem (py3langid), minimum 600 słów, istniejące slugi w `powiazane`.
- `narzedzia/zbuduj_spis.py`: odtwarza `SPIS.md` z nagłówków plików (po zmianach w artykułach uruchom go ponownie).
- `narzedzia/tematy.json`: założenia dla każdego artykułu (język tekstu i docelowy, dział, poziom, fraza z Google).
- `narzedzia/istniejace.json`: 7 slugów, które już są w serwisie i można do nich linkować.
- `narzedzia/instrukcja-dla-autorow.md`: przewodnik właściciela plus moje doprecyzowania, z którymi pisali i sprawdzali autorzy.

Uruchomienie walidatora (potrzebny `pip install py3langid`):

```bash
cd lingaria-artykuly/narzedzia
python3 waliduj_artykul.py ../artykuly tematy.json istniejace.json
```

Ostatni przebieg (po drugiej recenzji): 30/30 plików, 0 czerwonych, 4 żółte. Żółte to tylko ostrzeżenia, że długość odbiega od orientacyjnego celu
z `tematy.json` (hindi, grecki, japoński i duński o Madrycie wyszły dłuższe). Przewodnik nie wymaga stałej długości, więc zostawiłem je bez cięcia.

## Stan i publikacja
- Wszystkie pliki mają `status: szkic`, puste `autor:` i datę 2026-11-04. Nic nie zostało nigdzie opublikowane.
- Długości są różne (779 do 1509 słów, mediana 1190), bo przewodnik nie wymaga stałej liczby znaków.
- Publikuje człowiek po przeczytaniu (zasada z przewodnika), a przy wklejaniu do panelu trzeba uzupełnić `autor:`.
- Pole `zdjecie_pomysl:` w nagłówku to podpowiedź dla osoby dobierającej zdjęcie. Zgodnie z przewodnikiem parser ją pomija,
  a redakcja ją czyta. Obrazów do artykułów nie generowano.

## Co sprawdzić przed publikacją
Teksty przeszły cztery etapy: pisanie, niezależną recenzję ze sprawdzaniem faktów w sieci, korektę w duchu humanizera i drugą recenzję
skupioną na sensie i zrozumieniu (czytanie jak uczeń, spójność przykładów, quizy, bezpieczeństwo fraz). Druga runda znalazła w każdym
artykule od 3 do 12 problemów, m.in. błędne tłumaczenie (`entretien d'embauche` jako „appointment”), błędny akcent w greckim `γεια σου`,
niespójne dialogi i zapisy wymowy, które czytelnik odczytałby inaczej. Mimo tego żadnego tekstu nie czytał native speaker, więc poniższe
punkty są do zweryfikowania.

**1. Zapisy wymowy literami czytelnika są przybliżone.** Szczególnie w artykułach, gdzie tekst lub język docelowy to arabski, hindi,
japoński, koreański, chiński, grecki, turecki albo fiński (11 plików, kolumna „Natywna kontrola” w SPIS.md). W arabskim i hindi
akcent oznaczono znakiem IPA ˈ. Tekst arabski jest pisany od prawej do lewej, więc łacińskie etykiety i zapisy wymowy w zwykłym edytorze mogą
wyglądać inaczej niż w panelu. Artykuł chiński zapisuje wymowę francuskich słów w stylu pinyin (zapis przybliżony, bo francuskie dźwięki
nie mają dokładnych odpowiedników w pinyin).

**2. Fakty zależne od daty lub oparte na źródłach wtórnych.** Sprawdzone w sieci podczas pracy, ale mogą się zmienić:
- `ruotsi-kaupassa-ja-kahvilassa`: szwedzka ustawa o obowiązku przyjmowania gotówki w sklepach spożywczych i aptekach z obsługą kasową,
  w mocy od 1 lipca 2026, z wyjątkami. Potwierdzona w źródłach (Riksdag FiU39, The Local, Sveriges Radio).
- `spansk-i-byen-metro-og-taxa`: płatność kartą lub telefonem przy bramce madryckiego metra od 1 czerwca 2026. Potwierdzona w źródłach
  (Comunidad de Madrid, Metro de Madrid). Promocyjna cena 1,50 euro jest tymczasowa i artykuł jej nie podaje. Dopłata lotniskowa jest
  odesłana na stronę przewoźnika, bo kwota się zmienia.
- `polska-mova-v-apteci-ta-magazini`: opłata za torby foliowe w Polsce od 2018.
- `japanese-at-the-konbini`: opłata za plastikowe torby w Japonii od lipca 2020 oraz zdanie z oznaczeniem „January 2023”.
- `almanca-doktorda`: e-zwolnienie (eAU) i e-recepta (E-Rezept) w Niemczech, stan na 2023 i 2024.
- `frances-en-la-panaderia` i `fayu-kafeiguan-diandan`: dekret z 1993 o „pain de tradition française” i ustawa z 25 maja 1998 o nazwie „boulangerie”.
- `tuerkisch-im-urlaub-tee-und-basar`: baklawa z Gaziantep jako chronione oznaczenie geograficzne UE (2013).
- `germanika-sto-aerodromio`: kwoty odszkodowań z rozporządzenia UE 261/2004. Reforma nie weszła w życie, ale warto sprawdzić aktualny stan.
- `talijanski-u-restoranu`: opłata za „coperto” (brak zakazu na poziomie państwa, obowiązek podania kwoty w menu). Przepisy regionalne mogą się różnić.
- `ilboneo-sikdang-jumun` i `kankokugo-kafe-de-chuumon`: zwyczaje w koreańskich kawiarniach i restauracjach opisane z zastrzeżeniami, bo różnią się między lokalami.

**3. Pozostałe wątpliwości z drugiej recenzji** (recenzent nie potwierdził ich w źródłach albo to kwestia ucha):
- `polska-mova-v-apteci-ta-magazini`: szczegóły e-recepty (czterocyfrowy kod i PESEL), mojeIKP, UOKiK i paragon sprawdzone tylko z wiedzy ogólnej.
- `espanhol-falsos-amigos`: `coger` jako wulgaryzm w Meksyku i Argentynie (powszechnie znany fakt, bez sprawdzenia w sieci).
- `spanska-pa-semester-tapas-och-notan`: fraza `Perdona, ¿me cobras?` (naturalna, ale bez źródła).
- `spansk-i-byen-metro-og-taxa`: zasada kasowania biletu T-casual przy przesiadkach i gaśnięcie światła na dachu madryckiej taksówki.
- `germanika-sto-aerodromio`: istnienie niebieskiego wyjścia celnego dla lotów z UE we Frankfurcie i naturalność słowa `Gatewechsel`.
- `tuerkisch-im-urlaub-tee-und-basar`: dokładne daty zamknięcia Kapalıçarşı w czasie Bayramu oraz `açık/koyu` przy zamawianiu herbaty (potwierdzone tylko w słowniku).
- `polstina-pro-cechy-nakup-a-falesni-pratele`: znaczenie słowa `jagoda` jako borówka bywa regionalne.
- `ilboneo-sikdang-jumun`: uwagi o pałeczkach wbitych w ryż i o niewoływaniu obsługi „이모/사장님” w Japonii (wiedza ogólna).
- `kankokugo-kafe-de-chuumon`: część zapisów kana dla koreańskich zwrotów (np. ムォエヨ) to przybliżenia.
- `fayu-kafeiguan-diandan`: zapis francuskiego R literami pinyin-owymi (np. „kh”) trzeba ocenić uchem.
- `ruotsi-kaupassa-ja-kahvilassa`: zapisy wymowy `ursäkta`, `också`, `varsågod` i szwedzkiego „u” wymagają rodzimego słuchacza.
- `anglais-au-telephone`: zapis „kannt” odpowiada angielszczyźnie amerykańskiej.

**4. Obietnice dotyczące Lingarii.** Artykuły nie zawierają twierdzeń o funkcjach poza tymi, które dopuszcza przewodnik. Mimo to
przed publikacją przejrzyj blok `:cta` i ewentualne odwołania do fiszek w każdym pliku.

## Powiązania wewnętrzne
Pola `powiazane` wskazują tylko slugi z tej paczki i siedem istniejących w serwisie (lista w `narzedzia/istniejace.json`).
Walidator ostrzega, jeśli któryś slug nie istnieje. Jeśli zmienisz slug w panelu, popraw odpowiednie wpisy w `powiazane` innych plików.
