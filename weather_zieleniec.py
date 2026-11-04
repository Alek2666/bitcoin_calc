#!/usr/bin/env python3
"""
Sprawdza aktualną temperaturę w Zieleńcu (lub w dowolnej innej lokalizacji)
przy użyciu API Visual Crossing (Timeline Weather API).

Wymagania: tylko standardowa biblioteka Pythona (3.8+).

Klucz API:
    export VC_API_KEY="twoj_klucz"      # Linux / macOS
    set VC_API_KEY=twoj_klucz           # Windows (cmd)

Użycie:
    python weather_zieleniec.py                      # Zieleniec, Polska
    python weather_zieleniec.py "Zieleniec,PL"       # inna lokalizacja
    python weather_zieleniec.py "52.2297,21.0122"    # współrzędne GPS
"""

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

API_BASE = (
    "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/"
    "services/timeline/"
)
DEFAULT_LOCATION = "Zieleniec,Polska"
TIMEOUT_SECONDS = 15


def fetch_current_weather(location: str, api_key: str) -> dict:
    """Pobiera bieżące warunki pogodowe dla podanej lokalizacji."""
    query = urllib.parse.urlencode(
        {
            "unitGroup": "metric",   # stopnie Celsjusza, km/h, hPa
            "include": "current",    # tylko aktualne warunki
            "elements": "datetime,temp,feelslike,humidity,windspeed,conditions",
            "contentType": "json",
            "key": api_key,
        }
    )
    url = f"{API_BASE}{urllib.parse.quote(location)}?{query}"

    with urllib.request.urlopen(url, timeout=TIMEOUT_SECONDS) as response:
        return json.loads(response.read().decode("utf-8"))


def describe_http_error(error: urllib.error.HTTPError) -> str:
    """Zamienia kod błędu HTTP na czytelny komunikat."""
    body = error.read().decode("utf-8", errors="replace").strip()
    hints = {
        400: "Nieprawidłowa lokalizacja lub parametry zapytania.",
        401: "Nieprawidłowy klucz API (sprawdź zmienną VC_API_KEY).",
        403: "Dostęp zabroniony - klucz może być nieaktywny.",
        429: "Przekroczono limit zapytań dla Twojego konta.",
    }
    hint = hints.get(error.code, "Błąd serwera Visual Crossing.")
    return f"HTTP {error.code}: {hint}\n{body}" if body else f"HTTP {error.code}: {hint}"


def format_report(data: dict) -> str:
    """Buduje czytelny raport z odpowiedzi API."""
    current = data.get("currentConditions")
    if not current:
        raise ValueError("Odpowiedź nie zawiera danych o bieżącej pogodzie.")

    resolved = data.get("resolvedAddress", "nieznana lokalizacja")
    lines = [
        f"Lokalizacja:      {resolved}",
        f"Czas pomiaru:     {current.get('datetime', 'brak danych')}",
        f"Temperatura:      {current.get('temp', 'brak danych')} °C",
        f"Odczuwalna:       {current.get('feelslike', 'brak danych')} °C",
        f"Wilgotność:       {current.get('humidity', 'brak danych')} %",
        f"Wiatr:            {current.get('windspeed', 'brak danych')} km/h",
        f"Warunki:          {current.get('conditions', 'brak danych')}",
    ]
    return "\n".join(lines)


def main() -> int:
    api_key = os.environ.get("VC_API_KEY", "").strip()
    if not api_key:
        print("Brak klucza API. Ustaw zmienną środowiskową VC_API_KEY.", file=sys.stderr)
        return 1

    location = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_LOCATION

    try:
        data = fetch_current_weather(location, api_key)
        print(format_report(data))
        return 0
    except urllib.error.HTTPError as error:
        print(describe_http_error(error), file=sys.stderr)
    except urllib.error.URLError as error:
        print(f"Nie udało się połączyć z API: {error.reason}", file=sys.stderr)
    except (ValueError, KeyError) as error:
        print(f"Nie udało się odczytać odpowiedzi: {error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
