from flask import Flask
import threading
import time

from market_data import get_eth_candles
from indicators import add_indicators
from signal_engine import generate_signal


app = Flask(__name__)


latest_result = "Starting IMAN TRADING AI..."


@app.route("/")
def home():
    return f"""
    <html>
    <head>
    <title>IMAN TRADING AI</title>
    <meta http-equiv="refresh" content="10">
    </head>

    <body style="background:#111;color:white;font-family:Arial;padding:25px">

    <h1>🤖 IMAN TRADING AI</h1>

    <h2>Live ETH/USD Predictor</h2>

    <pre style="
    background:#222;
    padding:20px;
    border-radius:10px;
    font-size:18px;
    white-space:pre-wrap;
    ">
{latest_result}
    </pre>

    </body>
    </html>
    """


def start_web():
    app.run(host="0.0.0.0", port=10000)


print("🤖 IMAN TRADING AI STARTED")


threading.Thread(target=start_web).start()


while True:

    try:

        df = get_eth_candles()

        df = add_indicators(df)

        result = generate_signal(df)


        price = df.iloc[-1]["close"]


        reasons = "\n".join(
            ["• " + r for r in result["REASONS"]]
        )


        latest_result = f"""

🤖 IMAN TRADING AI

PAIR:
ETH/USD

TIMEFRAME:
5 MINUTES

━━━━━━━━━━━━━━━━

SIGNAL:
{result["SIGNAL"]}

CONFIDENCE:
{result["CONFIDENCE"]}%

CURRENT PRICE:
{price}

━━━━━━━━━━━━━━━━

ANALYSIS:

{reasons}


━━━━━━━━━━━━━━━━

NEXT SCAN:
5 MINUTES

"""


        print(latest_result, flush=True)


    except Exception as e:

        latest_result = f"""
⚠️ ERROR

{e}

Retrying...
"""

        print(e, flush=True)


    time.sleep(300)
