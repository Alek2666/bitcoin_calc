import json, os
def op(t, d, ui=False): n = {"kto": "ai", "opis": True}; n.update({"jezyk_ucznia": True} if ui else {}); n.update(tekst=t, dalej=d); return n
def a(t, d): return {"kto": "ai", "tekst": t, "dalej": d}
def q(t, ins, bl, *br):
    g = []
    for b in br:
        x = {"intencja": b[0], "wzor": b[1], "dalej": b[2]}
        if len(b) > 3 and b[3]: x["ukryta"] = True
        g.append(x)
    return {"kto": "ai", "tekst": t, "instrukcja": ins, "blad": bl, "galezie": g}
def u(ins, wz, bl, d): return {"kto": "uczen", "instrukcja": ins, "wzor": wz, "blad": bl, "dalej": d}
def p(wz, d): return {"kto": "uczen", "na_pamiec": True, "wzor": wz, "dalej": d}
def sw(ins, kr, wz, bl, d): return {"kto": "uczen", "swobodna": True, "instrukcja": ins, "kryteria": kr, "wzor": wz, "blad": bl, "dalej": d}
def fin(t): return {"kto": "ai", "koniec": True, "tekst": t}
def S(klucz, tytul, opis, cefr, ikona, glos, bot, uczen, slowka, luki, tagi, start, wezly):
    return dict(klucz=klucz, tytul=tytul, opis=opis, cefr=cefr, ikona=ikona, glos=glos, role={"bot": bot, "uczen": uczen}, slowka=slowka, luki=luki, jezyki=[], tagi=tagi, status="szkic", drzewo={"start": start, "wezly": wezly})
ALL = []

ALL.append(S("lingaria_kawiarnia_a1", "Kawa i ciasto w kawiarni", "Zamawiasz kawę lub herbatę i coś słodkiego w małej kawiarni. Kelnerka pyta o mleko, ciasto i imię na zamówieniu.",
 "A1", "fi-rr-coffee", "auto:feminine", "Kelnerka", "Gość", ["kawa", "herbata", "ciasto", "woda", "mleko", "cukier", "proszę", "dziękuję"], ["kawa", "ciasto"],
 ["a1", "kawiarnia", "kawa", "zamawianie", "napoje", "jedzenie"], "op1", {
 "op1": op("Wchodzisz do małej kawiarni. Jest rano, pachnie świeżą kawą. Przy ladzie stoi uśmiechnięta kelnerka.", "s1"),
 "s1": q("Dzień dobry! Co podać?", "Zamów coś do picia", "Przepraszam, nie dosłyszałam. Co podać do picia?",
   ("kawa", "Poproszę kawę.", "s2"), ("herbata", "Poproszę herbatę.", "a1"), ("woda", "Poproszę wodę.", "s3"), ("zart", "Poproszę kawę dla mojego psa.", "a2", True)),
 "a1": a("Dobrze. Mamy czarną i zieloną herbatę. Którą lubisz?", "u1"),
 "u1": u("Powiedz, jaką herbatę chcesz", "Poproszę zieloną herbatę.", "Przepraszam, czarną czy zieloną?", "s3"),
 "a2": a("Ha! Dla psa mamy tylko miskę wody. Kawy lepiej nie polecam!", "s3"),
 "s2": q("Dobrze, kawa. Z mlekiem czy bez mleka?", "Powiedz, czy chcesz mleko", "Przepraszam, z mlekiem czy bez?",
   ("mleko", "Z mlekiem, proszę.", "s3"), ("bez", "Bez mleka, dziękuję.", "s3"), ("cukier", "Z mlekiem i z cukrem.", "s3")),
 "s3": q("A może coś słodkiego? Mamy ciasto czekoladowe i szarlotkę.", "Powiedz, czy chcesz ciasto", "Przepraszam, chcesz ciasto?",
   ("czekolada", "Poproszę ciasto czekoladowe.", "a3"), ("szarlotka", "Poproszę szarlotkę.", "a3"), ("nie", "Nie, dziękuję. To wszystko.", "a3")),
 "a3": a("Dobrze. Na jakie imię zapisać zamówienie?", "u2"),
 "u2": u("Podaj swoje imię", "Mam na imię {imie}.", "Przepraszam, jak masz na imię?", "a4"),
 "a4": a("Dziękuję! Zamówienie dla {imie|tej osoby} będzie gotowe za chwilę. Razem osiem euro.", "s4"),
 "s4": q("Płacisz kartą czy gotówką?", "Powiedz, jak płacisz", "Przepraszam, kartą czy gotówką?",
   ("karta", "Kartą, proszę.", "fin2"), ("gotowka", "Gotówką, proszę.", "a5")),
 "a5": a("Dziękuję! Zanim przygotuję zamówienie, powiedz mi coś. Jak się dziś czujesz?", "sw1"),
 "sw1": sw("Powiedz, jak się dziś czujesz", "jak się czujesz i dlaczego, 1 lub 2 zdania", "Czuję się dobrze, bo świeci słońce.", "Przepraszam, pytałam, jak się czujesz.", "op2"),
 "op2": op("Wskazówka: w kawiarni zacznij od słowa „poproszę” i nazwy napoju. To krótko, grzecznie i zawsze zrozumiale.", "p1", True),
 "p1": p("Poproszę jeszcze jedną kawę.", "fin1"),
 "fin1": fin("Już robię! Do zobaczenia!"),
 "fin2": fin("Dziękuję! Kawa będzie za chwilę przy twoim stoliku. Miłego dnia!")}))

ALL.append(S("lingaria_poznajemy_sie_a1", "Poznajemy się na przyjęciu", "Poznajesz kogoś na przyjęciu. Podajesz imię, mówisz, skąd jesteś, czym się zajmujesz i co lubisz robić w wolnym czasie.",
 "A1", "fi-rr-comment", "auto:masculine", "Nowy znajomy", "Ty", ["imię", "miasto", "mieszkam", "pracuję", "studiuję", "lubię", "wolny czas", "miło mi"], ["mieszkam", "lubię"],
 ["a1", "poznawanie", "przedstawianie", "hobby", "praca", "rozmowa"], "op1", {
 "op1": op("Jesteś na przyjęciu u znajomych. Obok ciebie stoi sympatyczny mężczyzna ze szklanką soku. Uśmiecha się do ciebie.", "a1"),
 "a1": a("Cześć! Jestem Alex. A ty jak masz na imię?", "u1"),
 "u1": u("Przedstaw się", "Cześć, mam na imię {imie}.", "Przepraszam, jak masz na imię?", "s1"),
 "s1": q("Miło mi cię poznać! Skąd jesteś?", "Powiedz, skąd jesteś lub gdzie mieszkasz", "Przepraszam, skąd jesteś?",
   ("skad", "Jestem z {miasto}.", "s2"), ("mieszkam", "Mieszkam w {miasto}.", "s2"), ("daleko", "Jestem z bardzo daleka.", "a2"), ("prywatne", "Wolę o tym nie mówić.", "a6")),
 "a2": a("To ciekawe! Opowiesz mi kiedyś więcej.", "s2"),
 "a6": a("Rozumiem, nie ma sprawy. Miło było pogadać. Idę po ciastko.", "fin2"),
 "s2": q("{miasto|Twoje miasto} brzmi pięknie! A czym się zajmujesz?", "Powiedz, czym się zajmujesz", "Przepraszam, czym się zajmujesz?",
   ("studia", "Studiuję.", "a4"), ("praca", "Pracuję w szkole.", "a4"), ("szuka", "Szukam pracy.", "a4"), ("tajne", "Tego nie mogę ci powiedzieć.", "a3", True)),
 "a3": a("Ha, brzmi tajemniczo! Nie będę pytał dalej.", "a4"),
 "a4": a("Fajnie! Ja uwielbiam gotować w wolnym czasie. A ty? Co lubisz robić po pracy lub po zajęciach?", "sw1"),
 "sw1": sw("Opowiedz, co lubisz robić w wolnym czasie", "co lubisz robić i jak często to robisz, 2 zdania", "Lubię czytać książki i chodzić na spacery. Robię to w weekendy.", "Przepraszam, pytałem, co lubisz robić w wolnym czasie.", "op2"),
 "op2": op("Wskazówka: gdy kogoś poznajesz, zadaj pytanie zwrotne, na przykład „A ty?”. To najprostszy sposób, by rozmowa trwała dłużej.", "p1", True),
 "p1": p("Miło było cię poznać.", "fin1"),
 "fin1": fin("Mnie też! Do zobaczenia przy stole z ciastem!"),
 "fin2": fin("Do zobaczenia później!")}))

ALL.append(S("lingaria_droga_do_dworca_a1", "Jak dojść do dworca?", "Szukasz dworca w obcym mieście. Pytasz przechodnia o drogę, potwierdzasz wskazówki i dowiadujesz się, ile zostało do celu.",
 "A1", "fi-rr-map-marker", "auto:feminine", "Przechodnia", "Ty", ["dworzec", "prosto", "w lewo", "w prawo", "skrzyżowanie", "blisko", "daleko", "apteka"], ["skrzyżowanie", "apteka"],
 ["a1", "droga", "miasto", "kierunki", "ulica", "orientacja"], "op1", {
 "op1": op("Stoisz na ulicy w obcym mieście. Szukasz dworca kolejowego, ale nie masz mapy. Obok idzie przyjazna kobieta.", "u1"),
 "u1": u("Zatrzymaj tę osobę i zapytaj, gdzie jest dworzec", "Przepraszam, gdzie jest dworzec?", "Słucham? Czego szukasz?", "s1"),
 "s1": q("Dworzec? To niedaleko. Idź prosto tą ulicą aż do skrzyżowania. Rozumiesz?", "Powiedz, czy rozumiesz", "Przepraszam, rozumiesz? Prosto aż do skrzyżowania.",
   ("tak", "Tak, rozumiem. Prosto do skrzyżowania.", "a1"), ("nie", "Przepraszam, nie rozumiem. Powtórz, proszę.", "a2"), ("taxi", "Czy mogę pojechać taksówką?", "a3", True)),
 "a2": a("Dobrze. Jeszcze raz, powoli: prosto, aż do skrzyżowania.", "a1"),
 "a3": a("Oczywiście, ale pieszo to tylko pięć minut.", "a1"),
 "a1": a("Na skrzyżowaniu skręć w lewo. Zobaczysz dużą aptekę. Dworzec jest zaraz za nią.", "s2"),
 "s2": q("A teraz sprawdźmy. Gdzie skręcasz na skrzyżowaniu?", "Powiedz, gdzie skręcasz", "Przepraszam, w którą stronę skręcasz?",
   ("lewo", "W lewo, przy aptece.", "a4"), ("prawo", "W prawo.", "a5"), ("niewiem", "Nie wiem, gdzie jestem.", "a8")),
 "a5": a("Nie, w lewo! W prawo jest rzeka.", "a4"),
 "a8": a("Spokojnie, pokażę ci to na mapie w telefonie.", "fin2"),
 "a4": a("Dokładnie! Dworzec jest po prawej stronie, za apteką.", "u2"),
 "u2": u("Zapytaj, czy to daleko", "Czy to daleko stąd?", "Słucham?", "a6"),
 "a6": a("Nie, tylko pięć minut pieszo. A ty? Dokąd jedziesz pociągiem?", "sw1"),
 "sw1": sw("Powiedz, dokąd jedziesz i po co", "dokąd jedziesz i po co, 1 lub 2 zdania", "Jadę do stolicy odwiedzić przyjaciółkę.", "Przepraszam, pytałam, dokąd jedziesz.", "op2"),
 "op2": op("Wskazówka: kierunki to proste słowa: prosto, w lewo, w prawo. Warto je znać na pamięć, bo przydają się w każdym mieście.", "p1", True),
 "p1": p("Bardzo dziękuję za pomoc.", "fin1"),
 "fin1": fin("Nie ma za co! Miłej podróży!"),
 "fin2": fin("Proszę, tu jest dworzec na mapie. Powodzenia!")}))

ALL.append(S("lingaria_lotnisko_odprawa_a2", "Odprawa na lotnisku", "Odprawiasz się na lot za granicę. Podajesz dokumenty, bagaż i miejsce w samolocie, a potem pytasz o bramkę i opowiadasz o celu podróży.",
 "A2", "fi-rr-plane", "auto:masculine", "Pracownik odprawy", "Ty", ["lotnisko", "paszport", "bilet", "bagaż", "bramka", "okno", "korytarz", "lot"], ["paszport", "bramka"],
 ["a2", "lotnisko", "podroz", "samolot", "bagaz", "odprawa"], "op1", {
 "op1": op("Jesteś na lotnisku przy stanowisku odprawy. Za chwilę lecisz za granicę. Pracownik odprawy czeka z uśmiechem.", "s1"),
 "s1": q("Dzień dobry! Poproszę paszport i bilet. Dokąd dziś lecimy?", "Podaj dokumenty i powiedz, dokąd lecisz", "Przepraszam, nie dosłyszałem. Dokąd lecimy?",
   ("paszport", "Proszę, oto mój paszport. Lecę do {miasto}.", "s2"), ("bilet", "Przepraszam, nie mam biletu w ręku.", "a2"), ("brak", "Chyba nie mam paszportu przy sobie.", "a7"), ("basen", "Czy samolot ma basen?", "a3", True)),
 "a2": a("Nic nie szkodzi. Wystarczy numer rezerwacji.", "u1"),
 "u1": u("Podaj numer rezerwacji", "Mój numer rezerwacji to AB1234.", "Słucham? Jaki numer?", "s2"),
 "a3": a("Niestety nie, ale mamy bardzo wygodne fotele.", "s2"),
 "a7": a("Bez paszportu nie mogę cię odprawić na lot zagraniczny. Wróć po dokument, jeszcze zdążysz.", "fin2"),
 "s2": q("Dziękuję. Lot do {miasto|tego miasta} jest punktualny. Masz bagaż do nadania?", "Powiedz, jaki masz bagaż", "Przepraszam, walizka czy tylko bagaż podręczny?",
   ("walizka", "Mam jedną walizkę do nadania.", "a4"), ("reczny", "Mam tylko bagaż podręczny.", "s3")),
 "a4": a("Postaw walizkę na wadze. Waży dwadzieścia kilogramów, to w porządku.", "s3"),
 "s3": q("Gdzie wolisz siedzieć, przy oknie czy przy korytarzu?", "Wybierz miejsce w samolocie", "Przepraszam, okno czy korytarz?",
   ("okno", "Poproszę miejsce przy oknie.", "a5"), ("korytarz", "Poproszę miejsce przy korytarzu.", "a5"), ("obojetnie", "Obojętnie, jakie jest wolne.", "a5")),
 "a5": a("Oto twoja karta pokładowa. Bramka numer dwanaście. Masz jeszcze jakieś pytanie?", "u2"),
 "u2": u("Zapytaj, o której zaczyna się wejście do samolotu", "O której zaczyna się wejście na pokład?", "Słucham?", "a6"),
 "a6": a("Wejście zaczyna się godzinę przed startem. A ty? Po co lecisz, w podróż służbową czy na wakacje?", "sw1"),
 "sw1": sw("Opowiedz, po co lecisz", "po co lecisz i na jak długo, 2 zdania", "Lecę na wakacje na tydzień. Chcę odpocząć i zwiedzić miasto.", "Przepraszam, pytałem, po co lecisz.", "op2"),
 "op2": op("Wskazówka: na tablicy odlotów szukaj trzech rzeczy: numeru lotu, godziny i bramki. Te słowa warto znać w każdym języku.", "p1", True),
 "p1": p("Przepraszam, gdzie jest bramka numer dwanaście?", "fin1"),
 "fin1": fin("Prosto, a potem w prawo. Miłego lotu!"),
 "fin2": fin("Do zobaczenia! Powodzenia i szybkiego powrotu z paszportem.")}))

ALL.append(S("lingaria_hotel_zameldowanie_a2", "Zameldowanie w hotelu", "Meldujesz się w hotelu wieczorem po podróży. Podajesz nazwisko, wybierasz pokój i śniadanie, pytasz o internet i wymeldowanie.",
 "A2", "fi-rr-bed", "auto:feminine", "Recepcjonistka", "Ty", ["hotel", "rezerwacja", "pokój", "klucz", "śniadanie", "internet", "winda", "wymeldowanie"], ["rezerwacja", "klucz"],
 ["a2", "hotel", "podroz", "rezerwacja", "pokoj", "sniadanie"], "op1", {
 "op1": op("Jest wieczór. Wchodzisz do hotelu po długiej podróży. Za ladą stoi miła recepcjonistka.", "a1"),
 "a1": a("Dobry wieczór! Witamy w naszym hotelu. W czym mogę pomóc?", "u1"),
 "u1": u("Powiedz, że masz rezerwację", "Dobry wieczór. Mam rezerwację na nazwisko {nazwisko}.", "Przepraszam, na jakie nazwisko?", "s1"),
 "s1": q("Dziękuję. Mam rezerwację dla {nazwisko|ciebie} na trzy noce. Wolisz łóżko małżeńskie czy dwa osobne łóżka?", "Wybierz rodzaj pokoju", "Przepraszam, nie dosłyszałam. Łóżko małżeńskie czy dwa łóżka?",
   ("malzenskie", "Poproszę łóżko małżeńskie.", "a2"), ("dwa", "Poproszę dwa osobne łóżka.", "a2"), ("widok", "Czy macie pokój z widokiem na morze?", "a3"), ("kot", "Czy mogę zabrać do pokoju mojego kota?", "a4", True)),
 "a3": a("Mamy taki pokój na piątym piętrze. Jest trochę droższy.", "u2"),
 "u2": u("Powiedz, że bierzesz ten pokój", "Dobrze, wezmę ten pokój.", "Przepraszam, bierzesz ten pokój?", "a2"),
 "a4": a("Koty są mile widziane, ale kot musi być w transporterze.", "a2"),
 "a2": a("Świetnie. Pokój numer trzysta dwanaście jest na trzecim piętrze. Śniadanie jest od siódmej do dziesiątej.", "s2"),
 "s2": q("Czy chcesz jeść śniadanie w restauracji hotelowej, czy zamówić je do pokoju?", "Powiedz, gdzie chcesz jeść śniadanie", "Przepraszam, śniadanie w restauracji czy w pokoju?",
   ("restauracja", "Zjem śniadanie w restauracji.", "a5"), ("pokoj", "Poproszę śniadanie do pokoju.", "a5"), ("rezygnacja", "Przepraszam, wolę zrezygnować z rezerwacji.", "a8")),
 "a8": a("Rozumiem. Anuluję rezerwację bez opłat. Dziękuję za informację.", "fin2"),
 "a5": a("Dobrze. Oto klucz do pokoju. Winda jest po prawej stronie.", "s3"),
 "s3": q("Czy mogę jeszcze w czymś pomóc?", "Zapytaj o coś albo podziękuj", "Przepraszam, czy mogę w czymś pomóc?",
   ("internet", "Jakie jest hasło do internetu?", "a6"), ("wymeldowanie", "O której trzeba opuścić pokój?", "a7"), ("nie", "Nie, dziękuję. To wszystko.", "a9")),
 "a6": a("Hasło jest na karcie w pokoju.", "a9"),
 "a7": a("Wymeldowanie jest do jedenastej.", "a9"),
 "a9": a("Miłego pobytu! A tak między nami, jak minęła podróż?", "sw1"),
 "sw1": sw("Opowiedz o swojej podróży", "jak minęła podróż i jak się czujesz, 2 zdania", "Podróż była długa, ale spokojna. Chętnie się dziś wyśpię.", "Przepraszam, pytałam, jak minęła podróż.", "op2"),
 "op2": op("Wskazówka: w hotelu często usłyszysz słowa „rezerwacja”, „klucz” i „wymeldowanie”. Dobrze je znać, zanim przyjedziesz.", "p1", True),
 "p1": p("Poproszę budzenie o siódmej rano.", "fin1"),
 "fin1": fin("Oczywiście! Dobranoc i miłego odpoczynku!"),
 "fin2": fin("Do widzenia i miłego wieczoru!")}))

ALL.append(S("lingaria_restauracja_kolacja_a2", "Kolacja w restauracji", "Zamawiasz kolację w restauracji: napój, danie główne, deser i rachunek. Mówisz kelnerowi o alergii i opisujesz, jak smakowało.",
 "A2", "fi-rr-utensils", "auto:masculine", "Kelner", "Gość", ["menu", "zupa", "danie główne", "deser", "rachunek", "napój", "alergia", "woda"], ["rachunek", "alergia"],
 ["a2", "restauracja", "jedzenie", "zamawianie", "napoje", "rachunek"], "op1", {
 "op1": op("Wieczorem wchodzisz do restauracji. Na stołach stoją świece, gra spokojna muzyka. Podchodzi kelner z kartą dań.", "s1"),
 "s1": q("Dobry wieczór! Oto menu. Co przynieść do picia na początek?", "Zamów napój", "Przepraszam, nie dosłyszałem. Co przynieść do picia?",
   ("woda", "Poproszę wodę.", "a1"), ("sok", "Poproszę sok pomarańczowy.", "a1"), ("lemoniada", "Poproszę szklankę lemoniady.", "a1"), ("smok", "Poproszę wodę z lodem dla mojego smoka.", "a2", True)),
 "a2": a("Dla smoka mamy tylko gorącą zupę! Przyniosę też wodę dla ciebie.", "a1"),
 "a1": a("Już przynoszę. Czy możemy przyjąć zamówienie na danie główne?", "u1"),
 "u1": u("Zamów danie główne", "Poproszę {danie}.", "Przepraszam, jakie danie?", "s2"),
 "s2": q("{danie|To danie} brzmi świetnie. Czy jest jakaś alergia na jedzenie?", "Powiedz, czy masz alergię", "Przepraszam, czy jest jakaś alergia?",
   ("nie", "Nie, nie mam alergii.", "a3"), ("orzechy", "Tak, mam alergię na orzechy.", "a4"), ("gluten", "Tak, nie mogę jeść glutenu.", "a4"), ("poniedzialki", "Mam alergię na poniedziałki.", "a5", True)),
 "a4": a("Dziękuję za informację. Poproszę kuchnię o specjalne przygotowanie.", "a3"),
 "a5": a("Na szczęście dziś jest piątek!", "a3"),
 "a3": a("Zamówienie przyjęte. Danie będzie gotowe za piętnaście minut.", "a6"),
 "a6": a("Minęło trochę czasu. Mam nadzieję, że smakowało. Mamy dziś lody, sernik i świeże owoce.", "s3"),
 "s3": q("Czy chcesz deser?", "Zamów deser albo poproś o rachunek", "Przepraszam, deser czy rachunek?",
   ("lody", "Poproszę lody.", "a7"), ("sernik", "Poproszę sernik.", "a7"), ("rachunek", "Nie, dziękuję. Poproszę rachunek.", "a8")),
 "a8": a("Oczywiście, przynoszę rachunek. Razem trzydzieści euro. Dziękuję i do zobaczenia!", "fin2"),
 "a7": a("Dobry wybór! Razem trzydzieści pięć euro. A jak ci smakowała kolacja?", "sw1"),
 "sw1": sw("Powiedz, jak smakowała kolacja", "co smakowało, a co mniej, 2 zdania", "Zupa była bardzo smaczna, a danie główne trochę za słone.", "Przepraszam, pytałem, jak smakowała kolacja.", "op2"),
 "op2": op("Wskazówka: w restauracji nie wołaj kelnera głośno. Wystarczy powiedzieć „przepraszam” i spokojnie podnieść rękę.", "p1", True),
 "p1": p("Poproszę rachunek. Zapłacę kartą.", "fin1"),
 "fin1": fin("Oczywiście. Dziękuję za wizytę i do zobaczenia!"),
 "fin2": fin("Zapraszamy ponownie!")}))

ALL.append(S("lingaria_pociag_bilet_a2", "Bilet na pociąg", "Kupujesz bilet na pociąg w kasie. Wybierasz godzinę i rodzaj biletu, płacisz, a potem opowiadasz, po co jedziesz, i pytasz o peron.",
 "A2", "fi-rr-train", "auto:feminine", "Kasjerka", "Ty", ["bilet", "pociąg", "peron", "odjazd", "powrotny", "w jedną stronę", "kasa", "stacja"], ["bilet", "peron"],
 ["a2", "pociag", "podroz", "bilet", "dworzec", "peron"], "op1", {
 "op1": op("Stoisz w kolejce w kasie biletowej. Chcesz kupić bilet na pociąg do innego miasta. Kasjerka patrzy na ciebie życzliwie.", "a1"),
 "a1": a("Dzień dobry! Dokąd jedziemy?", "u1"),
 "u1": u("Powiedz, dokąd chcesz jechać", "Dzień dobry. Poproszę bilet do {miasto}.", "Przepraszam, dokąd?", "s1"),
 "s1": q("Do {miasto|tego miasta}? Mam pociąg o dziewiątej i o dwunastej. Który wybierasz?", "Wybierz godzinę odjazdu", "Przepraszam, o dziewiątej czy o dwunastej?",
   ("dziewiata", "Poproszę ten o dziewiątej.", "s2"), ("dwunasta", "Poproszę ten o dwunastej.", "s2"), ("pozniej", "Czy jest coś później?", "a2"), ("kosmos", "Czy pociąg jedzie przez kosmos?", "a3", True)),
 "a2": a("Ostatni pociąg odjeżdża o dwudziestej.", "u2"),
 "u2": u("Powiedz, że bierzesz ten o dwudziestej", "W takim razie poproszę ten o dwudziestej.", "Przepraszam, który pociąg?", "s2"),
 "a3": a("Niestety nie, tylko przez pola i lasy.", "s2"),
 "s2": q("W jedną stronę czy powrotny?", "Powiedz, jaki bilet chcesz", "Przepraszam, w jedną stronę czy powrotny?",
   ("jedna", "W jedną stronę, proszę.", "a4"), ("powrotny", "Poproszę bilet powrotny.", "a4"), ("dziecko", "Poproszę też bilet dla dziecka.", "a4")),
 "a4": a("Dobrze. Razem dwadzieścia pięć euro.", "s3"),
 "s3": q("Płacisz kartą czy gotówką?", "Powiedz, jak płacisz", "Przepraszam, kartą czy gotówką?",
   ("karta", "Kartą, proszę.", "a5"), ("gotowka", "Gotówką, proszę.", "a5"), ("brak", "Przepraszam, nie mam przy sobie portfela.", "a6")),
 "a6": a("Rozumiem. Bankomat jest przy wejściu. Poczekam na ciebie.", "fin2"),
 "a5": a("Dziękuję. Oto bilet. Pociąg odjeżdża z peronu trzeciego. Dużo osób jedzie dziś do {miasto|tego miasta}. Po co tam jedziesz?", "sw1"),
 "sw1": sw("Powiedz, po co jedziesz", "po co jedziesz i na jak długo, 2 zdania", "Jadę odwiedzić babcię. Zostanę tam na trzy dni.", "Przepraszam, pytałam, po co jedziesz.", "op2"),
 "op2": op("Wskazówka: na bilecie szukaj numeru peronu i godziny odjazdu. To dwie informacje, bez których pociąg ci ucieknie.", "p1", True),
 "p1": p("Przepraszam, z którego peronu odjeżdża pociąg?", "fin1"),
 "fin1": fin("Z peronu trzeciego, schodami w dół. Szczęśliwej podróży!"),
 "fin2": fin("Do zobaczenia! Zdążysz jeszcze na pociąg.")}))

ALL.append(S("lingaria_lekarz_bol_gardla_b1", "U lekarza: ból gardła", "Idziesz do lekarki z bólem gardła. Opisujesz objawy, odpowiadasz na pytania o gorączkę i alergię, a potem ustalasz, jak będziesz odpoczywać.",
 "B1", "fi-rr-stethoscope", "auto:feminine", "Lekarka", "Ty", ["gardło", "gorączka", "kaszel", "recepta", "alergia", "objawy", "tabletki", "odpoczynek"], ["gorączka", "recepta"],
 ["b1", "lekarz", "zdrowie", "objawy", "choroba", "przychodnia"], "op1", {
 "op1": op("Od trzech dni boli cię gardło i masz katar. Idziesz do przychodni. Lekarka zaprasza cię do gabinetu.", "s1"),
 "s1": q("Dzień dobry, proszę usiąść. Co się dzieje?", "Opisz, co cię boli", "Przepraszam, co dokładnie cię boli?",
   ("gardlo", "Od trzech dni boli mnie gardło i mam katar.", "a1"), ("glowa", "Boli mnie głowa i czuję się bardzo słabo.", "a1"), ("kaszel", "Mam silny kaszel, zwłaszcza w nocy.", "a1"), ("serce", "Boli mnie serce, bo nikt do mnie nie pisze.", "a2", True)),
 "a2": a("To nie jest choroba, ale rozumiem. Zbadajmy najpierw gardło.", "a1"),
 "a1": a("Rozumiem. Zaraz to sprawdzę. Najpierw zmierzymy temperaturę.", "s2"),
 "s2": q("Czy masz gorączkę?", "Powiedz, czy masz gorączkę", "Przepraszam, masz gorączkę czy nie?",
   ("tak", "Tak, wczoraj termometr pokazał trzydzieści osiem stopni.", "a3"), ("nie", "Nie, temperatura jest normalna.", "a3"), ("niewiem", "Nie wiem, nie mam termometru.", "a4")),
 "a4": a("To nic. Zmierzymy ją tutaj.", "a3"),
 "a3": a("Otwórz szeroko usta. Gardło jest czerwone i spuchnięte.", "u1"),
 "u1": u("Zapytaj, czy to coś poważnego", "Czy to coś poważnego?", "Słucham?", "a5"),
 "a5": a("Nie, to zwykłe zapalenie gardła. Muszę jeszcze o coś zapytać.", "s3"),
 "s3": q("Czy masz alergię na jakieś leki?", "Powiedz, czy masz alergię na leki", "Przepraszam, czy masz alergię na leki?",
   ("nie", "Nie, nie mam alergii na leki.", "a6"), ("penicylina", "Tak, mam alergię na penicylinę.", "a7"), ("wole", "Wolę nie brać żadnych leków.", "a8")),
 "a7": a("Dziękuję. W takim razie przepiszę inny lek, bez penicyliny.", "a6"),
 "a8": a("Rozumiem. Zalecam wtedy odpoczynek i dużo płynów. Jeśli gorączka wróci, przyjdź ponownie.", "fin2"),
 "a6": a("Wypiszę ci receptę na tabletki do ssania i syrop. Przez trzy dni musisz odpoczywać i pić dużo ciepłych napojów. Czy możesz zostać w domu?", "sw1"),
 "sw1": sw("Powiedz, czy możesz odpoczywać w domu", "czy możesz zostać w domu i jak to zorganizujesz, 2 lub 3 zdania", "Mogę pracować z domu przez trzy dni, a sąsiad zrobi mi zakupy.", "Przepraszam, pytałam, czy możesz odpoczywać w domu.", "op2"),
 "op2": op("Wskazówka: opisując objawy, podaj dwie rzeczy: co cię boli i od kiedy. Lekarz zawsze zapyta o jedno i drugie.", "p1", True),
 "p1": p("Ile razy dziennie mam brać ten lek?", "fin1"),
 "fin1": fin("Trzy razy dziennie po posiłku. Szybkiego powrotu do zdrowia!"),
 "fin2": fin("Dbaj o siebie i wracaj do zdrowia!")}))

ALL.append(S("lingaria_rozmowa_o_prace_b1", "Rozmowa o pracę", "Masz rozmowę kwalifikacyjną. Opowiadasz o swoim doświadczeniu i znajomości języków, ustalasz, kiedy możesz zacząć, i opisujesz swój największy sukces.",
 "B1", "fi-rr-briefcase", "auto:masculine", "Rekruter", "Ty", ["doświadczenie", "stanowisko", "zespół", "umiejętności", "wynagrodzenie", "rozmowa", "kandydat", "umowa"], ["doświadczenie", "zespół"],
 ["b1", "praca", "rozmowa", "kariera", "doswiadczenie", "cv"], "op1", {
 "op1": op("Siedzisz w sali konferencyjnej. Masz rozmowę o pracę w średniej firmie. Naprzeciwko siedzi rekruter z twoim CV w ręku.", "a1"),
 "a1": a("Dzień dobry i dziękuję za spotkanie. Mam przed sobą twoje CV.", "s1"),
 "s1": q("Opowiedz mi krótko o sobie. Czym zajmujesz się obecnie?", "Powiedz, czym zajmujesz się zawodowo", "Przepraszam, czym zajmujesz się na co dzień?",
   ("praca", "Pracuję jako {zawod} od trzech lat.", "a2"), ("studia", "Jestem po studiach i szukam pierwszej pracy.", "a3"), ("zmiana", "Chcę zmienić branżę, bo szukam nowych wyzwań.", "a10"), ("szachy", "Moim największym doświadczeniem jest gra w szachy.", "a9", True)),
 "a2": a("Praca jako {zawod|specjalista} to dobre doświadczenie. Co najbardziej lubisz w swojej pracy?", "u1"),
 "u1": u("Powiedz, co lubisz w swojej pracy", "Najbardziej lubię pracę w zespole i rozwiązywanie problemów.", "Przepraszam, co lubisz w pracy?", "s2"),
 "a3": a("Każdy zaczyna od pierwszej pracy. Mamy program stażowy dla osób po studiach.", "s2"),
 "a10": a("Zmiana branży wymaga odwagi. Cenimy takie nastawienie.", "s2"),
 "a9": a("Szachy uczą planowania. To przydatna umiejętność w naszej firmie.", "s2"),
 "s2": q("Pracujemy z klientami z różnych krajów. W jakim stopniu znasz języki obce?", "Opisz swoją znajomość języków", "Przepraszam, jakie języki znasz?",
   ("dobrze", "Dobrze znam angielski i uczę się kolejnego języka.", "a4"), ("srednio", "Znam angielski na poziomie komunikatywnym.", "a4"), ("poczatek", "Dopiero zaczynam, ale szybko się uczę.", "a4")),
 "a4": a("Dziękuję za odpowiedź. Teraz kwestia organizacyjna.", "s3"),
 "s3": q("Od kiedy możesz zacząć pracę?", "Powiedz, od kiedy możesz zacząć", "Przepraszam, od kiedy możesz zacząć?",
   ("tydzien", "Mogę zacząć od przyszłego tygodnia.", "a5"), ("miesiac", "Potrzebuję miesiąca okresu wypowiedzenia.", "a5"), ("pomysle", "Chcę to jeszcze przemyśleć.", "a6")),
 "a6": a("Rozumiem. Poczekamy na twoją odpowiedź do piątku.", "fin2"),
 "a5": a("Dobrze. A teraz opowiedz o swoim największym sukcesie w pracy lub w nauce.", "sw1"),
 "sw1": sw("Opowiedz o swoim największym sukcesie", "jaki to był sukces, co zrobiono i jaki był wynik, 3 zdania", "W zeszłym roku przygotowaliśmy w zespole nowy system zamówień. Dzięki niemu skróciliśmy czas obsługi klienta o połowę.", "Przepraszam, pytałem o twój największy sukces.", "op2"),
 "op2": op("Wskazówka: opowiadając o sukcesie, podaj trzy rzeczy: co zrobiono, jak i z jakim wynikiem. To prosty plan dobrej odpowiedzi na rozmowie.", "p1", True),
 "p1": p("Chętnie dołączę do waszego zespołu.", "fin1"),
 "fin1": fin("Dziękujemy za rozmowę. Odezwiemy się w ciągu tygodnia."),
 "fin2": fin("Dziękujemy za spotkanie i do usłyszenia!")}))

ALL.append(S("lingaria_wynajem_mieszkania_b2", "Wynajem mieszkania", "Oglądasz mieszkanie do wynajęcia i negocjujesz z właścicielem czynsz, kaucję i okres wypowiedzenia. Na koniec tłumaczysz, dlaczego wybierasz właśnie tę okolicę.",
 "B2", "fi-rr-home", "auto:masculine", "Właściciel", "Ty", ["wynajem", "kaucja", "umowa", "czynsz", "rachunki", "właściciel", "umeblowane", "wypowiedzenie"], ["kaucja", "czynsz"],
 ["b2", "mieszkanie", "wynajem", "umowa", "kaucja", "negocjacje"], "op1", {
 "op1": op("Oglądasz mieszkanie do wynajęcia. Jest jasne, na trzecim piętrze, z balkonem. Właściciel oprowadza cię po pokojach i czeka na twoje pytania.", "s1"),
 "s1": q("Jak widzisz, mieszkanie jest umeblowane i świeżo odmalowane. Czynsz wynosi osiemset euro miesięcznie. Co o tym sądzisz?", "Zareaguj na cenę i zapytaj o szczegóły", "Przepraszam, nie zrozumiałem. Co sądzisz o cenie?",
   ("ok", "Cena jest w porządku. Czy w tej kwocie są wliczone rachunki?", "a1"), ("drogo", "To trochę za dużo jak na mój budżet. Czy możemy negocjować?", "a2"), ("kuchnia", "Najpierw chcę zobaczyć kuchnię i łazienkę.", "a3"), ("sprzatanie", "Czy w cenie jest codzienne sprzątanie przez pana?", "a4", True)),
 "a1": a("Rachunki za prąd i internet płacisz osobno. Czynsz obejmuje tylko wodę i ogrzewanie.", "u1"),
 "u1": u("Zapytaj o kaucję", "A jaka jest wysokość kaucji i kiedy ją zwracacie?", "Słucham? O co pytasz?", "s2"),
 "a2": a("Mogę zejść do siedmiuset pięćdziesięciu euro, jeśli podpiszesz umowę na rok.", "s2"),
 "a3": a("Proszę bardzo. Kuchnia jest nowa, a w łazience stoi pralka.", "s2"),
 "a4": a("Niestety nie, ale mogę polecić dobrą firmę sprzątającą.", "s2"),
 "s2": q("Kaucja to dwa miesięczne czynsze i zwracam ją po wyprowadzce, jeśli mieszkanie jest w dobrym stanie. Umowa jest na rok z trzymiesięcznym okresem wypowiedzenia. Czy te warunki ci odpowiadają?", "Powiedz, czy akceptujesz warunki umowy", "Przepraszam, czy akceptujesz warunki umowy?",
   ("tak", "Tak, warunki mi odpowiadają. Kiedy mogę się wprowadzić?", "a5"), ("wypowiedzenie", "Okres wypowiedzenia jest dla mnie za długi. Czy da się go skrócić?", "a6"), ("przemysle", "Muszę to jeszcze przemyśleć i skonsultować.", "a7")),
 "a6": a("Mogę skrócić go do dwóch miesięcy, ale nie mniej.", "u2"),
 "u2": u("Przyjmij propozycję właściciela", "Dwa miesiące to dla mnie dobre rozwiązanie. Zgadzam się.", "Przepraszam, zgadzasz się?", "a5"),
 "a5": a("Możesz wprowadzić się od pierwszego dnia przyszłego miesiąca. Umowę podpiszemy w piątek. A tak z ciekawości: dlaczego szukasz mieszkania właśnie w tej okolicy?", "sw1"),
 "a7": a("Oczywiście, to ważna decyzja. Daj mi znać do końca tygodnia.", "fin2"),
 "sw1": sw("Opowiedz, dlaczego wybierasz tę okolicę", "powody wyboru okolicy, jeden argument i jeden przykład, 2 lub 3 zdania", "Wybieram tę okolicę, bo mieszkam blisko pracy, a w pobliżu jest duży park, w którym mogę biegać.", "Przepraszam, pytałem, dlaczego wybierasz właśnie tę okolicę.", "op2"),
 "op2": op("Wskazówka: przy negocjacjach używaj łagodnych form, na przykład „Czy da się to zmienić?” albo „Czy moglibyśmy to ustalić inaczej?”. Brzmi to uprzejmiej niż polecenie.", "p1", True),
 "p1": p("Czy mogę zobaczyć projekt umowy przed podpisaniem?", "fin1"),
 "fin1": fin("Oczywiście, wyślę ci ją mailem jeszcze dziś. Do zobaczenia w piątek!"),
 "fin2": fin("Dziękuję za wizytę. Jeśli mieszkanie ci się spodoba, odezwij się do końca tygodnia.")}))

def uklad(d):
    w = d['wezly']; succ = {i: ([b['dalej'] for b in n['galezie']] if n.get('galezie') else ([n['dalej']] if n.get('dalej') else [])) for i, n in w.items()}
    depth = {d['start']: 0}; order = [d['start']]
    for i in order:
        for t in succ[i]:
            if t in w and t not in depth: depth[t] = depth[i] + 1; order.append(t)
    rows = {}
    for i in order: rows.setdefault(depth[i], []).append(i)
    out = {}
    for dd, ids in rows.items():
        for k, i in enumerate(ids): out[i] = {"x": int(k * 280 - (len(ids) - 1) * 140), "y": dd * 170}
    return out
for s in ALL: s['drzewo']['uklad'] = uklad(s['drzewo'])
if __name__ == '__main__':
    base = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(base, 'out'); os.makedirs(f'{out}/scenariusze', exist_ok=True); os.makedirs(f'{out}/drzewa', exist_ok=True)
    for s in ALL:
        json.dump(s, open(f'{out}/scenariusze/{s["klucz"]}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        json.dump(s['drzewo'], open(f'{out}/drzewa/{s["klucz"]}.drzewo.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(len(ALL), 'scenariuszy zapisanych w', out)
