# Lingaria: 150 tekstów do trybu „Czytanie"

Każdy plik `.txt` to jeden gotowy do wklejenia tekst (pierwsza linia to tytuł, potem jedno zdanie w linii).

## Nazwy plików
`{JĘZYK_INTERFEJSU}_{JĘZYK_NAUKI}_{opis}.txt`, np. `POLSKI_WLOSKI_...txt` = konto w języku polskim, tekst po włosku.
Sam tekst jest zawsze wyłącznie w języku nauki. Język interfejsu występuje tylko w nazwie pliku.

## Zawartość
- 25 języków nauki × 6 tekstów = 150 tekstów; 25 języków interfejsu (po 24 teksty dla polskiego i angielskiego, reszta rozłożona).
- Poziomy: A1 (25), A2 (50), B1 (50), B2 (25). Długość: 9–28 linii treści plus tytuł.
- Kategorie: codzienne, podróże (samolot, pociąg, hotel…), praca i kariera, kultura (targ, kościół/świątynia, święta…), opowieści i dialogi, listy i opisy.
- Dialogi: `IMIĘ: kwestia`, sceny: `SCENA 1 – ...` (w języku tekstu).
- Szczegółowa lista: `manifest-teksty.csv` (język, poziom, temat, liczba linii).

## Jak powstały i co sprawdzono
1. Teksty napisało 10 agentów (po 2–3 języki) według jednakowych reguł jakości: sens, poziom CEFR, brak fałszywych faktów, kultura kraju języka.
2. Każdy tekst przeczytał i poprawił niezależny recenzent (gramatyka, naturalność, logika, fakty, poziom). Poprawił ok. 3/4 tekstów.
3. Drugi niezależny przebieg („humanizer"): usuwanie śladów pisania przez AI (morały na końcu, patos, reklamowe przymiotniki, sztuczne trójki, stylistyczne myślniki), bez zmiany treści i poziomu.
4. Automatyczna walidacja: liczba linii, kodowanie, brak pustych linii, zgodność pisma i wykrytego języka z nazwą pliku (test z celowo zepsutymi plikami wykrył 6/6 usterek).

## Uwagi
- Portugalski jest brazylijski, chorwacki ijekawski, norweski to bokmål, chiński to uproszczony.
- Fikcyjne miejsca i ceny są oznaczone w treści jako zwykłe szczegóły opowieści, a fakty o prawdziwych miejscach ograniczono do pewnych.
- Dla rzadszych języków (hindi, arabski, koreański, japoński, chiński, fiński, turecki) dobrze, żeby osoba znająca język przejrzała teksty przed publikacją: recenzje były wykonane przez model, nie przez native speakera.
