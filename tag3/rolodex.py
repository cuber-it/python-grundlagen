# Adressdatenverwaltung
#
# Der Benutzer soll:
# - Adressen anlegen, ändern und löschen können
# - Adressen suchen können
# - Adressen in einer Datei speichern können
# - Adressen aus einer Datei laden können
# - Adressen in einer Tabelle anzeigen können

# Benutzerdaten sind: Name, Vorname, PLZ, Ort, Strasse
#
# Adresse -> dict(name: ..., vorname: ..., plz: ..., ort: ..., strasse: ...)
# Adressbuch -> list(Adresse, Adresse, Adresse, ...)

import os

kontakte = []
first_time = True
# Das Kommandozeilen-Interface
while True:
    # das hier, damit dieses Return nicht shcon beim allerersten Start kommt
    if not first_time:
        input("Drücken Sie Enter, um fortzufahren...")
    first_time = False
    # Clear screen
    print("\033[H\033[J", end="")  # ANSI escape code to clear the screen
    # Print menu    
    print("===================================")
    print("Willkommen zur Adressdatenverwaltung")
    print("Bitte wählen Sie eine Option:")
    print("1. Adresse anlegen")
    print("2. Adresse ändern")
    print("3. Adresse löschen")
    print("4. Adresse suchen")
    print("5. Adressen speichern")
    print("6. Adressen laden")
    print("7. Adressen anzeigen")
    print("8. Beenden")
    auswahl = input("Ihre Wahl: ")
    if auswahl == "1":
        vorname = input("Vorname: ")
        name = input("Name: ")
        plz = input("PLZ: ")
        ort = input("Ort: ")
        strasse = input("Strasse: ")

        adresse = { 
            "vorname": vorname,
            "name": name,
            "plz": plz,
            "ort": ort,
            "strasse": strasse
        }
        kontakte.append(adresse)
        print(f"Adresse {vorname} {name} wurde angelegt.")
    elif auswahl == "2":
        # Adresse ändern
        pass
    elif auswahl == "3":
        print("Adresse löschen:")
        vorname = input("Vorname: ")
        name = input("Name: ")
        gefunden = False
        for adresse in kontakte:
            if adresse["vorname"].lower() == vorname.lower() and adresse["name"].lower() == name.lower():
                kontakte.remove(adresse) # Entfernt dict-Objekt aus der Liste
                print(f"Adresse {vorname} {name} wurde gelöscht.")
                gefunden = True
                break
        if not gefunden:
            print(f"Adresse {vorname} {name} wurde nicht gefunden.")
    elif auswahl == "4":
        print("Adresse suchen:")
        feld = input("Verfügbare Felder: Vorname, Name, PLZ, Ort, Strasse")
        wert = input("Suchwert: ")
        gefunden = False
        counter = 0
        for adresse in kontakte:
            # adresse[feld] gibt den Wert des Feldes zurück
            # adresse[feld.lower()] gibt den Wert des Feldes zurück, wenn das Feld in Kleinbuchstaben geschrieben ist
            # adresse[feld.lower()].lower() gibt den Wert des Feldes in Kleinbuchstaben zurück
            # adresse[feld.lower()].lower() == wert.lower() gibt True zurück, wenn der Wert des Feldes gleich dem Suchwert ist
            if feld.lower() in adresse and wert.lower() in adresse[feld.lower()].lower():
                print(f"Treffer: {adresse['vorname']} {adresse['name']}, {adresse['plz']}-{adresse['ort']}, {adresse['strasse']}")
                gefunden = True
                counter += 1
        if not gefunden:
            print(f"Keine Adresse mit {feld} = {wert} gefunden.")
        else:
            print(f"{counter} Treffer gefunden.")
    elif auswahl == "5":
        print("Adressen speichern:")
        datei_name = input("Dateiname: ")

        if datei_name == "":
            print("Dateiname darf nicht leer sein.")
            continue

        if os.path.exists(datei_name):
            print(f"Die Datei {datei_name} existiert bereits.")
            aktion = input("Möchten Sie die Datei überschreiben? (Y/N)")
            
            if aktion != "Y" and aktion != "y":
                print("Aktion abgebrochen.")
                continue            

        try:
            with open(datei_name, 'w') as file:
                for adresse in kontakte:
                    zeile = f"{adresse['vorname']},{adresse['name']},{adresse['plz']},{adresse['ort']},{adresse['strasse']}\n"
                    file.write(zeile)
            print(f"Adressen wurden in {datei_name} gespeichert.")
        except IOError:
            print(f"Fehler beim Speichern in {datei_name}.")
    elif auswahl == "6":
        print("Adressen laden:")
        datei_name = input("Dateiname: ")

        if datei_name == "":
            print("Dateiname darf nicht leer sein.")
            continue

        if not os.path.exists(datei_name):
            print(f"Die Datei {datei_name} existiert nicht.")
            continue

        try:
            kontakte = []
            with open(datei_name, 'r') as file:
                zeilen = file.read().splitlines() # Zerlegung und Entfernen des '\n' am Ende jeder Zeile
                for zeile in zeilen:
                    werte = zeile.strip().split(",")
                    adresse = {
                        "vorname": werte[0].strip(),
                        "name": werte[1].strip(),
                        "plz": werte[2].strip(),
                        "ort": werte[3].strip(),
                        "strasse": werte[4].strip()
                    }
                    kontakte.append(adresse)
            print(f"Adressen wurden aus {datei_name} geladen.")
        except IOError:
            print(f"Fehler beim Laden aus {datei_name}.")

    elif auswahl == "7":
        print("Meine Adressen:")
        for adresse in kontakte:
            print(f"{adresse['vorname']} {adresse['name']}, {adresse['plz']}-{adresse['ort']}, {adresse['strasse']}")
    elif auswahl == "8":
        print("Auf Wiedersehen!")
        exit()
    else:
        print("Ungültige Auswahl. Bitte versuchen Sie es erneut.")
    
