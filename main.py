from flask import Flask
import threading
import time

from market_data import get_eth_candles
from indicators import add_indicators
from signal_engine import generate_signal
from telegram_bot import send_alert


app = Flask(__name__)

latest_result = "Starting IMAN TRADING AI..."


@app.route("/")
def home():
    return f"""
    <html>
    <head>
    <title>IMAN TRADING AI</title>
    <meta http-equiv="refresh" content="60">
    </head>

    <body style="background:#111;color:white;font-family:Arial;padding:20px">

    <h1>🤖 IMAN TRADING AI</h1>

    <h2>ETH/USD 5 Minute Predictor</h2>

    <pre style="
    background:#222;
    padding:20px;
    border-radius:10px;
    font-size:18px;
    color:white;
    ">
{latest_result}
    </pre>

    </body>
    </html>
    """


def start_web():
    app.run(host="0.0.0.0", port=10000)


threading.Thread(target=start_web).start()


print("🤖 IMAN TRADING AI STARTED")


while True:

    try:

        print("FETCHING MARKET DATA...")

        df = get_eth_candles()

        df = add_indicators(df)

        result = generate_signal(df)

        price = df.iloc[-1]["close"]


        message = f"""
🤖 IMAN TRADING AI

📊 PAIR: ETH/USD
⏱ TIMEFRAME: 5M

SIGNAL: {result["SIGNAL"]}

CONFIDENCE: {result["CONFIDENCE"]}%

PRICE: {price}

REASONS:
"""

        for reason in result["REASONS"]:
            message += "\n• " + reason


        message += "\n\nNext scan in 5 minutes..."


        latest_result = message


        print(message)


        # SEND TELEGRAM
        try:
            send_alert(message)
            print("Telegram sent")
        except Exception as e:
            print("Telegram error:", e)



        print("==============================")
        time.sleep(300)


    except Exception as e:

        latest_result = "ERROR: " + str(e)

        print("ERROR:", e)

        time.sleep(60)
