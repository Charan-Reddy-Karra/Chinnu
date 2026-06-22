class TradeLedger:

    def __init__(self):

        self.trades = []

    def add(self, trade):

        self.trades.append(trade)

    def count(self):

        return len(self.trades)

    def winners(self):

        return [
            t
            for t in self.trades
            if t.return_pct > 0
        ]

    def losers(self):

        return [
            t
            for t in self.trades
            if t.return_pct <= 0
        ]

    def total_profit(self):

        return sum(
            t.pnl
            for t in self.trades
        )

    def average_return(self):

        if not self.trades:
            return 0

        return sum(
            t.return_pct
            for t in self.trades
        ) / len(self.trades)
