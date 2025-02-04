#!/usr/bin/env python3
while True:
    eingabe = input("Eingabe einer Zahl- exit beendet:")

    if eingabe == "exit":
        break

    try:
        zahl = int(eingabe)
        print(f"Die Zahl ist: {zahl}")
        print(f"Das Division der Zahl ist: {1/zahl}")
    except ValueError:
        print("Bitte gib eine gültige Zahl ein.")
