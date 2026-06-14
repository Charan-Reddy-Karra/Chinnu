from database.db import get_connection
from backtester.metrics import Metrics
import pandas as pd

conn = get_connection()

df = pd.read_sql_query(
"""
SELECT *
FROM backtest_results
""",
conn
)

stats = Metrics.calculate(df)

print("\n=========== CHINNU REPORT ===========\n")

for k,v in stats.items():
    print(f"{k:15}: {v}")

print("\n=====================================\n")
