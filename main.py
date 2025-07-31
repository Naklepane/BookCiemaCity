import requests
import datetime

# Konfiguracja seansu i miejsca
MOVIE_START = "2025-06-08 14:00:00"
PRESENTATION_ID = 771554
VENUE_ID = 154
X_COORD = "2"
Y_COORD = "1"
UUID = "7f61dbfe-c2c2-42d6-544c-dca20a704f05"

# Ciasteczka z przeglądarki (pełne, skopiowane z DevTools)
HARDCODED_COOKIES = {
    "_fbp": "fb.1.1749226139804.542859923742457346",
    "_tt_enable_cookie": "1",
    "_ttp": "01JX301C7ZTNSHN3H2YH8AD0Q2_.tt.1",
    "OptanonAlertBoxClosed": "2025-06-06T16:09:03.532Z",
    "_gcl_au": "1.1.1407077903.1749226144",
    "_ga": "GA1.1.762822235.1749226140",
    "ttcsid_CSBNA0RC77U5IJO1Q7M0": "1749226139909::BjB95uDQM6IwD8YrGS78.1.1749226542801",
    "ttcsid": "1749226139909::5jwi3jhxi4_gKGAK0xEH.1.1749226542801",
    "session": "s%3ArrCKvi6zh4Ydsj4GkPxmajq8hdmfezIs.qDt23VLch12fFHTMeroEZ%2FFMjeRXdPUrjGibfutTbT4",
    "uuid": UUID,
    "__cf_bm": "Gz7MZK7hTi5iHpKEmuE97aw_DiPe7013ggK53GD3Vmg-1749237100-1.0.1.1-6Jum7GSd2jDG6inEDfosFNXIugx_PHQwAK4gQU..STFXW05TrBsSOHp4KYaxtobYyWZkKFBu..T9tae67o7p564WESgigWKLodzlTmBPJlk"
}

def lambda_handler(event=None, context=None):
    now = datetime.datetime.now()
    movie_start = datetime.datetime.strptime(MOVIE_START, "%Y-%m-%d %H:%M:%S")

    if now >= movie_start:
        print(f"Film już się zaczął ({movie_start}), bez locka.")
        return {"status": "skipped", "reason": "movie started"}

    payload = {
        "seat": {
            "PresentationId": PRESENTATION_ID,
            "VenueId": VENUE_ID,
            "VenueSeatplanId": 1,
            "VenueSectionId": "1",
            "TicketGroupId": 1,
            "XCoordinate": X_COORD,
            "YCoordinate": Y_COORD
        }
    }

    headers = {
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "origin": "https://tickets.cinema-city.pl",
        "referer": f"https://tickets.cinema-city.pl/order/{PRESENTATION_ID}?lang=pl",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
        "uuid": UUID
    }

    try:
        response = requests.put(
            "https://tickets.cinema-city.pl/api/seats/lock-seat",
            headers=headers,
            cookies=HARDCODED_COOKIES,
            json=payload
        )

        print(f"[{now}] Status: {response.status_code}")
        print(response.text)

        return {
            "status": "lock_sent" if response.status_code == 200 else "failed",
            "http_status": response.status_code,
            "response": response.text
        }

    except Exception as e:
        print(f"Błąd: {e}")
        return {"status": "error", "error": str(e)}

# Lokalny test
if __name__ == "__main__":
    lambda_handler()
