import requests
import pandas as pd


def get_eth_candles():
    """
    Get live ETH 5-minute candles from Binance
    """

    url = "https://api.binance.com/api/v3/klines"

    params = {
        "symbol": "ETHUSDT",
        "interval": "5m",
        "limit": 100
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        data = response.json()

        if not isinstance(data, list):
            print("BINANCE ERROR:", data)
            return pd.DataFrame()

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

        # Convert numbers
        columns = [
            "open",
            "high",
            "low",
            "close",
            "volume"
        ]

        for col in columns:
            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

        # Convert timestamp
        df["time"] = pd.to_datetime(
            df["time"],
            unit="ms"
        )

        df = df.dropna()

        print(
            "BINANCE CANDLES LOADED:",
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
            "BINANCE DATA ERROR:",
            e
        )

        return pd.DataFrame()
