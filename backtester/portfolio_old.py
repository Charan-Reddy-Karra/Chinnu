from dataclasses import dataclass


@dataclass
class Position:
    symbol: str
    entry_date: str
    entry_price: float
    quantity: int
    invested: float
    stop_loss: float


class Portfolio:

    def __init__(
        self,
        initial_capital=500000,
        max_positions=10,
        risk_per_trade=0.02
    ):

        self.initial_capital = initial_capital
        self.cash = initial_capital

        self.max_positions = max_positions
        self.risk_per_trade = risk_per_trade

        self.positions = {}

        self.closed = []

    def has_position(self, symbol):
        return symbol in self.positions

    def free_slots(self):
        return self.max_positions - len(self.positions)

    def can_enter(self, symbol):

        if self.has_position(symbol):
            return False

        if self.free_slots() <= 0:
            return False

        return True

    def calculate_position_size(
        self,
        entry_price,
        stop_percent
    ):

        risk_amount = (
            self.cash *
            self.risk_per_trade
        )

        risk_per_share = (
            entry_price *
            abs(stop_percent) /
            100
        )

        qty = int(
            risk_amount /
            risk_per_share
        )

        if qty <= 0:
            return 0

        affordable = int(
            self.cash /
            entry_price
        )

        return min(
            qty,
            affordable
        )

    def buy(
        self,
        symbol,
        date,
        entry_price,
        stop_percent
    ):

        if not self.can_enter(symbol):
            return False

        qty = self.calculate_position_size(
            entry_price,
            stop_percent
        )

        if qty <= 0:
            return False

        invested = qty * entry_price

        self.cash -= invested

        self.positions[symbol] = Position(
            symbol=symbol,
            entry_date=date,
            entry_price=entry_price,
            quantity=qty,
            invested=invested,
            stop_loss=entry_price * (
                1 + stop_percent / 100
            )
        )

        return True
    def sell(
        self,
        symbol,
        exit_price,
        exit_date
    ):

        if symbol not in self.positions:
            return

        p = self.positions.pop(symbol)

        proceeds = p.quantity * exit_price

        pnl = proceeds - p.invested

        self.cash += proceeds

        self.closed.append(
            {
                "symbol": symbol,
                "entry_date": p.entry_date,
                "exit_date": exit_date,
                "entry": p.entry_price,
                "exit": exit_price,
                "qty": p.quantity,
                "pnl": pnl,
                "return_pct": (
                    (exit_price / p.entry_price) - 1
                ) * 100
            }
        )

    def equity(self):

        invested = sum(
            p.invested
            for p in self.positions.values()
        )

        return self.cash + invested

    def summary(self):

        print()

        print("=" * 40)

        print(
            "Initial Capital:",
            round(self.initial_capital, 2)
        )

        print(
            "Cash:",
            round(self.cash, 2)
        )

        print(
            "Open Positions:",
            len(self.positions)
        )

        print(
            "Closed Trades:",
            len(self.closed)
        )

        print(
            "Equity:",
            round(self.equity(), 2)
        )

        print("=" * 40)
