from backtester.portfolio import Portfolio

p = Portfolio()

p.buy(
    "RELIANCE",
    "2025-01-01",
    1500,
    -20
)

p.buy(
    "SBIN",
    "2025-01-05",
    800,
    -20
)

p.summary()

p.sell(
    "RELIANCE",
    1650,
    "2025-04-01"
)

p.summary()
