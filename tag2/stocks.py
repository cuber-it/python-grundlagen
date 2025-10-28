import sqlite3
conn = sqlite3.connect('stocks.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM stock_data ORDER BY timestamp DESC LIMIT 10")
print(cursor.fetchall())
