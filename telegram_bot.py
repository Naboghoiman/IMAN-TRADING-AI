# IMAN TRADING AI TELEGRAM BOT

import os
import requests
import telebot

TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = telebot.TeleBot(TOKEN)

CHAT_ID_FILE = "chat_id.txt"


@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id

    with open(CHAT_ID_FILE, "w") as f:
        f.write(str(chat_id))

    bot.send_message(
        chat_id,
        "✅ IMAN TRADING AI connected successfully.\n\n"
        f"Your Chat ID is: {chat_id}"
    )

    print("CHAT ID SAVED:", chat_id)


def send_alert(message):
    try:
        if not os.path.exists(CHAT_ID_FILE):
            print("NO CHAT ID FOUND")
            return

        with open(CHAT_ID_FILE, "r") as f:
            chat_id = f.read().strip()

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

        data = {
            "chat_id": chat_id,
            "text": message
        }

        response = requests.post(url, data=data)

        print("TELEGRAM RESPONSE:", response.text)

    except Exception as e:
        print("TELEGRAM ERROR:", e)


print("TELEGRAM BOT RUNNING")

bot.infinity_polling()
