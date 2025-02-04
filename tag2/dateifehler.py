#!/usr/bin/env python3
try:
    file = open('datei.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print("Fehler: Datei nicht gefunden.")
finally:
    print("Versuche, die Datei zu schließen.")
    try:
        file.close()
    except NameError:
        print("Datei wurde nicht geöffnet, daher kein Schließen erforderlich.")