from database.db import get_connection

conn = get_connection()

tables = conn.execute(
    """
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    ORDER BY name
    """
).fetchall()

print("\nCHINNU DB TEST\n")

for row in tables:
    print(row["name"])

conn.close()
