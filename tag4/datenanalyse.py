import yfinance as yf
import pandas as pd

df = yf.Ticker("NVDA").history(period="6mo")
df.index = df.index.tz_localize(None)
df = df.reset_index()
df["Date"] = df["Date"].dt.strftime("%d.%m.%Y")
df["WTag"] = pd.to_datetime(df["Date"], dayfirst=True).dt.strftime("%a").str[:2]
df["Mean_High_Low"] = (df["High"] + df["Low"]) / 2
df["Date_raw"] = pd.to_datetime(df["Date"], dayfirst=True)

df["KW"] = df["Date_raw"].dt.isocalendar().week
df["Jahr"] = df["Date_raw"].dt.isocalendar().year

mon = df[df["WTag"] == "Mo"]
fre = df[df["WTag"] == "Fr"]

mon = mon[["Jahr", "KW", "Mean_High_Low"]].rename(columns={"Mean_High_Low": "Kurs_Mo"})
fre = fre[["Jahr", "KW", "Mean_High_Low"]].rename(columns={"Mean_High_Low": "Kurs_Fr"})

merged = pd.merge(mon, fre, on=["Jahr", "KW"])
merged["Diff_abs"] = (merged["Kurs_Fr"] - merged["Kurs_Mo"]).round(2)
merged["Diff_pct"] = ((merged["Diff_abs"] / merged["Kurs_Mo"]) * 100).round(2)

# Ausgabe pro Woche
print(merged[["Jahr", "KW", "Kurs_Mo", "Kurs_Fr", "Diff_abs", "Diff_pct"]])

# Gesamtsumme
sum_abs = merged["Diff_abs"].sum().round(2)
sum_pct = ((merged["Kurs_Fr"].sum() - merged["Kurs_Mo"].sum()) / merged["Kurs_Mo"].sum() * 100).round(2)

print(f"\nGesamtgewinn/Verlust: {sum_abs} USD")
print(f"Gesamtperformance: {sum_pct} %")
