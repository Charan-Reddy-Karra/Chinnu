import pandas as pd

from database.db import get_connection
from engines.rs.score import calculate_rs_score

conn = get_connection()

stock_df = pd.read_sql_query(
    """
    SELECT *
    FROM daily_prices
    WHERE symbol='RELIANCE'
    ORDER BY trade_date
    """,
    conn
)

benchmark_df = pd.read_sql_query(
    """
    SELECT *
    FROM benchmarks
    ORDER BY trade_date
    """,
    conn
)

score = calculate_rs_score(
    stock_df,
    benchmark_df
)

print("RELIANCE RS:", score)

conn.close()
