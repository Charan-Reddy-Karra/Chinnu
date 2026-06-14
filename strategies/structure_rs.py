from strategies.base import BaseStrategy

from engines.structure.v2_score import \
calculate_structure_score

from engines.rs.score import \
calculate_rs_score


class StrategyV2(BaseStrategy):

    NAME = "Structure + RS"

    STRUCTURE_THRESHOLD = 70

    RS_THRESHOLD = 60

    COOLDOWN = 60

    STOPLOSS = -20

    def should_enter(
        self,
        history,
        benchmark,
    ):

        structure = calculate_structure_score(
            history
        )

        rs = calculate_rs_score(
            history,
            benchmark
        )

        return (
            structure >=
            self.STRUCTURE_THRESHOLD
            and
            rs >=
            self.RS_THRESHOLD
        )
