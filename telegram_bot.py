
import os
import requests


TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_alert(message):

    print("TOKEN EXISTS:", bool(TOKEN), flush=True)
    print("CHAT ID:", CHAT_ID, flush=True)

    if not TOKEN:
        print("ERROR: TELEGRAM_TOKEN missing", flush=True)
        return

    if not CHAT_ID:
        print("ERROR: TELEGRAM_CHAT_ID missing", flush=True)
        return


    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }


    try:

        response = requests.post(
            url,
            data=data,
            timeout=10
        )

        print(
            "TELEGRAM RESPONSE:",
            response.text,
            flush=True
        )


    except Exception as e:

        print(
            "TELEGRAM ERROR:",
            e,
            flush=True
        )
