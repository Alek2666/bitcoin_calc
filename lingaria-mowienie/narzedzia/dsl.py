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
