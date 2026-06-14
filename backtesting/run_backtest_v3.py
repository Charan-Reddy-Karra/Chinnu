import pandas as pd

from database.db import get_connection
from engines.structure.v2_score import calculate_structure_score
from engines.rs.score import calculate_rs_score

conn = get_connection()

conn.execute("DELETE FROM backtest_results")

benchmark_df = pd.read_sql_query(
    """
    SELECT *
    FROM benchmarks
    ORDER BY trade_date
    """,
    conn
)

symbols = conn.execute(
    """
    SELECT DISTINCT symbol
    FROM daily_prices
    """
).fetchall()

signals = 0

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

    if len(df) < 220:
        continue

    for i in range(150, len(df) - 90):

        history = df.iloc[: i + 1].copy()

        structure = calculate_structure_score(
            history
        )

        rs = calculate_rs_score(
            history,
            benchmark_df.iloc[: i + 1]
        )

        if structure < 60:
            continue

        if rs < 60:
            continue

        entry = float(df.iloc[i]["close"])

        ret30 = (
            (float(df.iloc[i + 30]["close"]) / entry)
            - 1
        ) * 100

        ret60 = (
            (float(df.iloc[i + 60]["close"]) / entry)
            - 1
        ) * 100

        ret90 = (
            (float(df.iloc[i + 90]["close"]) / entry)
            - 1
        ) * 100

        conn.execute(
            """
            INSERT INTO backtest_results
            (
                engine_version,
                symbol,
                entry_date,
                entry_price,
                future_30d_return,
                future_60d_return,
                future_90d_return
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                "structure_rs_v1",
                symbol,
                str(df.iloc[i]["trade_date"]),
                entry,
                round(ret30, 2),
                round(ret60, 2),
                round(ret90, 2)
            )
        )

        signals += 1

conn.commit()

print("Signals:", signals)

summary = pd.read_sql_query(
    """
    SELECT
        AVG(future_30d_return) avg30,
        AVG(future_60d_return) avg60,
        AVG(future_90d_return) avg90
    FROM backtest_results
    """,
    conn
)

print(summary)

conn.close()
