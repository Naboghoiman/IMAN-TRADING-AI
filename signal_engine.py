def generate_signal(df):

    last = df.iloc[-1]

    buy = 0
    sell = 0
    reasons = []

    # Trend filter EMA200
    if last["close"] > last["EMA200"]:
        buy += 1
        reasons.append("Price above EMA200 trend")
    else:
        sell += 1
        reasons.append("Price below EMA200 trend")


    # EMA50 direction
    if last["close"] > last["EMA50"]:
        buy += 1
        reasons.append("EMA50 bullish")
    else:
        sell += 1
        reasons.append("EMA50 bearish")


    # RSI confirmation
    if 40 < last["RSI"] < 65:
        buy += 1
        reasons.append("RSI supports upward momentum")

    elif 35 < last["RSI"] < 60:
        sell += 1
        reasons.append("RSI supports downward momentum")


    # MACD confirmation
    if last["MACD"] > 0:
        buy += 1
        reasons.append("MACD positive")
    else:
        sell += 1
        reasons.append("MACD negative")


    # Candle confirmation
    if last["close"] > last["open"]:
        buy += 1
        reasons.append("Bullish candle")

    else:
        sell += 1
        reasons.append("Bearish candle")


    # Final decision
    if buy >= 4:
        signal = "🟢 BUY"
        confidence = min(buy * 20, 95)

    elif sell >= 4:
        signal = "🔴 SELL"
        confidence = min(sell * 20, 95)

    else:
        signal = "⚪ WAIT"
        confidence = max(buy, sell) * 15


    return {
        "SIGNAL": signal,
        "CONFIDENCE": confidence,
        "REASONS": reasons
    }
