import os
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_alert(message):

    print("TOKEN EXISTS:", bool(TOKEN), flush=True)
    print("CHAT ID:", CHAT_ID, flush=True)

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.post(url, data=data)

    print("TELEGRAM RESPONSE:", response.text, flush=True)
