#!/usr/bin/env python3

wert1 = input("Bitte ersten Wert eingeben: ")
wert2 = input("Bitte zweiten Wert eingeben: ")
operation = input("Bitte Operation eingeben (+, -, *, /): ")

if not wert1.isdigit() or not wert2.isdigit():
    print("Fehler: Werte müssen Zahlen sein.")
    exit(1) 

wert1 = int(wert1)
wert2 = int(wert2)

ergebnis = None

if operation == '+':
    ergebnis = wert1 + wert2
elif operation == '-':
    ergebnis = wert1 - wert2
elif operation == '*':
    ergebnis = wert1 * wert2
elif operation == '/':
    ergebnis = wert1 / wert2
else:
    print("Fehler: Unbekannte Operation.")
    exit(1)

print("Ergebnis:", ergebnis)