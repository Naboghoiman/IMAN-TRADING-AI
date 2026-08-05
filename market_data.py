
import requests
import pandas as pd
import time

def get_eth_candles():
    url = "https://api.binance.com/api/v3/klines"

    params = {
        "symbol": "ETHUSDT",
        "interval": "5m",
        "limit": 100
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        df = pd.DataFrame(data, columns=[
            "time",
            "open",
            "high",
            "low",
            "close",
            "volume",
            "close_time",
            "quote_volume",
            "trades",
            "taker_buy_base",
            "taker_buy_quote",
            "ignore"
        ])

        df["open"] = df["open"].astype(float)
        df["high"] = df["high"].astype(float)
        df["low"] = df["low"].astype(float)
        df["close"] = df["close"].astype(float)
        df["volume"] = df["volume"].astype(float)

        df["time"] = pd.to_datetime(
            df["time"],
            unit="ms"
        )

        return df[[
            "time",
            "open",
            "high",
            "low",
            "close",
            "volume"
        ]]

    except Exception as e:
        print("BINANCE DATA ERROR:", e)
        return pd.DataFrame()
