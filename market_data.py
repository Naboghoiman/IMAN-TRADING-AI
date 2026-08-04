import requests
import pandas as pd

def get_eth_candles():
    url = "https://api.binance.com/api/v3/klines"
    
    params = {
        "symbol": "ETHUSDT",
        "interval": "5m",
        "limit": 100
    }

    data = requests.get(url, params=params).json()

    df = pd.DataFrame(data, columns=[
        "time","open","high","low","close",
        "volume","close_time",
        "qav","trades",
        "tb_base","tb_quote","ignore"
    ])

    df["close"] = df["close"].astype(float)
    df["open"] = df["open"].astype(float)
    df["high"] = df["high"].astype(float)
    df["low"] = df["low"].astype(float)

    return df
