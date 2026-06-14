from strategies.structure_rs import StrategyV2
from backtester.execution import ExecutionEngine

engine = ExecutionEngine(
    StrategyV2()
)

engine.summary()
