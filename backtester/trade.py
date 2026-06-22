from dataclasses import dataclass


@dataclass
class Trade:

    symbol: str

    entry_date: str

    exit_date: str

    entry_price: float

    exit_price: float

    quantity: int

    pnl: float

    return_pct: float

    exit_reason: str
