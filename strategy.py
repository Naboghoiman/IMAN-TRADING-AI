# IMAN TRADING AI STRATEGY ENGINE

def analyze_signal(price, ema50, ema200, rsi, macd, macd_signal):

    score_buy = 0
    score_sell = 0

    # Trend
    if price > ema200 and ema50 > ema200:
        score_buy += 1

    if price < ema200 and ema50 < ema200:
        score_sell += 1

    # RSI
    if rsi < 30:
        score_buy += 1

    if rsi > 70:
        score_sell += 1

    # MACD
    if macd > macd_signal:
        score_buy += 1

    if macd < macd_signal:
        score_sell += 1

    if score_buy >= 2:
        return "BUY", score_buy

    elif score_sell >= 2:
        return "SELL", score_sell

    else:
        return "WAIT", max(score_buy, score_sell)
