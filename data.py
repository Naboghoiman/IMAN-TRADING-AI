# IMAN TRADING AI LIVE DATA

import yfinance as yf


def get_eth_price():

    data = yf.download(
        "ETH-USD",
        period="1d",
        interval="5m"
    )

    latest = data.iloc[-1]

    price = float(latest["Close"])

    return price


if __name__ == "__main__":
    print("ETH/USD PRICE:", get_eth_price())
