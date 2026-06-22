import os

# -----------------------------
# DATABASE
# -----------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE_PATH = os.path.join(
    BASE_DIR,
    "database",
    "data",
    "chinnu.db"
)

# -----------------------------
# MARKET
# -----------------------------

UNIVERSE_MIN_MARKET_CAP = 500  # Crores

LOOKBACK_DAYS = 500

TOP_PICKS = 10

# -----------------------------
# SCORING
# -----------------------------

TREND_WEIGHT = 20
STRUCTURE_WEIGHT = 20
RS_WEIGHT = 20
BREAKOUT_WEIGHT = 15
VOLUME_WEIGHT = 10
SECTOR_WEIGHT = 10
RISK_REWARD_WEIGHT = 5

TOTAL_SCORE = 100

# -----------------------------
# INDICATORS
# -----------------------------

EMA_FAST = 20
EMA_MID = 50
EMA_SLOW = 200

RSI_PERIOD = 14
ATR_PERIOD = 14
ADX_PERIOD = 14

VOLUME_PERIOD = 20

# -----------------------------
# TELEGRAM
# -----------------------------

TELEGRAM_TOKEN = ""

TELEGRAM_CHAT_ID = ""

# -----------------------------
# GEMINI
# -----------------------------

GEMINI_API_KEY = ""

GEMINI_MODEL = "gemini-2.5-flash"

# -----------------------------
# BACKTEST
# -----------------------------

BACKTEST_HOLD_DAYS = 90

STOP_LOSS_PERCENT = 8

TARGET_PERCENT = 25

# -----------------------------
# SCHEDULER
# -----------------------------

RUN_TIME = "17:00"
