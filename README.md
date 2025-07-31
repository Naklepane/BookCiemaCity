# 🤖 Bot do Rezerwacji Miejsc w Cinema City

Ten projekt to skrypt działający w AWS Lambda, który automatycznie rezerwuje wybrane miejsca w Cinema City za pomocą requestów do API. Bot działa cyklicznie (co 10 minut) i może utrzymywać miejsce "gorące" (hot) aż do momentu rozpoczęcia seansu.

## 🧠 Funkcjonalność

- Automatyczne wysyłanie zapytań `lock-seat`
- Harmonogram wywołań co 10 minut (AWS EventBridge)
- Możliwość działania z zhardcodowaną sesją/cookies
- Obsługa statusów HTTP i ewentualnych błędów

## ⚙️ Wymagania

- Python 3.9+
- AWS konto z uprawnieniami do uruchamiania Lambdy
- Utworzony EventBridge trigger (cron: `rate(10 minutes)` lub CRON schedule)

## 🎥 Pełna konfiguracja na AWS
Szczegółowy proces konfiguracji projektu jako AWS Lambda z harmonogramem wywołań (EventBridge), wraz z omówieniem działania bota rezerwującego miejsca w Cinema City, znajdziesz w moim filmie na YouTube: https://youtu.be/uT3Ug5lwKdA?si=_KP4m5Ti4guo3xmN

Omowione też zostały tam pewne ograniczenia systemu.
