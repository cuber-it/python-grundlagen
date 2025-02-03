#!/usr/bin/env python3

while(True):
    eingabe = input("Bitte eine Zahl eingeben (Abbruch mit exit): ")
    # Einfache Verzweigung
    if eingabe == "exit":
        break   

    zahl = int(eingabe)
    # Verzweigug mit if, elif, else
    if zahl < 0:
        print("Die Zahl ist negativ.")
    elif zahl == 0:
        print("Die Zahl ist null.")
    else:
        print("Die Zahl ist positiv.")
print("Programm beendet.")


