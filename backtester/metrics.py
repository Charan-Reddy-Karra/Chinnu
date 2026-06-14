import pandas as pd

class Metrics:

    @staticmethod
    def calculate(df):

        wins = (df["future_90d_return"] > 0).sum()
        losses = (df["future_90d_return"] <= 0).sum()

        return {
            "Trades": len(df),
            "Win Rate": round((wins/len(df))*100,2) if len(df) else 0,
            "Average": round(df["future_90d_return"].mean(),2),
            "Median": round(df["future_90d_return"].median(),2),
            "Best": round(df["future_90d_return"].max(),2),
            "Worst": round(df["future_90d_return"].min(),2),
            "StdDev": round(df["future_90d_return"].std(),2),
            "Profit Factor":
                round(
                    df[df.future_90d_return>0].future_90d_return.sum() /
                    abs(df[df.future_90d_return<0].future_90d_return.sum()),
                    2
                ) if losses else 999
        }
