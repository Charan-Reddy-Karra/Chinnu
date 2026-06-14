import pandas as pd

from database.db import get_connection

URL = "https://archives.nseindia.com/content/equities/EQUITY_L.csv"

df = pd.read_csv(URL)

conn = get_connection()

inserted = 0

for _, row in df.iterrows():

    symbol = str(row["SYMBOL"]).strip()
    company_name = str(row["NAME OF COMPANY"]).strip()

    conn.execute(
        """
        INSERT OR REPLACE INTO stocks
        (
            symbol,
            exchange,
            company_name
        )
        VALUES (?, ?, ?)
        """,
        (
            symbol,
            "NSE",
            company_name
        )
    )

    inserted += 1

conn.commit()
conn.close()

print(f"Inserted: {inserted}")
