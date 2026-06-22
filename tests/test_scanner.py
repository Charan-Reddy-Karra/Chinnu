import yfinance as yf

from scanner import scan

df = yf.download(
    "RELIANCE.NS",
    period="2y",
    progress=False,
    auto_adjust=False
)

if hasattr(df.columns, "nlevels") and df.columns.nlevels > 1:
    df.columns = df.columns.get_level_values(0)

result = scan(df)

for k, v in result.items():
    print(f"{k:25} {v}")
