"""Buduje SPIS.md z nagłówków artykułów. Uruchom: python3 zbuduj_spis.py  (z katalogu narzedzia)"""
import json, re, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
spec = {x['slug']: x for x in json.load(open(os.path.join(HERE, 'tematy.json')))}
NAMES = {'pl':'polski','en':'angielski','de':'niemiecki','es':'hiszpański','it':'włoski','fr':'francuski','pt':'portugalski','nl':'holenderski','sv':'szwedzki','no':'norweski','da':'duński','fi':'fiński','cs':'czeski','sk':'słowacki','hr':'chorwacki','ro':'rumuński','el':'grecki','tr':'turecki','ru':'rosyjski','uk':'ukraiński','ar':'arabski','hi':'hindi','ja':'japoński','ko':'koreański','zh':'chiński'}
CHECK = {'ar','hi','ja','ko','zh','el','tr','fi'}
def words(body, lang):
    out = []
    for l in body:
        if re.match(r'^:(frazy|koniec|uwaga|cta|cwiczenie\b.*)$', l.strip()) or l.startswith(':::'): continue
        out.append(re.sub(r'[#*`>\[\]()|\-:]', ' ', l))
    t = ' '.join(out)
    if lang in ('ja', 'zh'): return round(len(re.findall(r'[぀-ヿ㐀-鿿]', t)) / 2.2)
    return len([w for w in t.split() if any(c.isalnum() for c in w)])
rows = []
d = os.path.join(ROOT, 'artykuly')
for f in sorted(os.listdir(d)):
    if not f.endswith('.txt'): continue
    slug = f[:-4]; lines = open(os.path.join(d, f), encoding='utf-8').read().split('\n'); i = lines.index('---'); h = {}
    for l in lines[:i]:
        m = re.match(r'^([a-z_]+):\s?(.*)$', l)
        if m: h[m.group(1)] = m.group(2).strip()
    s = spec[slug]; rows.append((s['nr'], slug, h, words(lines[i+1:], h['jezyk_tekstu']), s['fraza_google']))
rows.sort(key=lambda r: r[0])
out = ['# Spis 30 artykułów\n', 'Wszystkie mają `status: szkic` i puste `autor:`. Liczba słów liczona jak w walidatorze (dla japońskiego i chińskiego: znaki podzielone przez 2,2, więc to wartość orientacyjna).\n',
       'Kolumna „Natywna kontrola” = tak, gdy tekst lub język docelowy to arabski, hindi, japoński, koreański, chiński, grecki, turecki albo fiński. Tam zapisy wymowy literami czytelnika są przybliżone i warto je pokazać native speakerowi przed publikacją.\n',
       '| Nr | Plik (slug) | Tytuł | Dział | Poziom | Tekst | Uczy | Słowa | Fraza z Google | Natywna kontrola |', '|---|---|---|---|---|---|---|---|---|---|']
for nr, slug, h, w, fr in rows:
    jt, jd = h['jezyk_tekstu'], h['jezyk_docelowy']
    chk = 'tak' if (jt in CHECK or jd in CHECK) else 'nie'
    out.append(f"| {nr} | `{slug}.txt` | {h['tytul']} | {h['dzial']} | {h['poziom']} | {NAMES[jt]} | {NAMES[jd] if jd else 'metoda (bez języka)'} | {w} | {fr} | {chk} |")
ws = sorted(r[3] for r in rows)
out.append(f"\nŁącznie: {len(rows)} artykułów, od {ws[0]} do {ws[-1]} słów, mediana {ws[len(ws)//2]}.")
open(os.path.join(ROOT, 'SPIS.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(len(rows), ws[0], ws[-1], ws[len(ws)//2])
