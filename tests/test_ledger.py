from backtester.ledger import TradeLedger
from backtester.trade import Trade

ledger = TradeLedger()

ledger.add(
    Trade(
        "ABC",
        "2025-01-01",
        "2025-03-01",
        100,
        120,
        10,
        200,
        20,
        "TARGET"
    )
)

print(ledger.count())
print(ledger.total_profit())
print(ledger.average_return())
