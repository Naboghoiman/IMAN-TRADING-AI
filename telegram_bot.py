# IMAN TRADING AI TELEGRAM ALERT

import requests


TOKEN = "PUT_YOUR_BOT_TOKEN_HERE"
CHAT_ID = "PUT_YOUR_CHAT_ID_HERE"


def send_alert(message):

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, data=data)

    print("Telegram alert sent")
