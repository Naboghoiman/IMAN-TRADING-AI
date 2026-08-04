import os
import requests


TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def check_telegram():

    print("Checking Telegram connection...", flush=True)

    if TOKEN:
        print("TOKEN FOUND ✅", flush=True)
    else:
        print("TOKEN MISSING ❌", flush=True)

    if CHAT_ID:
        print("CHAT ID FOUND:", CHAT_ID, flush=True)
    else:
        print("CHAT ID MISSING ❌", flush=True)



def send_alert(message):

    check_telegram()

    if not TOKEN:
        print("Cannot send: TELEGRAM_TOKEN missing", flush=True)
        return False


    if not CHAT_ID:
        print("Cannot send: TELEGRAM_CHAT_ID missing", flush=True)
        return False


    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"


    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }


    try:

        response = requests.post(
            url,
            data=payload,
            timeout=15
        )


        print(
            "Telegram response:",
            response.text,
            flush=True
        )


        if response.status_code == 200:

            print(
                "Telegram message delivered ✅",
                flush=True
            )

            return True

        else:

            print(
                "Telegram sending failed ❌",
                flush=True
            )

            return False


    except Exception as e:

        print(
            "Telegram error:",
            e,
            flush=True
        )

        return False
