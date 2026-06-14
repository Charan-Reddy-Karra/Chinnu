from strategies.registry import STRATEGIES

print(STRATEGIES.keys())

strategy = STRATEGIES["structure_rs"]()

print(strategy.NAME)
