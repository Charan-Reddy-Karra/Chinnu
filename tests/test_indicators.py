import yfinance as yf

from engines.indicators import calculate_indicators

df = yf.download(
    "RELIANCE.NS",
    period="2y",
    auto_adjust=False,
    progress=False
)

# Flatten MultiIndex columns if present
if hasattr(df.columns, "nlevels") and df.columns.nlevels > 1:
    df.columns = df.columns.get_level_values(0)

df = calculate_indicators(df)

print(df.tail(3)[[
    "ema20",
    "ema50",
    "ema200",
    "rsi",
    "atr",
    "adx",
    "volume_ratio"
]])
