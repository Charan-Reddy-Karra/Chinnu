import pandas as pd

from database.db import get_connection
from engines.structure.score import calculate_structure_score
from engines.rs.score import calculate_rs_score

conn = get_connection()

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

results = []

for row in symbols:

    symbol = row["symbol"]

    stock_df = pd.read_sql_query(
        """
        SELECT *
        FROM daily_prices
        WHERE symbol = ?
        ORDER BY trade_date
        """,
        conn,
        params=(symbol,)
    )

    structure_score = calculate_structure_score(stock_df)

    rs_score = calculate_rs_score(
        stock_df,
        benchmark_df
    )

    final_score = round(
        (structure_score * 0.7)
        +
        (rs_score * 0.3),
        2
    )

    results.append(
        {
            "symbol": symbol,
            "structure": structure_score,
            "rs": rs_score,
            "final": final_score
        }
    )

results = sorted(
    results,
    key=lambda x: x["final"],
    reverse=True
)

print("\nCHINNU RANKINGS\n")

print(
    f"{'SYMBOL':15}"
    f"{'STRUCT':>10}"
    f"{'RS':>10}"
    f"{'FINAL':>10}"
)

for r in results[:20]:

    print(
        f"{r['symbol']:15}"
        f"{r['structure']:>10}"
        f"{r['rs']:>10}"
        f"{r['final']:>10}"
    )

conn.close()
