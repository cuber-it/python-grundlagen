import yfinance as yf
import sqlite3
from datetime import datetime

# Aktuelles Datum
heute = datetime.today().strftime('%Y-%m-%d')

# Daten abrufen (inkl. 'Adj Close')
df = yf.download("AMZN", start="2000-01-01", end=heute, auto_adjust=False)

if df.empty:
    print("Keine Daten abgerufen.")
else:
    conn = sqlite3.connect("meine_datenbank.db")
    cursor = conn.cursor()

    # Tabelle anlegen (falls noch nicht vorhanden)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS amazon_kurse (
            datum TEXT PRIMARY KEY,
            open REAL,
            high REAL,
            low REAL,
            close REAL,
            adj_close REAL,
            volume INTEGER
        )
    """)

    # DataFrame vorbereiten
    df.reset_index(inplace=True)
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
    df.rename(columns={
        'Date': 'datum',
        'Open': 'open',
        'High': 'high',
        'Low': 'low',
        'Close': 'close',
        'Adj Close': 'adj_close',
        'Volume': 'volume'
    }, inplace=True)

    # Daten einfügen
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT OR REPLACE INTO amazon_kurse (datum, open, high, low, close, adj_close, volume)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            row['datum'],
            row['open'],
            row['high'],
            row['low'],
            row['close'],
            row['adj_close'],
            row['volume']
        ))

    conn.commit()
    conn.close()
    print("Daten erfolgreich gespeichert.")
