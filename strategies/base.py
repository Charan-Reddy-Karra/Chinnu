from abc import ABC, abstractmethod


class BaseStrategy(ABC):

    NAME = "Base"

    STRUCTURE_THRESHOLD = 0
    RS_THRESHOLD = 0
    COOLDOWN = 0
    STOPLOSS = 0

    @abstractmethod
    def should_enter(
        self,
        history,
        benchmark,
    ):
        pass

    def should_exit(
        self,
        position,
        current_bar,
    ):

        stop_price = (
            position.entry_price *
            (
                1 +
                self.STOPLOSS /
                100
            )
        )

        if (
            current_bar["low"]
            <= stop_price
        ):
            return True

        return False
