
from flask import Flask
import threading
import time

from market_data import get_eth_candles
from indicators import add_indicators
from signal_engine import generate_signal
from dashboard_update import update_dashboard
from memory import save_prediction
from telegram_bot import send_alert


app = Flask(__name__)


@app.route("/")
def home():
    return "IMAN TRADING AI ONLINE"


def start_web():
    app.run(host="0.0.0.0", port=10000)


print("🤖 IMAN TRADING AI APPLICATION STARTED", flush=True)


# Start Render web server
threading.Thread(target=start_web).start()


while True:

    print("AI LOOP STARTED", flush=True)

    try:

        print("FETCHING CANDLES...", flush=True)

        df = get_eth_candles()

        print("DATA SIZE:", len(df), flush=True)


        df = add_indicators(df)


        result = generate_signal(df)
        update_dashboard(result)


        price = df.iloc[-1]["close"]


        print("==============================")
        print("ETH/USD PRICE:", price)
        print("SIGNAL:", result["SIGNAL"])
        print("CONFIDENCE:", result["CONFIDENCE"])
        print("REASONS:")

        for r in result["REASONS"]:
            print("-", r)


        message = f"""
🤖 IMAN TRADING AI

📊 PAIR: ETH/USD
⏱ TIMEFRAME: 5M

SIGNAL: {result["SIGNAL"]}

CONFIDENCE: {result["CONFIDENCE"]}%

PRICE: {price}

REASONS:

{chr(10).join(result["REASONS"])}

Next scan in 5 minutes...
"""


        # Send every analysis to Telegram
        send_alert(message)

        print("Telegram alert sent", flush=True)


        print("==============================")
        print("Next scan in 5 minutes...", flush=True)


        time.sleep(300)


    except Exception as e:

        print("ERROR:", e, flush=True)

        time.sleep(60)
