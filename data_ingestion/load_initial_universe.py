from database.db import get_connection

symbols = [
    "RELIANCE",
    "TCS",
    "HDFCBANK",
    "ICICIBANK",
    "INFY",
    "SBIN",
    "BHARTIARTL",
    "LT",
    "ITC",
    "HINDUNILVR",
    "AXISBANK",
    "BAJFINANCE",
    "KOTAKBANK",
    "SUNPHARMA",
    "MARUTI",
    "TITAN",
    "ULTRACEMCO",
    "ASIANPAINT",
    "NTPC",
    "POWERGRID"
]

conn = get_connection()

for s in symbols:
    conn.execute(
        """
        INSERT OR REPLACE INTO universe
        (symbol, priority, active)
        VALUES (?, ?, 1)
        """,
        (s, 1)
    )

conn.commit()
conn.close()

print("Universe loaded:", len(symbols))
