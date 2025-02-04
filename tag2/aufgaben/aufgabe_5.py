# Aufgabe
#
# Time-Counter
#
# Es wird ein Zeit-Counter gebaut, bei dem ein Benutzer eine Zeit eingeben kann
# in der Form 00:00:00 (Stunden:Minuten:Sekunden)
#
# Nach dem Start läuft der Counter runter und gibt die verstrichene Zeit aus
# und zwar im Sekundentakt
#
# Zielwert: 00:05:15
#
# Ausgabe:
# 00:00:00
# 00:00:01
# ...
# 00:05:15 - Fertig!!
#
# Hinweis:
# - Verwendet eine Schleife
# - Verwendet eine Zeitverzögerung (wait, sleep, ...)
#

import time

# Eingabe der Zielzeit im Format HH:MM:SS
eingabe = input("Gib die Zielzeit ein (HH:MM:SS): ")

try:
    # Aufteilen der Eingabe in Stunden, Minuten und Sekunden
    h, m, s = eingabe.split(":")
    
    # Umwandeln in Ganzzahlen
    stunden = int(h)
    minuten = int(m)
    sekunden = int(s)

    # Berechnung der Gesamtzeit in Sekunden
    gesamt_sekunden = stunden * 3600 + minuten * 60 + sekunden

    # Time-Counter starten
    print("Time-Counter gestartet!")
    aktueller_zaehler = 0

    for aktueller_zaehler in range(gesamt_sekunden + 1):
    # wäre auch ok, aber pythonistas machen es mir for und range: while aktueller_zaehler <= gesamt_sekunden:
        # Berechne Stunden, Minuten und Sekunden
        stunden_aktuell = aktueller_zaehler // 3600
        minuten_aktuell = (aktueller_zaehler % 3600) // 60
        sekunden_aktuell = aktueller_zaehler % 60

        # Formatierte Ausgabe im Stil 00:00:00
        print(f"{stunden_aktuell:02d}:{minuten_aktuell:02d}:{sekunden_aktuell:02d}")

        # Warten für 1 Sekunde
        time.sleep(1)
        #  wird nur bei while benötigt: aktueller_zaehler += 1
    print(f"Fertig: {stunden_aktuell:02d}:{minuten_aktuell:02d}:{sekunden_aktuell:02d}")

except ValueError:
    print("Ungültige Eingabe! Bitte im Format HH:MM:SS eingeben.")