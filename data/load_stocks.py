import sqlite3

from database.db import get_connection


def add_stock(symbol, exchange, company_name):
    conn = get_connection()

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
            exchange,
            company_name,
        ),
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":

    add_stock("RELIANCE", "NSE", "Reliance Industries")
    add_stock("TCS", "NSE", "Tata Consultancy Services")
    add_stock("HDFCBANK", "NSE", "HDFC Bank")

    print("Loaded sample stocks")
