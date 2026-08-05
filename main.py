import time
import json
from market_data import get_market_data
from indicators import add_indicators
from signal_engine import generate_signal


def save_signal(signal):
    with open("signals.json", "w") as f:
        json.dump(signal, f, indent=4)


def run():

    print("🤖 IMAN TRADING AI ENGINE STARTED")

    while True:

        try:
            print("FETCHING MARKET DATA...")

            # Get candles
            df = get_market_data()

            if df is None or len(df) == 0:
                print("No market data")
               
