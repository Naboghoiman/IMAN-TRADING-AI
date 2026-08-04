def generate_signal(df):

    last = df.iloc[-1]

    buy = 0
    sell = 0
    reasons = []

    # Trend
    if last["close"] > last["EMA200"]:
        buy += 1
        reasons.append("Price above EMA200")
    else:
        sell += 1
        reasons.append("Price below EMA200")

    # EMA50 direction
    if last["close"] > last["EMA50"]:
        buy += 1
        reasons.append("EMA50 bullish")
    else:
        sell += 1
        reasons.append("EMA50 bearish")

    # RSI
    if last["RSI"] < 30:
        buy += 1
        reasons.append("RSI oversold")
    elif last["RSI"] > 70:
        sell += 1
        reasons.append("RSI overbought")

    # MACD
    if last["MACD"] > 0:
        buy += 1
        reasons.append("MACD positive")
    else:
        sell += 1
        reasons.append("MACD negative")


    if buy >= 3:
        signal = "🟢 BUY"
        confidence = buy * 25

    elif sell >= 3:
        signal = "🔴 SELL"
        confidence = sell * 25

    else:
        signal = "⚪ WAIT"
        confidence = max(buy, sell) * 25


    return {
        "SIGNAL": signal,
        "CONFIDENCE": confidence,
        "REASONS": reasons
      }
