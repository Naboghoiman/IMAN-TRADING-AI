from flask import Flask
import threading
import time

from market_data import get_eth_candles
from indicators import add_indicators
from signal_engine import generate_signal


app = Flask(__name__)


@app.route("/")
def home():
    return "IMAN TRADING AI ONLINE"


def start_web():
    app.run(host="0.0.0.0", port=10000)


print("🤖 IMAN TRADING AI APPLICATION STARTED")
print("✅ IMAN TRADING AI ONLINE")


# Start Render web server
threading.Thread(target=start_web).start()


while True:
    try:
        df = get_eth_candles()

        df = add_indicators(df)

        result = generate_signal(df)

        price = df.iloc[-1]["close"]

        print("==========================")
        print("ETH/USD PRICE:", price)
        print("SIGNAL:", result["SIGNAL"])
        print("CONFIDENCE:", result["CONFIDENCE"])
        print("REASONS:")

        for r in result["REASONS"]:
            print("-", r)

        print("==========================")
        print("Next scan in 5 minutes...")

        time.sleep(300)

    except Exception as e:
        print("ERROR:", e)
        time.sleep(60)
        
