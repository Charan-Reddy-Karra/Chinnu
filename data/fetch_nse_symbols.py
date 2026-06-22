import pandas as pd

URL = "https://archives.nseindia.com/content/equities/EQUITY_L.csv"

df = pd.read_csv(URL)

print(df.head())

print("\nRows:", len(df))
