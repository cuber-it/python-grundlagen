import yfinance as yf
import pandas as pd

wkn = "AAPL"
ticker = yf.Ticker(wkn)
df = ticker.history(period="1y")  # z. B. 1 Jahr
df.index = df.index.tz_localize(None)


with pd.ExcelWriter("kursdaten.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name=wkn)
