#!/usr/bin/env python3
"""
Einfaches Skript zum Abrufen von Wertpapierdaten von Yahoo Finance
und Speichern in einer SQLite-Datenbank.
"""

import sys
import sqlite3
from datetime import datetime
import yfinance as yf


def create_database():
    """Erstellt die SQLite-Datenbank und die Tabelle, falls noch nicht vorhanden."""
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stock_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            current_price REAL,
            open_price REAL,
            high_price REAL,
            low_price REAL,
            volume INTEGER,
            market_cap REAL,
            company_name TEXT
        )
    ''')

    conn.commit()
    conn.close()
    print("✓ Datenbank bereit")


def fetch_stock_data(symbol):
    """Holt Daten von Yahoo Finance für das angegebene Wertpapierkürzel."""
    try:
        stock = yf.Ticker(symbol)
        info = stock.info

        # Daten extrahieren
        data = {
            'symbol': symbol.upper(),
            'timestamp': datetime.now().isoformat(),
            'current_price': info.get('currentPrice') or info.get('regularMarketPrice'),
            'open_price': info.get('open') or info.get('regularMarketOpen'),
            'high_price': info.get('dayHigh') or info.get('regularMarketDayHigh'),
            'low_price': info.get('dayLow') or info.get('regularMarketDayLow'),
            'volume': info.get('volume') or info.get('regularMarketVolume'),
            'market_cap': info.get('marketCap'),
            'company_name': info.get('longName') or info.get('shortName')
        }

        return data

    except Exception as e:
        print(f"❌ Fehler beim Abrufen der Daten: {e}")
        return None


def save_to_database(data):
    """Speichert die Wertpapierdaten in der Datenbank."""
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO stock_data
        (symbol, timestamp, current_price, open_price, high_price, low_price, volume, market_cap, company_name)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data['symbol'],
        data['timestamp'],
        data['current_price'],
        data['open_price'],
        data['high_price'],
        data['low_price'],
        data['volume'],
        data['market_cap'],
        data['company_name']
    ))

    conn.commit()
    conn.close()
    print("✓ Daten in Datenbank gespeichert")


def display_data(data):
    """Zeigt die abgerufenen Daten formatiert an."""
    print("\n" + "=" * 50)
    print(f"Wertpapier: {data['company_name']} ({data['symbol']})")
    print("=" * 50)
    print(f"Aktueller Kurs:  {data['current_price']:.2f}" if data['current_price'] else "Aktueller Kurs:  N/A")
    print(f"Eröffnungskurs:  {data['open_price']:.2f}" if data['open_price'] else "Eröffnungskurs:  N/A")
    print(f"Tageshoch:       {data['high_price']:.2f}" if data['high_price'] else "Tageshoch:       N/A")
    print(f"Tagestief:       {data['low_price']:.2f}" if data['low_price'] else "Tagestief:       N/A")
    print(f"Volumen:         {data['volume']:,}" if data['volume'] else "Volumen:         N/A")
    if data['market_cap']:
        print(f"Marktkapital.:   {data['market_cap']:,.0f}")
    print(f"Zeitstempel:     {data['timestamp']}")
    print("=" * 50 + "\n")


def main():
    """Hauptfunktion des Skripts."""
    # Prüfen ob Wertpapierkürzel angegeben wurde
    if len(sys.argv) < 2:
        print("Usage: python stock_fetcher.py <SYMBOL>")
        print("Beispiel: python stock_fetcher.py AAPL")
        sys.exit(1)

    symbol = sys.argv[1]

    # Datenbank vorbereiten
    create_database()

    # Daten abrufen
    print(f"\n📊 Rufe Daten für {symbol.upper()} ab...")
    data = fetch_stock_data(symbol)

    if data:
        # Daten anzeigen
        display_data(data)

        # In Datenbank speichern
        save_to_database(data)
    else:
        print("❌ Keine Daten abgerufen")
        sys.exit(1)


if __name__ == "__main__":
    main()
