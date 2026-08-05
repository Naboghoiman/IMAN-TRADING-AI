
import requests
import pandas as pd


def get_eth_candles():
    """
    Get ETH 5-minute candles from Coinbase
    """

    url = "https://api.exchange.coinbase.com/products/ETH-USD/candles"

    params = {
        "granularity": 300
    }

    try:
        response = requests.get(
            url,
            params=params,
            headers={
                "User-Agent": "IMAN-Trading-AI"
            },
            timeout=10
        )

        data = response.json()

        if not isinstance(data, list):
            print("COINBASE ERROR:", data)
            return pd.DataFrame()

        df = pd.DataFrame(
            data,
            columns=[
                "time",
                "low",
                "high",
                "open",
                "close",
                "volume"
            ]
        )

        for col in [
            "open",
            "high",
            "low",
            "close",
            "volume"
        ]:
            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

        df["time"] = pd.to_datetime(
            df["time"],
            unit="s"
        )

        df = df.sort_values(
            "time"
        )

        df = df.dropna()

        print(
            "COINBASE CANDLES LOADED:",
            len(df),
            "LAST PRICE:",
            df["close"].iloc[-1]
        )

        return df[
            [
                "time",
                "open",
                "high",
                "low",
                "close",
                "volume"
            ]
        ]


    except Exception as e:
        print(
            "COINBASE DATA ERROR:",
            e
        )
        return pd.DataFrame()
