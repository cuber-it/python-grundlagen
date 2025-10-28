"""
Erstelle ein einfaches digitales Tagebuch, das Einträge in einer Textdatei speichert und anzeigen kann!
Das Programm soll:
Ein Menü mit folgenden Optionen anbieten:

1 Neuen Tagebuch-Eintrag schreiben
2 Alle Einträge anzeigen
3 Programm beenden

Beim Schreiben wird automatisch das aktuelle Datum und die Uhrzeit hinzugefügt.

Datei öffnen - lesen / schreiben - anhängend
Schleife mit Benutzereingabe
Mehrere Verzweigungen

Optional: Uhrzeit im 24-Stunden-Format anzeigen mit einbauen und zu beginn der Zeile beim speichern mit ausgeben
"""
import datetime

dateiname = input("Dateiname: ")

while True:
    print("\nTagebuch Menü:")
    print("1. Neuen Tagebuch-Eintrag schreiben")
    print("2. Alle Einträge anzeigen")
    print("3. Programm beenden")

    auswahl = input("Bitte eine Option wählen (1-3): ")

    if auswahl == "3":
        print("Programm wird beendet.")
        break
    elif auswahl == "1":
        eintrag = input("Dein Tagebuch-Eintrag:")
        jetzt = datetime.datetime.now()
        zeitstempel = jetzt.strftime("%Y-%m-%d %H:%M:%S")

        try:
            with open(dateiname, "a") as datei:
                datei.write(f"{zeitstempel} - {eintrag}\n")
            print("Eintrag gespeichert.")
        except Exception as e:
            print(f"Fehler beim Speichern des Eintrags: {e}")
    elif auswahl == "2":
        try:
            with open(dateiname, "r") as datei:
                inhalt = datei.read()
                print("\n--- Tagebuch Einträge ---")
                print(inhalt)
                print("-------------------------")
        except FileNotFoundError:
            print("Keine Einträge gefunden. Die Datei existiert nicht.")
    else:
        print("Ungültige Auswahl. Bitte wähle eine Option von 1 bis 3." )
