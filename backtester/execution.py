from backtester.portfolio import Portfolio


class ExecutionEngine:

    def __init__(
        self,
        strategy,
        capital=500000,
    ):

        self.strategy = strategy

        self.portfolio = Portfolio(
            initial_capital=capital
        )

        self.last_signal = {}

    def in_cooldown(
        self,
        symbol,
        index,
    ):

        if symbol not in self.last_signal:
            return False

        return (
            index -
            self.last_signal[symbol]
        ) < self.strategy.COOLDOWN

    def record_signal(
        self,
        symbol,
        index,
    ):

        self.last_signal[symbol] = index

    def try_enter(
        self,
        symbol,
        index,
        history,
        benchmark,
    ):

        if self.in_cooldown(
            symbol,
            index,
        ):
            return False

        if not self.strategy.should_enter(
            history,
            benchmark,
        ):
            return False

        row = history.iloc[-1]

        ok = self.portfolio.buy(

            symbol,

            str(
                row["trade_date"]
            ),

            float(
                row["close"]
            ),

            self.strategy.STOPLOSS
        )

        if ok:

            self.record_signal(
                symbol,
                index,
            )

        return ok

    def try_exit(
        self,
        symbol,
        bar,
    ):

        if not self.portfolio.has_position(
            symbol
        ):
            return

        position = self.portfolio.positions[
            symbol
        ]

        if self.strategy.should_exit(
            position,
            bar,
        ):

            self.portfolio.sell(

                symbol,

                position.stop_loss,

                str(
                    bar["trade_date"]
                )
            )

    def summary(self):

        self.portfolio.summary()
