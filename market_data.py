
import MetaTrader5 as mt5
import pandas as pd


def get_eth_candles():

    symbol = "ETHUSD"

    if not mt5.initialize():
        print("MT5 CONNECTION FAILED")
        return pd.DataFrame()

    rates = mt5.copy_rates_from_pos(
        symbol,
        mt5.TIMEFRAME_M5,
        0,
        100
    )

    if rates is None:
        print("NO EXNESS DATA")
        return pd.DataFrame()

    df = pd.DataFrame(rates)

    df["time"] = pd.to_datetime(df["time"], unit="s")

    df.rename(
        columns={
            "open": "open",
            "high": "high",
            "low": "low",
            "close": "close",
            "tick_volume": "volume"
        },
        inplace=True
    )

    return df
