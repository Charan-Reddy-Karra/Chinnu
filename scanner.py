from engines.indicators import calculate_indicators


def scan(df):

    df = calculate_indicators(df)

    latest = df.iloc[-1]

    return {

        "trend": (
            latest["ema20"] >
            latest["ema50"] >
            latest["ema200"]
        ),

        "breakout": (
            latest["Close"] >=
            latest["high_52w"] * 0.98
        ),

        "volume": (
            latest["volume_ratio"] >= 1.5
        ),

        "rsi": latest["rsi"],

        "adx": latest["adx"],

        "atr": latest["atr"],

        "ema20": latest["ema20"],

        "ema50": latest["ema50"],

        "ema200": latest["ema200"],

        "distance_from_high":
            latest["distance_from_high"],

        "distance_from_low":
            latest["distance_from_low"]
    }
