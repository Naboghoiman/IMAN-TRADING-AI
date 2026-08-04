import requests
import pandas as pd


def get_eth_candles():

    url = "https://api.kraken.com/0/public/OHLC"

    params = {
        "pair": "ETHUSD",
        "interval": 5
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if "result" not in data:
            print("KRAKEN ERROR:", data)
            return pd.DataFrame()

        result = data["result"]

        pair = [x for x in result.keys() if x != "last"][0]

        candles = result[pair]

        df = pd.DataFrame(
            candles,
            columns=[
                "time",
                "open",
                "high",
                "low",
                "close",
                "vwap",
                "volume",
                "count"
            ]
        )

        df["open"] = df["open"].astype(float)
        df["high"] = df["high"].astype(float)
        df["low"] = df["low"].astype(float)
        df["close"] = df["close"].astype(float)
        df["volume"] = df["volume"].astype(float)

        return df

    except Exception as e:
        print("DATA ERROR:", e)
        return pd.DataFrame()                "vwap",
                "volume",
                "count"
            ]
        )

        df["open"] = df["open"].astype(float)
        df["high"] = df["high"].astype(float)
        df["low"] = df["low"].astype(float)
        df["close"] = df["close"].astype(float)
        df["volume"] = df["volume"].astype(float)

        return df

    except Exception as e:
        print("DATA ERROR:", e)
        return pd.DataFrame()            "tb_base",
            "tb_quote",
            "ignore"
        ]
    )

    df["close"] = df["close"].astype(float)
    df["open"] = df["open"].astype(float)
    df["high"] = df["high"].astype(float)
    df["low"] = df["low"].astype(float)

    return df
