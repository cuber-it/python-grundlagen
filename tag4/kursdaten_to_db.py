import yfinance as yf
import pandas as pd
import sqlite3

wkn = "AAPL"
ticker = yf.Ticker(wkn)
df = ticker.history(period="1y")
df.index = df.index.tz_localize(None)
df.reset_index(inplace=True)  # Index als Spalte für DB

conn = sqlite3.connect("kursdaten.db")
df.to_sql(wkn, conn, if_exists="replace", index=False)
conn.close()
