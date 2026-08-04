from flask import Flask
import threading
import time
from datetime import datetime

from market_data import get_eth_candles
from indicators import add_indicators
from signal_engine import generate_signal


app = Flask(__name__)

latest = {
    "signal": "STARTING...",
    "confidence": 0,
    "price": 0,
    "reasons": [],
    "time": "Loading..."
}


@app.route("/")
def dashboard():

    reasons = "<br>".join(
        ["• " + r for r in latest["reasons"]]
    )

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title>IMAN TRADING AI</title>

    <meta http-equiv="refresh" content="10">

    <style>

    body {{
        background:#101010;
        color:white;
        font-family:Arial;
        padding:20px;
    }}

    .box {{
        background:#1e1e1e;
        padding:25px;
        border-radius:15px;
        max-width:500px;
    }}

    .signal {{
        font-size:30px;
        font-weight:bold;
        margin:20px 0;
    }}

    </style>

    </head>

    <body>

    <div class="box">

    <h1>🤖 IMAN TRADING AI</h1>

    <h3>ETH/USD</h3>

    <p>TIMEFRAME: 5 MINUTES</p>

    <hr>

    <div class="signal">
    SIGNAL: {latest["signal"]}
    </div>


    <h2>
    CONFIDENCE:
    {latest["confidence"]}%
    </h2>


    <h3>
    PRICE:
    {latest["price"]}
    </h3>


    <hr>


    <h3>ANALYSIS</h3>

    <p>
    {reasons}
    </p>


    <hr>


    <p>
    LAST UPDATE:
    {latest["time"]}
    </p>


    <p>
    NEXT SCAN:
    5 MINUTES
    </p>


    </div>

    </body>

    </html>
    """


def run_web():

    app.run(
        host="0.0.0.0",
        port=10000
    )


threading.Thread(
    target=run_web
).start()


print("🤖 IMAN TRADING AI DASHBOARD STARTED")


while True:

    try:

        df = get_eth_candles()

        df = add_indicators(df)

        result = generate_signal(df)

        price = df.iloc[-1]["close"]


        latest["signal"] = result["SIGNAL"]

        latest["confidence"] = result["CONFIDENCE"]

        latest["price"] = price

        latest["reasons"] = result["REASONS"]

        latest["time"] = datetime.now().strftime(
            "%H:%M:%S"
        )


        print(
            "SIGNAL:",
            latest["signal"]
        )


    except Exception as e:

        print(
            "ERROR:",
            e
        )


    time.sleep(300)
