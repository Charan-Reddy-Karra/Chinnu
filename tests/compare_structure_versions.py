import pandas as pd

from database.db import get_connection

from engines.structure.v1.score import \
calculate_structure_score as v1

from engines.structure.v2_score import \
calculate_structure_score as v2

conn = get_connection()

symbols = conn.execute(
    """
    SELECT DISTINCT symbol
    FROM daily_prices
    """
).fetchall()

print()

for row in symbols:

    symbol = row["symbol"]

    df = pd.read_sql_query(
        """
        SELECT *
        FROM daily_prices
        WHERE symbol=?
        ORDER BY trade_date
        """,
        conn,
        params=(symbol,)
    )

    s1 = v1(df)
    s2 = v2(df)

    print(
        f"{symbol:15}"
        f"V1={s1:>6}"
        f" V2={s2:>6}"
    )

conn.close()
