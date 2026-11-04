"""python3 sciezki.py plik_scenariuszy.py [klucz]  -> wypisuje zestaw ścieżek pokrywający każdą gałąź jako czytelną rozmowę."""
import sys, importlib.util, os
spec = importlib.util.spec_from_file_location('sc', sys.argv[1]); m = importlib.util.module_from_spec(spec); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); spec.loader.exec_module(m)
only = sys.argv[2] if len(sys.argv) > 2 else None
def succ(n):
    if n.get('galezie'): return [(b['dalej'], b) for b in n['galezie']]
    return [(n['dalej'], None)] if n.get('dalej') else []
for s in m.ALL:
    if only and s['klucz'] != only: continue
    w = s['drzewo']['wezly']; paths = []
    def dfs(i, trail, seen):
        n = w[i]; trail = trail + [(i, None)] if not trail or True else trail
        nx = succ(n)
        if not nx: paths.append(list(trail)); return
        for t, b in nx:
            if t in seen: continue
            dfs(t, trail + ([(f'{i}>{t}', b)] if b else []), seen | {t})
    dfs(s['drzewo']['start'], [], {s['drzewo']['start']})
    edges = lambda p: {x[0] for x in p if '>' in x[0]} | {f'{a[0]}->{b[0]}' for a, b in zip([y for y in p if '>' not in y[0]], [y for y in p if '>' not in y[0]][1:])}
    chosen, cov = [], set(); allE = set().union(*[edges(p) for p in paths]) if paths else set()
    while cov != allE:
        best = max(paths, key=lambda p: len(edges(p) - cov))
        if not edges(best) - cov: break
        chosen.append(best); cov |= edges(best)
    print('=' * 100); print(f"{s['klucz']}  [{s['cefr']}, głos {s['glos'].split(':')[1]}]  ścieżek ogółem {len(paths)}, pokazanych {len(chosen)}")
    for k, p in enumerate(chosen, 1):
        print(f'--- ścieżka {k}')
        for i, b in p:
            if '>' in i:
                print(f"    TY{' (ukryta)' if b.get('ukryta') else ''}: {b['wzor']}"); continue
            n = w[i]
            if n.get('koniec'): print(f"  [KONIEC {i}] {n['tekst']}")
            elif n.get('opis'): print(f"  [OPIS{' dla ucznia' if n.get('jezyk_ucznia') else ''}] {n['tekst']}")
            elif n.get('kto') == 'ai': print(f"  BOT {i}: {n['tekst']}")
            elif n.get('swobodna'): print(f"  [ODPOWIEDŹ SWOBODNA {i}] zadanie: {n['instrukcja']} | przykład: {n.get('wzor','')}")
            elif n.get('na_pamiec'): print(f"  [NA PAMIĘĆ {i}] TY: {n['wzor']}")
            else: print(f"  [UCZEŃ {i}] zadanie: {n['instrukcja']} | TY: {n['wzor']}")
