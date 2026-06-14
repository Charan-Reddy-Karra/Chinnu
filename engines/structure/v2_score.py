import pandas as pd

def calculate_structure_score(df):

    if len(df) < 150:
        return 0

    close = df["close"]

    high20 = close.tail(20).max()
    low20 = close.tail(20).min()

    high60 = close.tail(60).max()
    low60 = close.tail(60).min()

    range20 = ((high20 - low20) / low20) * 100
    range60 = ((high60 - low60) / low60) * 100

    score = 0.0

    # Compression
    if range60 > 0:
        compression_ratio = range20 / range60

        if compression_ratio < 0.30:
            score += 35
        elif compression_ratio < 0.50:
            score += 25
        elif compression_ratio < 0.70:
            score += 15

    # Breakout proximity
    current = close.iloc[-1]

    dist = ((high60 - current) / high60) * 100

    if dist <= 2:
        score += 25
    elif dist <= 5:
        score += 15
    elif dist <= 8:
        score += 5

    # Trend
    ma50 = close.rolling(50).mean().iloc[-1]
    ma100 = close.rolling(100).mean().iloc[-1]

    if current > ma50:
        score += 15

    if ma50 > ma100:
        score += 15

    # Tight closes
    recent20 = close.tail(20)

    volatility = (
        recent20.std()
        / recent20.mean()
    ) * 100

    if volatility < 2:
        score += 10
    elif volatility < 4:
        score += 5

    score = min(score, 95)

    return round(score, 2)
