import pandas as pd

from engines.structure.score import calculate_structure_score

df = pd.read_sql_query(
    """
    SELECT *
    FROM daily_prices
    WHERE symbol='RELIANCE'
    ORDER BY trade_date
    """,
    __import__("sqlite3").connect(
        "database/data/chinnu.db"
    )
)

score = calculate_structure_score(df)

print("\nCHINNU STRUCTURE TEST\n")
print("RELIANCE SCORE:", score)
