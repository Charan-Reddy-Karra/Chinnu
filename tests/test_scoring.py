import yfinance as yf

from scanner import scan
from scoring.score import calculate_score

df = yf.download(
    "RELIANCE.NS",
    period="2y",
    progress=False,
    auto_adjust=False
)

if hasattr(df.columns, "nlevels") and df.columns.nlevels > 1:
    df.columns = df.columns.get_level_values(0)

signal = scan(df)

score = calculate_score(signal)

print(signal)
print()
print("SCORE =", score)
