import MetaTrader5 as mt5
import pandas as pd


def connect_exness():

    if not mt5.initialize():
        print("MT5 connection failed")
        return False

    print("EXNESS MT5 CONNECTED")
    return True


def get_eth_candles():

    symbol = "ETHUSD"

    rates = mt5.copy_rates_from_pos(
        symbol,
        mt5.TIMEFRAME_M5,
        0,
        100
    )

    if rates is None:
        print("No Exness data")
        return pd.DataFrame()

    df = pd.DataFrame(rates)

    df["time"] = pd.to_datetime(
        df["time"],
        unit="s"
    )

    return df
