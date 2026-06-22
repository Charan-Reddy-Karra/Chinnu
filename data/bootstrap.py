import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "data" / "chinnu.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

tables = cursor.execute(
    """
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    ORDER BY name
    """
).fetchall()

print("\nCHINNU DATABASE\n")

for table in tables:
    print(table[0])

conn.close()
