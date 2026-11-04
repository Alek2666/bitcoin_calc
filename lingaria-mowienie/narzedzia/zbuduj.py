"""Runner: python3 zbuduj.py plik_scenariuszy.py  -> buduje JSON-y, waliduje (reguły Lingarii + brak zmiennych + płeć)."""
import sys, os, re, json, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import waliduj, dsl
GEN = re.compile(r'\b\w+(łem|łam|łeś|łaś|łbym|łabym|łbyś|łabyś)\b', re.I)
PART = re.compile(r'\b(zadowolony|zadowolona|zmęczony|zmęczona|gotowy|gotowa|pewien|pewna|głodny|głodna|szczęśliwy|szczęśliwa|uczulony|uczulona|spóźniony|spóźniona|zajęty|zajęta|dumny|dumna|nowy sąsiad|nowa sąsiadka|turysta|turystka|klient|klientka|pasażer|pasażerka|pacjent|pacjentka)\b', re.I)
def texts(n):
    ai = n.get('kto') == 'ai'
    for f in ('tekst', 'blad', 'instrukcja', 'wzor', 'kryteria'):
        if n.get(f): yield f, n[f], ai
    for b in n.get('galezie', []): yield 'galaz.wzor', b['wzor'], False
def extra(s):
    E, W = [], []; g = s['glos'].split(':')[1]; w = s['drzewo']['wezly']
    for i, n in w.items():
        for f, t, ai in texts(n):
            if '{' in t or '}' in t: E.append(f'{i}.{f}: zmienna {{...}} niedozwolona')
            student_line = (f in ('wzor', 'galaz.wzor')) and n.get('kto') != 'ai' or f == 'galaz.wzor'
            if student_line:
                for m in list(GEN.finditer(t)) + list(PART.finditer(t)): W.append(f'{i}.{f}: forma zależna od płci ucznia "{m.group(0)}" w "{t[:60]}"')
            if n.get('kto') == 'ai' and f in ('tekst', 'blad'):
                bad = re.findall(r'\b\w+(?:łem|łbym)\b', t) if g == 'feminine' else re.findall(r'\b\w+(?:łam|łabym)\b', t)
                for x in bad: E.append(f'{i}.{f}: rodzaj bota niezgodny z głosem {g}: "{x}"')
            if n.get('kto') == 'uczen' and f == 'blad':
                bad = re.findall(r'\b\w+(?:łem|łbym)\b', t) if g == 'feminine' else re.findall(r'\b\w+(?:łam|łabym)\b', t)
                for x in bad: E.append(f'{i}.blad: rodzaj bota niezgodny z głosem {g}: "{x}"')
    return E, W
if __name__ == '__main__':
    path = sys.argv[1]; spec = importlib.util.spec_from_file_location('sc', path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    out = os.path.join(HERE, 'wynik'); os.makedirs(out, exist_ok=True); bad = 0; keys = set()
    for s in m.ALL:
        s['drzewo']['uklad'] = dsl.uklad(s['drzewo'])
        E = waliduj.dane(s); Et, Wt, _ = waliduj.tree(s['drzewo'], lingaria=True); E += Et; Ee, We = extra(s); E += Ee; Wt += We
        if s['klucz'] in keys: E.append('powtórzony klucz')
        keys.add(s['klucz']); ok = not E
        print(('OK   ' if ok and not Wt else 'BLAD ' if E else 'UWAGA'), s['klucz'], f'(błędów {len(E)}, ostrzeżeń {len(Wt)})')
        for x in E: print('   błąd:', x)
        for x in Wt: print('   ostrz.:', x)
        if ok: json.dump(s, open(os.path.join(out, s['klucz'] + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        bad += not ok
    print(f'{len(m.ALL)} scenariuszy, z błędami: {bad}'); sys.exit(1 if bad else 0)
