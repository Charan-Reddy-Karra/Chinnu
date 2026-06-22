import pandas as pd
import ta


def calculate_indicators(df):

    df = df.copy()

    df["ema20"] = ta.trend.ema_indicator(
        df["Close"],
        window=20
    )

    df["ema50"] = ta.trend.ema_indicator(
        df["Close"],
        window=50
    )

    df["ema200"] = ta.trend.ema_indicator(
        df["Close"],
        window=200
    )

    df["rsi"] = ta.momentum.rsi(
        df["Close"],
        window=14
    )

    df["atr"] = ta.volatility.average_true_range(
        df["High"],
        df["Low"],
        df["Close"],
        window=14
    )

    df["adx"] = ta.trend.adx(
        df["High"],
        df["Low"],
        df["Close"],
        window=14
    )

    df["avg_volume"] = (
        df["Volume"]
        .rolling(20)
        .mean()
    )

    df["volume_ratio"] = (
        df["Volume"] /
        df["avg_volume"]
    )

    df["high_52w"] = (
        df["High"]
        .rolling(252)
        .max()
    )

    df["low_52w"] = (
        df["Low"]
        .rolling(252)
        .min()
    )

    df["distance_from_high"] = (
        (df["Close"] - df["high_52w"])
        / df["high_52w"]
        * 100
    )

    df["distance_from_low"] = (
        (df["Close"] - df["low_52w"])
        / df["low_52w"]
        * 100
    )

    return df
