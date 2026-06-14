from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "database" / "data" / "chinnu.db"

MIN_MARKET_CAP = 500  # crore

MIN_DAILY_VALUE_TRADED = 5  # crore

TOP_RANKS_TO_SEND = 20

LOOKBACK_DAYS = 252

STRUCTURE_WEIGHT = 0.45
RS_WEIGHT = 0.20
QUALITY_WEIGHT = 0.15
SPONSORSHIP_WEIGHT = 0.10
RISK_WEIGHT = 0.10
