#!/usr/bin/env python3

# Aufgabenbeschreibung:
# Schreibe ein einfaches Python-Programm, bei dem der Benutzer 
# eine Zahl zwischen 1 und 10 erraten muss. Das Programm gibt 
# Hinweise, ob die geratene Zahl zu hoch oder zu niedrig ist. 
# Der Benutzer soll so lange raten, bis die richtige Zahl erraten wird
# oder er aufgibt.

import random

geheime_zahl = random.randint(1, 10)
versuch = 0

print("Willkommen beim Zahlenschätzspiel!")
print("Rate eine Zahl zwischen 1 und 10.")
print("Gib 'Ende' ein, um das Spiel zu beenden.")

# Schleife läuft, bis die richtige Zahl erraten wurde oder der Benutzer aufgibt
while True:
    eingabe = input("Dein Tipp: ").strip().lower() # Eingabe bereinigen und klein schreiben
    versuch += 1  # Erhöhe den Zähler für jeden Versuch

    # Überprüfen, ob der Benutzer aufgeben möchte
    if eingabe == "ende":
        print(f"Du hast aufgegeben. Die geheime Zahl war {geheime_zahl}.")
        break

    # Überprüfen, ob die Eingabe eine Zahl ist
    if eingabe.isdigit():
        tipp = int(eingabe)

        # Vergleiche den Tipp mit der geheimen Zahl
        if tipp < geheime_zahl:
            print("Zu niedrig, versuche es noch einmal.")
        elif tipp > geheime_zahl:
            print("Zu hoch, versuche es noch einmal.")
        else:
            print(f"Glückwunsch! Du hast die Zahl {geheime_zahl} erraten.")
            print(f"Anzahl der Versuche: {versuch}")
            break
    else:
        print("Bitte gib eine gültige Zahl ein oder 'Ende' zum Beenden!")
exit(0)