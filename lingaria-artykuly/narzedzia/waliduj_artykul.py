"""Walidator artykułów Lingarii wg przewodnika (czerwone = wstrzymują publikację, żółte = ostrzeżenia).
python3 waliduj_artykul.py KATALOG [tematy.json] [istniejace.json]"""
import sys, os, re, json
import py3langid as langid
CODES = {'pl','en','de','es','it','fr','pt','nl','sv','no','da','fi','cs','sk','hr','ro','el','tr','ru','uk','ar','hi','ja','ko','zh'}
BLOCKS = {'fiszki','quiz','sluchanie','smart-czytanie','film','modal-trigger'}
DATE = '2026-11-04'; SLUG = re.compile(r'^[a-z0-9][a-z0-9-]{0,80}$'); LEVEL = re.compile(r'^(A1|A2|B1|B2|C1)(-(A1|A2|B1|B2|C1))?$')
HEAD_KEYS = ['tytul','opis','data','zaktualizowano','status','dzial','poziom','autor','tagi','powiazane','jezyk_docelowy','jezyk_tekstu']
LANGID_OK = {'no': {'no','nb','nn','da'}, 'da': {'da','no'}, 'hr': {'hr','sr','bs','sl'}, 'cs': {'cs','sk'}, 'sk': {'sk','cs'}, 'zh': {'zh'}, 'uk': {'uk'}, 'nl': {'nl','af'}}
def parse(path):
    raw = open(path, 'rb').read(); E, W = [], []
    if raw.startswith(b'\xef\xbb\xbf'): E.append('BOM')
    if b'\r' in raw: W.append('znaki CR')
    txt = raw.decode('utf-8'); lines = txt.split('\n')
    if '---' not in lines: return None, None, None, ['brak linii --- po nagłówku'], W
    i = lines.index('---'); head = {}; keys_seen = []
    for l in lines[:i]:
        if not l.strip(): continue
        m = re.match(r'^([a-z_]+):\s?(.*)$', l)
        if not m: E.append(f'nagłówek: zła linia "{l[:50]}"'); continue
        k, v = m.group(1), m.group(2).strip(); keys_seen.append(k); head[k] = v
    return head, lines[i + 1:], txt, E, W
def words(body, lang):
    out = []
    for l in body:
        if re.match(r'^:(frazy|koniec|uwaga|cta|cwiczenie\b.*)$', l.strip()) or l.startswith(':::'): continue
        out.append(re.sub(r'[#*`>\[\]()|\-:]', ' ', l))
    t = ' '.join(out)
    if lang in ('ja', 'zh'): return round(len(re.findall(r'[぀-ヿ㐀-鿿]', t)) / 2.2)
    return len([w for w in t.split() if any(ch.isalnum() for ch in w)])
def check(path, spec, pack, existing):
    slug = os.path.basename(path)[:-4]; E, W = [], []
    head, body, txt, e, w = parse(path); E += e; W += w
    if head is None: return E, W, {}
    if not SLUG.match(slug): E.append('zły slug (nazwa pliku)')
    for k in HEAD_KEYS:
        if k not in head: E.append(f'brak pola {k}')
    if head.get('autor', '') != '': E.append('autor musi być puste')
    if head.get('status') != 'szkic': E.append('status musi być szkic')
    if head.get('dzial') not in ('praktyka', 'gramatyka', 'metoda'): E.append('zły dzial')
    for k in ('data', 'zaktualizowano'):
        if head.get(k) != DATE: W.append(f'{k} ma być {DATE}')
    if not LEVEL.match(head.get('poziom', '')): W.append('zły poziom')
    for k in ('jezyk_tekstu', 'jezyk_docelowy'):
        v = head.get(k, '')
        if (k == 'jezyk_tekstu' and v not in CODES) or (v and v not in CODES): E.append(f'zły kod {k}: "{v}"')
    if not head.get('opis'): W.append('brak opisu')
    elif len(head['opis']) > 175: W.append(f'opis {len(head["opis"])} znaków (max 175)')
    if not head.get('tytul'): E.append('brak tytułu')
    tg = [x for x in re.split(r',\s*', head.get('tagi', '')) if x]
    if not 2 <= len(tg) <= 8: W.append('tagi: oczekiwane 3 do 6')
    for r in [x for x in re.split(r',\s*', head.get('powiazane', '')) if x]:
        if r == slug: W.append('powiazane wskazuje samo siebie')
        elif r not in pack and r not in existing: W.append(f'powiazane: nieznany slug {r}')
    if spec:
        for k in ('jezyk_tekstu', 'jezyk_docelowy', 'dzial', 'poziom'):
            if head.get(k, '') != spec[k]: E.append(f'{k} = "{head.get(k)}", oczekiwano "{spec[k]}"')
    # zakazane znaki
    if '—' in txt: E.append('PAUZA (U+2014) w pliku')
    if '·' in txt: E.append('kropka środkowa U+00B7')
    if re.search(r'[→←⇒]|->', txt): E.append('strzałka jako tekst')
    if re.search(r' – ', txt): E.append('półpauza z odstępami (pauza w przebraniu)')
    if re.search(r' -- ', txt): E.append('podwójny łącznik jako pauza')
    if re.search(r'(?<=\S) - (?=\S)', '\n'.join(l for l in txt.split('\n') if not l.lstrip().startswith('- '))): W.append('spacja, łącznik, spacja w środku zdania (pauza w przebraniu?)')
    if re.search(r'</?[a-zA-Z][^>]*>', txt): E.append('HTML w treści')
    if re.search(r'\*\*[^*\n]*\*[^*\n]+\*[^*\n]*\*\*', txt) or '***' in txt: E.append('kursywa wewnątrz pogrubienia')
    # bloki
    ids, modal_ids, quizzes, nfrazy, nfisz, ncta, ncw, nuwaga = [], [], 0, 0, 0, 0, 0, 0; i = 0; prose = []; cta_pos = None
    n = len(body)
    while i < n:
        l = body[i].rstrip(); s = l.strip()
        if s in (':frazy', ':uwaga'):
            j = i + 1; rows = []
            while j < n and body[j].strip() != ':koniec': rows.append(body[j].strip()); j += 1
            if j >= n: E.append(f'blok {s} niezamknięty (brak :koniec)'); break
            rows = [r for r in rows if r]
            if s == ':frazy':
                nfrazy += 1
                for r in rows:
                    p = [x.strip() for x in r.split('|')]
                    if len(p) != 4: E.append(f':frazy wiersz nie ma 4 kolumn: "{r[:50]}"')
                    else:
                        if not p[1]: W.append(f':frazy bez wymowy: "{r[:40]}"')
                        if not p[3]: W.append(f':frazy bez notki: "{r[:40]}"')
                        if p[3] in ('-', '–', '—'): E.append(':frazy notka jako kreska')
                if len(rows) < 6: W.append(f':frazy ma tylko {len(rows)} zwrotów')
            else:
                nuwaga += 1
                if not rows: W.append(':uwaga pusta')
            i = j + 1; continue
        if s == ':cta': ncta += 1; cta_pos = i / max(n, 1); i += 1; continue
        m = re.match(r'^:cwiczenie\s+(\w+)$', s)
        if s.startswith(':cwiczenie'):
            ncw += 1
            if not m or m.group(1) not in ('fiszki', 'tekst', 'sluchanie'): E.append(f'zły znacznik {s}')
            i += 1; continue
        if s.startswith(':::') and s != ':::':
            m = re.match(r'^:::([a-z-]+)(?:\[(.*)\])?$', s)
            if not m: E.append(f'zły wiersz bloku "{s[:50]}"'); i += 1; continue
            name, attrs = m.group(1), m.group(2) or ''
            if name not in BLOCKS: E.append(f'nieznany blok :::{name}'); 
            if name == 'film': W.append('blok film (w tej paczce nie używać)')
            found = re.findall(r'(\w[\w-]*)="([^"]*)"', attrs); rest = re.sub(r'(\w[\w-]*)="([^"]*)"', '', attrs).strip()
            if rest: E.append(f'atrybuty bloku :::{name} poza prostym cudzysłowem: "{attrs[:60]}"')
            ad = dict(found); j = i + 1; rows = []
            while j < n and body[j].strip() != ':::': rows.append(body[j].rstrip()); j += 1
            if j >= n: E.append(f'blok :::{name} niezamknięty'); break
            rows = [r for r in rows if r.strip()]
            if name == 'fiszki':
                nfisz += 1
                for r in rows:
                    p = [x.strip() for x in r.split('|')]
                    if len(p) < 3 or not p[2].startswith('wymowa:'): E.append(f'fiszki: zły wiersz (obcy | tłum | wymowa: … | notka): "{r[:50]}"')
                    elif len(p) < 4 or not p[3]: W.append(f'fiszki bez notki: "{r[:40]}"')
                if len(rows) < 6: W.append(f'fiszki ma tylko {len(rows)} zwrotów')
            elif name == 'quiz':
                quizzes += 1
                if not ad.get('id'): E.append('quiz bez id')
                else: ids.append(ad['id'])
                qs = []; cur = None
                for r in rows:
                    if r.startswith('Pytanie:'): cur = {'q': r, 'opts': [], 'ok': 0, 'wyj': False}; qs.append(cur)
                    elif r.startswith('Wyjaśnienie:'):
                        if cur: cur['wyj'] = True
                    elif r.startswith('- ') and cur is not None:
                        cur['opts'].append(r)
                        if '[correct]' in r: cur['ok'] += 1
                    else: W.append(f'quiz: nierozpoznana linia "{r[:40]}"')
                if not qs: E.append('quiz bez pytań')
                if len(qs) < 3: W.append(f'quiz ma {len(qs)} pytań (zalecane 3)')
                for q in qs:
                    if q['ok'] != 1: E.append(f'quiz: pytanie ma {q["ok"]} odpowiedzi [correct] (musi być 1): "{q["q"][:40]}"')
                    if len(q['opts']) < 2: E.append(f'quiz: pytanie ma {len(q["opts"])} opcji')
                    if not q['wyj']: W.append(f'quiz: brak Wyjaśnienie: przy "{q["q"][:40]}"')
            elif name == 'sluchanie':
                for r in rows:
                    if len([x for x in r.split('|') if x.strip()]) != 2: E.append(f'sluchanie: wiersz nie ma 2 kolumn: "{r[:50]}"')
            elif name == 'smart-czytanie':
                for r in rows:
                    if r.count('[') != r.count(']'): E.append(f'smart-czytanie: niezbalansowane nawiasy "{r[:50]}"')
            elif name == 'modal-trigger':
                for k in ('target', 'id', 'label'):
                    if not ad.get(k): E.append(f'modal-trigger bez {k}')
                if ad.get('id'): modal_ids.append(ad['id'])
            i = j + 1; continue
        if s == ':::': E.append('samotny :::'); i += 1; continue
        if s.startswith(':') and s not in (':koniec',) and re.match(r'^:[a-z]+$', s): E.append(f'nieznany znacznik {s}')
        if s == ':koniec': E.append('samotny :koniec')
        if s and not s.startswith(('#', '>')) and '|' not in s: prose.append(s)
        i += 1
    for m_ in modal_ids:
        if m_ not in ids: E.append(f'modal-trigger wskazuje nieistniejące id "{m_}"')
    if len(set(ids)) != len(ids): E.append('powtórzone id quizu')
    if ncta != 1: W.append(f':cta powinno być dokładnie jedno (jest {ncta})')
    elif not 0.3 <= cta_pos <= 0.7: W.append(f':cta nie w połowie tekstu ({cta_pos:.0%})')
    if ncw > 1: E.append('więcej niż jedno :cwiczenie')
    if ncw and not nfrazy: W.append(':cwiczenie bez :frazy')
    if head.get('jezyk_docelowy') and not (nfrazy or nfisz): E.append('artykuł o języku bez :frazy ani :::fiszki')
    if not head.get('jezyk_docelowy') and (nfrazy or nfisz): W.append('artykuł uniwersalny ma :frazy/:::fiszki')
    if quizzes == 0: W.append('brak quizu')
    if not 1 <= nuwaga <= 3: W.append(f':uwaga razy {nuwaga} (oczekiwane 1 do 3)')
    wc = words(body, head.get('jezyk_tekstu', 'pl'))
    if wc < 600: E.append(f'tylko {wc} słów (twardy próg 600, noindex)')
    if spec and abs(wc - spec['slowa_cel']) > spec['slowa_cel'] * 0.45: W.append(f'długość {wc} słów daleko od celu {spec["slowa_cel"]}')
    if len(re.findall(r'Lingaria', txt)) > 4: W.append('Lingaria wspomniana więcej niż 3 razy')
    if re.search(r'Premium|App Store|Google Play|\bAdSense\b', txt): E.append('niedozwolone twierdzenie o Lingarii (Premium/App Store/Google Play)')
    # język prozy
    tl = head.get('jezyk_tekstu', '')
    ptxt = ' '.join(prose)
    if len(ptxt) > 400 and tl:
        rk = [r[0] for r in langid.rank(ptxt)[:3]]
        if rk[0] != tl and not (tl in LANGID_OK and rk[0] in LANGID_OK[tl] and tl in rk): E.append(f'język prozy wygląda na {rk}, a jezyk_tekstu = {tl}')
    if tl == 'pl' and re.search(r'kluczow\w*|niezwykle ważn\w*|w dzisiejszych czasach|zanurz\w*|odkryj\w*|to nie tylko', txt, re.I): W.append('typowe słowa AI w polskim tekście')
    if tl == 'en' and re.search(r'\b(delve|tapestry|testament|pivotal|vibrant|breathtaking|unlock)\b', txt, re.I): W.append('typowe słowa AI w angielskim tekście')
    return E, W, {'slowa': wc, 'slug': slug, 'tytul': head.get('tytul', '')}
if __name__ == '__main__':
    d = sys.argv[1]; here = os.path.dirname(os.path.abspath(__file__))
    spec = {s['slug']: s for s in json.load(open(sys.argv[2] if len(sys.argv) > 2 else f'{here}/tematy.json', encoding='utf-8'))}
    exist = set(json.load(open(sys.argv[3] if len(sys.argv) > 3 else f'{here}/istniejace.json')))
    files = sorted(f for f in os.listdir(d) if f.endswith('.txt')); pack = {f[:-4] for f in files} | set(spec)
    red = yel = 0; missing = [s for s in spec if s + '.txt' not in files]
    for f in files:
        E, W, info = check(os.path.join(d, f), spec.get(f[:-4]), pack, exist)
        if f[:-4] not in spec: W.append('slug spoza listy tematów')
        tag = 'CZERWONE' if E else ('ŻÓŁTE  ' if W else 'OK      ')
        print(f"{tag} {f[:-4]} ({info.get('slowa', '?')} słów)")
        for x in E: print('    czerwone:', x)
        for x in W: print('    żółte:   ', x)
        red += bool(E); yel += bool(W) and not E
    print(f'\nplików {len(files)}/{len(spec)}, z czerwonymi {red}, tylko z żółtymi {yel}' + (f', BRAKUJE: {missing}' if missing else ''))
    sys.exit(1 if red or missing else 0)
