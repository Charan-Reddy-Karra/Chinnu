import pandas as pd
import yfinance as yf

from database.db import get_connection


def get_universe():

    conn = get_connection()

    rows = conn.execute(
        """
        SELECT symbol
        FROM universe
        WHERE active = 1
        ORDER BY priority
        """
    ).fetchall()

    conn.close()

    return [row["symbol"] for row in rows]


def save_prices(symbol, df):

    conn = get_connection()

    inserted = 0

    for _, row in df.iterrows():

        conn.execute(
            """
            INSERT OR REPLACE INTO daily_prices
            (
                symbol,
                trade_date,
                open,
                high,
                low,
                close,
                volume,
                source
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                symbol,
                str(row["Date"])[:10],
                float(row["Open"]),
                float(row["High"]),
                float(row["Low"]),
                float(row["Close"]),
                int(row["Volume"]),
                "YAHOO"
            )
        )

        inserted += 1

    conn.commit()
    conn.close()

    return inserted


symbols = get_universe()

for symbol in symbols:

    ticker = f"{symbol}.NS"

    print(f"Downloading {ticker}")

    try:

        df = yf.download(
            ticker,
            period="2y",
            interval="1d",
            auto_adjust=True,
            progress=False
        )

        if df.empty:
            print(f"Failed: {ticker}")
            continue

        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        df = df.reset_index()

        inserted = save_prices(symbol, df)

        print(f"{symbol}: {inserted}")

    except Exception as e:

        print(f"{symbol}: ERROR -> {e}")

print("Done")
