#!/usr/bin/env python3
# Thema: Fehlerbehandlung mittels try ... except ... finally

a = input("Divisor: ")

try:
    a = int(a)
    b = 10 / a
    print("Ergebnis:", b)
except ZeroDivisionError:
    print("Division durch Null ist nicht erlaubt!") 
except ValueError:
    print("Bitte geben Sie eine Zahl ein!")
finally:
    print("Programmende")

# Einfacher Fehlertest
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Fehler: Division durch Null ist nicht erlaubt.")

# Mit finally
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


