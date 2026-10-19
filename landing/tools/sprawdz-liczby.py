#!/usr/bin/env python3
"""Liczy dane do landing page'a z API aplikacji WebCameraSki (to samo źródło, z którego korzysta aplikacja).

Użycie:  python3 tools/sprawdz-liczby.py
Wynik porównaj z liczbami w index.html (sekcja "LICZBY", opisy i FAQ).
"""
import collections
import json
import urllib.request

API = "https://www.webcamera.pl/api/webcameraski_ios_android/data.json.php"

with urllib.request.urlopen(urllib.request.Request(API, headers={"User-Agent": "WebCameraSki-landing-check"}), timeout=60) as r:
    data = json.load(r)

resorts = [r for r in data["stoki"].values() if r.get("active") == "1"]
cams = [c for r in resorts for c in (r.get("cams") or [])]
active_cams = [c for c in cams if str(c.get("disabled")) != "1"]
routes = [t for r in resorts for t in (r.get("trasy") or [])]

def res_ok(c, min_w, min_h):
    try:
        w, h = (int(x) for x in str(c.get("res") or "0x0").split("x"))
    except ValueError:
        return False
    return w >= min_w and h >= min_h

sk = [r for r in resorts if r.get("country") == "Słowacja" or "Słowacja" in (r.get("wojewodztwo") or "")]
print(f"Ośrodki:            {len(resorts)}  (Słowacja: {len(sk)}, Polska: {len(resorts) - len(sk)})")
print(f"Kamery:             {len(cams)}  (aktywne: {len(active_cams)})")
print(f"  min. HD 720p:     {sum(res_ok(c, 1280, 700) for c in cams)}")
print(f"  Full HD i więcej: {sum(res_ok(c, 1920, 1080) for c in cams)}")
print(f"Ośrodki z kamerą:   {sum(1 for r in resorts if r.get('cams'))}")
print(f"Trasy:              {sum(int(r.get('routes_total') or 0) for r in resorts)}")
print(f"Długość tras:       {sum(float(t.get('dlugosc') or 0) for t in routes) / 1000:.0f} km")
print(f"Wyciągi:            {sum(int(r.get('lifts_total') or 0) for r in resorts)}")
print(f"Orczyki / krzesełka / gondole (liczba ośrodków): "
      f"{sum(r.get('has_drag_lift') == '1' for r in resorts)} / {sum(r.get('has_big_lift') == '1' for r in resorts)} / {sum(r.get('has_gondole_lift') == '1' for r in resorts)}")
groups = []
for g in data.get("grupy", {}).values():
    g = g[0] if isinstance(g, list) else g
    groups.append(f"{g.get('nazwa')} ({g.get('osrodkow')})")
print("Ski passy:          " + ", ".join(groups))
print(f"Aktualności:        {len(data.get('articles') or [])}")

# kontrola jakości danych
wrong_country = [r["name"] for r in resorts if "Słowacja" in (r.get("wojewodztwo") or "") and r.get("country") != "Słowacja"]
if wrong_country:
    print("UWAGA, kraj niezgodny z regionem: " + ", ".join(wrong_country))
no_cams = sorted(r["name"] for r in resorts if not r.get("cams"))
print(f"Ośrodki bez kamery ({len(no_cams)}): " + ", ".join(no_cams))
