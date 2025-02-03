#!/usr/bin/env python3
import sys

# Eingabezeile ausgeben (ohne Programmname)
print(sys.argv[1:])

if len(sys.argv) > 1:
    for i, arg in enumerate(sys.argv[1:]):
        print("Argument", i+1 , ":", arg)

    ergebnis = None
    if sys.argv[2] == '+':
        ergebnis = int(sys.argv[1]) + int(sys.argv[3])
    print("Ergebnis:", ergebnis)
    
else:
    print("Keine Argumente")