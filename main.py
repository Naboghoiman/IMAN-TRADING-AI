# IMAN TRADING AI MAIN ENGINE

from data import get_eth_price
from strategy import analyze_signal
import time


print("🤖 IMAN TRADING AI STARTED")


while True:

    try:
        price = get_eth_price()

        # Temporary placeholders
        ema50 = price
        ema200 = price
        rsi = 50
        macd = 0
        macd_signal = 0

        signal, score = analyze_signal(
            price,
            ema50,
            ema200,
            rsi,
            macd,
            macd_signal
        )

        print("----------------------")
        print("ETH/USD:", price)
        print("SIGNAL:", signal)
        print("SCORE:", score)

        print("Next scan in 5 minutes")

        time.sleep(300)

    except Exception as e:
        print("ERROR:", e)
        time.sleep(60)
