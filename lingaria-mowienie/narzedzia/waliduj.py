"""Walidator scenariuszy Mówienia wg ściągi z 2026-11-04 (punkty 3-10). To moja reimplementacja reguł, nie kod PHP Lingarii."""
import json, re, sys
ICONS = ['fi-rr-comment','fi-rr-shopping-basket','fi-rr-shopping-cart','fi-rr-coffee','fi-rr-utensils','fi-rr-train','fi-rr-plane','fi-rr-bed','fi-rr-map-marker','fi-rr-briefcase','fi-rr-stethoscope','fi-rr-home','fi-rr-phone-call','fi-rr-graduation-cap','fi-rr-ticket']
ID = re.compile(r'^[a-z0-9_-]+$'); PH = re.compile(r'\{([A-Za-z][A-Za-z0-9_]{0,23})(?:\|([^{}]{1,60}))?\}')
LIM = dict(tekst=300, opis=700, koniec=300, instrukcja=160, blad=200, wzor=200, wzor_sw=400, kryteria=200, role=40, tytul=80, opis_rozmowy=300, slowko=60)
def kind(n):
    if n.get('koniec'): return 'fin'
    if n.get('kto') == 'ai':
        if n.get('opis'): return 'op'
        return 'q' if n.get('galezie') else 'a'
    if n.get('swobodna'): return 'sw'
    if n.get('na_pamiec'): return 'p'
    return 'u'
def tree(d, lingaria=True):
    E, W = [], []
    w = d.get('wezly', {}); start = d.get('start') or (next(iter(w)) if w else None)
    if start not in w: E.append(f'start "{start}" nie istnieje'); return E, W, {}
    kinds = {i: kind(n) for i, n in w.items()}; setters = {}; used = []
    def txt(i, f, s, lim):
        if not isinstance(s, str): E.append(f'{i}.{f}: nie tekst'); return
        if len(s) > lim: E.append(f'{i}.{f}: {len(s)} znaków (limit {lim})')
        if re.search(r'[—–→←⇒]|->| - | -- ', s): E.append(f'{i}.{f}: pauza, półpauza, strzałka lub myślnik')
        if '…' in s or '...' in s: W.append(f'{i}.{f}: wielokropek')
        rest = PH.sub('', s)
        if '{' in rest or '}' in rest: E.append(f'{i}.{f}: błędne miejsce na odpowiedź')
        return [(m.group(1).lower(), m.group(2)) for m in PH.finditer(s)]
    def use(i, f, s, lim):
        ph = txt(i, f, s, lim) or []
        for name, fb in ph:
            used.append((i, f, name, fb))
    for i, n in w.items():
        if not ID.match(i): E.append(f'{i}: zły identyfikator')
        k = kinds[i]; kto = n.get('kto')
        if k == 'fin':
            use(i, 'tekst', n.get('tekst', ''), LIM['koniec'])
            if not n.get('tekst'): E.append(f'{i}: koniec bez tekstu')
        elif k == 'op':
            use(i, 'tekst', n.get('tekst', ''), LIM['opis'])
            if not n.get('tekst'): E.append(f'{i}: opis bez tekstu')
            if not n.get('dalej'): E.append(f'{i}: opis bez dalej')
            if n.get('galezie'): E.append(f'{i}: opis z gałęziami')
        elif k in ('q', 'a'):
            if not n.get('tekst'): E.append(f'{i}: bot nic nie mówi')
            use(i, 'tekst', n.get('tekst', ''), LIM['tekst'])
            if 'blad' in n: use(i, 'blad', n['blad'], LIM['blad'])
            if 'instrukcja' in n: use(i, 'instrukcja', n['instrukcja'], LIM['instrukcja'])
            if k == 'a' and not n.get('dalej'): E.append(f'{i}: bot bez gałęzi, bez dalej i bez końca')
            if k == 'q':
                g = n['galezie']
                if len(g) > 4: E.append(f'{i}: {len(g)} gałęzi (max 4)')
                if not n.get('instrukcja'): W.append(f'{i}: pytanie bez instrukcji')
                if sum(1 for b in g if not b.get('ukryta')) < 2: E.append(f'{i}: mniej niż 2 widoczne odpowiedzi')
                for j, b in enumerate(g):
                    if not b.get('wzor'): E.append(f'{i}.galezie[{j}]: brak wzoru')
                    else:
                        ph = txt(f'{i}.g{j}', 'wzor', b['wzor'], LIM['wzor'])
                        if len(ph or []) > 1: E.append(f'{i}.g{j}: więcej niż jedno miejsce w wzorze')
                        for name, _ in (ph or []): setters.setdefault(name, []).append(i)
                    if not b.get('dalej'): E.append(f'{i}.galezie[{j}]: brak dalej')
                    if b.get('intencja') and not ID.match(b['intencja']): E.append(f'{i}.g{j}: zła intencja')
        else:
            if kto != 'uczen': E.append(f'{i}: zły kto')
            if not n.get('dalej'): E.append(f'{i}: uczeń bez dalej')
            if 'blad' in n: use(i, 'blad', n['blad'], LIM['blad'])
            if 'instrukcja' in n: use(i, 'instrukcja', n['instrukcja'], LIM['instrukcja'])
            if k == 'u':
                if not n.get('instrukcja'): E.append(f'{i}: uczeń bez instrukcji')
                if not n.get('wzor'): E.append(f'{i}: uczeń bez wzoru')
                else:
                    ph = txt(i, 'wzor', n['wzor'], LIM['wzor'])
                    if len(ph or []) > 1: E.append(f'{i}: więcej niż jedno miejsce w wzorze')
                    for name, _ in (ph or []): setters.setdefault(name, []).append(i)
            if k == 'p':
                ph = txt(i, 'wzor', n.get('wzor', ''), LIM['wzor'])
                if not n.get('wzor'): E.append(f'{i}: pamięć bez wzoru')
                if ph: E.append(f'{i}: miejsce {{...}} w zdaniu na pamięć')
            if k == 'sw':
                if not n.get('instrukcja'): E.append(f'{i}: swobodna bez instrukcji')
                for f, lim in (('wzor', LIM['wzor_sw']), ('kryteria', LIM['kryteria'])):
                    if f in n and txt(i, f, n[f], lim): E.append(f'{i}: miejsce {{...}} w odpowiedzi swobodnej ({f})')
    succ = {}
    for i, n in w.items():
        k = kinds[i]
        succ[i] = [b.get('dalej') for b in n.get('galezie', [])] if k == 'q' else ([n['dalej']] if n.get('dalej') and k != 'fin' else [])
        for t in succ[i]:
            if t not in w: E.append(f'{i}: dalej prowadzi do "{t}", którego nie ma')
    seen, st = set(), [start]
    while st:
        x = st.pop()
        if x in seen or x not in w: continue
        seen.add(x); st += succ[x]
    for i in w:
        if i not in seen: E.append(f'{i}: nieosiągalny ze startu')
    if not any(k == 'fin' for k in kinds.values()): E.append('brak klocka końcowego')
    for name in {u[2] for u in used}:
        if name not in setters: E.append(f'miejsce {{{name}}} użyte, ale żaden wzór go nie ustala')
    for i, f, name, fb in used:
        if not fb: W.append(f'{i}.{f}: miejsce {{{name}}} bez zapasu')
    if lingaria:
        need = {'op': 'opis', 'q': 'pytanie', 'a': 'kwestia', 'u': 'uczeń', 'p': 'na pamięć', 'sw': 'swobodna'}
        for k, nm in need.items():
            if k not in kinds.values(): E.append(f'brak klocka: {nm}')
        if sum(1 for k in kinds.values() if k == 'fin') < 2: E.append('mniej niż dwa końce')
        stud = {'u', 'p', 'sw'}
        for i in w:
            for t in succ[i]:
                if t in w and kinds[t] in stud and (kinds[i] in stud or kinds[i] == 'q'): E.append(f'uczeń mówi dwa razy z rzędu: {i} -> {t}')
                if t in w and kinds[t] == 'sw' and kinds[i] != 'a': E.append(f'przed odpowiedzią swobodną {t} stoi {i}, a powinna zwykła kwestia bota')
    return E, W, kinds
def dane(s):
    E = []; g = lambda k: s.get(k)
    if not (g('klucz') and re.match(r'^lingaria_[a-z0-9_-]+$', g('klucz'))): E.append('klucz musi zaczynać się od lingaria_')
    if not g('tytul') or len(g('tytul')) > LIM['tytul']: E.append('tytul pusty lub > 80')
    if not g('opis') or len(g('opis')) > LIM['opis_rozmowy']: E.append('opis pusty lub > 300')
    if g('cefr') not in ('A1','A2','B1','B2','C1','C2'): E.append('zły cefr')
    if g('ikona') not in ICONS: E.append('ikona spoza listy')
    if g('glos') not in ('auto:masculine', 'auto:feminine'): E.append('głos tylko auto:masculine lub auto:feminine')
    r = g('role') or {}
    for k in ('bot', 'uczen'):
        if not r.get(k) or len(r[k]) > LIM['role']: E.append(f'rola {k} pusta lub > 40')
    sl = g('slowka') or []
    if len(sl) < 6: E.append('mniej niż 6 słówek')
    if len(set(sl)) != len(sl) or any(len(x) > LIM['slowko'] for x in sl): E.append('słówka: duplikaty lub > 60 znaków')
    if any(x not in sl for x in (g('luki') or [])): E.append('luki spoza słówek')
    if g('jezyki'): E.append('rozmowy Lingarii bez pola jezyki')
    t = g('tagi') or []
    if not (4 <= len(t) <= 10) or len(set(t)) != len(t) or any(not re.match(r'^[a-z0-9_-]+$', x) for x in t): E.append('tagi: 4-10, małe litery, bez powtórek')
    if t and t[0] != (g('cefr') or '').lower(): E.append('pierwszy tag to poziom małymi literami')
    if g('status') not in ('gotowy', 'szkic'): E.append('zły status')
    return E
if __name__ == '__main__':
    bad = 0; strict = '--lingaria' in sys.argv
    for p in [a for a in sys.argv[1:] if not a.startswith('--')]:
        s = json.load(open(p, encoding='utf-8')); full = 'drzewo' in s
        E = dane(s) if full else []; Et, Wt, _ = tree(s['drzewo'] if full else s, lingaria=full or strict)
        E += Et; print(('OK   ' if not E and not Wt else 'BLAD ' if E else 'UWAGA'), p.split('/')[-1], f'(błędów {len(E)}, ostrzeżeń {len(Wt)})')
        for x in E: print('   błąd:', x)
        for x in Wt: print('   ostrz.:', x)
        bad += bool(E)
    sys.exit(1 if bad else 0)
