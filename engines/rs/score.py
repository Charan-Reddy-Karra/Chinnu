import pandas as pd


def calculate_rs_score(stock_df, benchmark_df):

    if len(stock_df) < 126:
        return 0

    if len(benchmark_df) < 126:
        return 0

    stock_close = stock_df["close"]

    benchmark_close = benchmark_df["close"]

    stock_return = (
        (
            stock_close.iloc[-1]
            / stock_close.iloc[-126]
        ) - 1
    ) * 100

    benchmark_return = (
        (
            benchmark_close.iloc[-1]
            / benchmark_close.iloc[-126]
        ) - 1
    ) * 100

    excess = stock_return - benchmark_return

    score = 50 + excess

    if score > 100:
        score = 100

    if score < 0:
        score = 0

    return round(score, 2)
