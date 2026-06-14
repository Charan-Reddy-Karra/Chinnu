import pandas as pd


def calculate_structure_score(df):

    if len(df) < 120:
        return 0

    close = df["close"]

    last_price = close.iloc[-1]

    high_20 = close.tail(20).max()
    low_20 = close.tail(20).min()

    high_60 = close.tail(60).max()
    low_60 = close.tail(60).min()

    range20 = (high_20 - low_20) / low_20
    range60 = (high_60 - low_60) / low_60

    score = 0

    # Contraction

    if range20 < range60:
        score += 30

    # Near breakout

    breakout_distance = (
        (high_60 - last_price)
        / high_60
    ) * 100

    if breakout_distance <= 5:
        score += 25

    # Trend quality

    ma50 = close.rolling(50).mean().iloc[-1]
    ma100 = close.rolling(100).mean().iloc[-1]

    if last_price > ma50:
        score += 20

    if ma50 > ma100:
        score += 15

    # Base quality

    closes20 = close.tail(20)

    volatility = closes20.std() / closes20.mean()

    if volatility < 0.05:
        score += 10

    return round(score, 2)
