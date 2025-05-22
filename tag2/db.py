import sqlite3

# Verbindung zur DB (Datei wird angelegt, falls nicht vorhanden)
conn = sqlite3.connect("beispiel.db")
cur = conn.cursor()

# Tabelle anlegen (wenn nicht existiert)
cur.execute("""
CREATE TABLE IF NOT EXISTS kunden (
    id INTEGER PRIMARY KEY,
    name TEXT,
    land TEXT
)
""")

# Daten einfügen
cur.execute("INSERT INTO kunden (name, land) VALUES (?, ?)", ("Max", "DE"))
cur.execute("INSERT INTO kunden (name, land) VALUES (?, ?)", ("Anna", "AT"))
conn.commit()

# Daten abfragen
cur.execute("SELECT * FROM kunden")
for row in cur.fetchall():
    print(row)

# Verbindung schließen
conn.close()

