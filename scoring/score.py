def calculate_score(scan):

    score = 0

    if scan["trend"]:
        score += 20

    if scan["breakout"]:
        score += 15

    if scan["volume"]:
        score += 10

    if scan["rsi"] >= 55:
        score += 10
    elif scan["rsi"] >= 45:
        score += 5

    if scan["adx"] >= 25:
        score += 10
    elif scan["adx"] >= 20:
        score += 5

    if scan["distance_from_high"] >= -5:
        score += 15
    elif scan["distance_from_high"] >= -10:
        score += 10
    elif scan["distance_from_high"] >= -20:
        score += 5

    if scan["distance_from_low"] >= 20:
        score += 10
    elif scan["distance_from_low"] >= 10:
        score += 5

    return min(score, 100)
