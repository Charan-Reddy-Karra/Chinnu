import pandas as pd
import yfinance as yf

from database.db import get_connection

TICKER = "^NSEI"

df = yf.download(
    TICKER,
    period="2y",
    interval="1d",
    auto_adjust=True,
    progress=False
)

if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)

df = df.reset_index()

conn = get_connection()

inserted = 0

for _, row in df.iterrows():

    conn.execute(
        """
        INSERT OR REPLACE INTO benchmarks
        (
            trade_date,
            close
        )
        VALUES (?, ?)
        """,
        (
            str(row["Date"])[:10],
            float(row["Close"])
        )
    )

    inserted += 1

conn.commit()
conn.close()

print("Inserted:", inserted)
