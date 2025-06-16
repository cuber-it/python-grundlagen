#!/usr/bin/env python3
import random

# Eingabe

def check_and_convert_rohdaten(rohdaten: list[str]) -> list[int]:
    # return [int(wert) for wert in rohdaten]
    daten = []
    if len(rohdaten) != 6:
        raise ValueError("Es müssen genau 6 Zahlen eingegeben werden.")
    
    for wert in rohdaten:
        neu_daten = int(wert)
        if neu_daten < 1 or neu_daten > 49:
            raise ValueError("Die Zahlen müssen zwischen 1 und 49 liegen.")
        if neu_daten in daten:
            raise ValueError("Es dürfen keine doppelten Zahlen eingegeben werden.")
        daten.append(neu_daten)
    return daten

def read_tipp() -> list[int]:
    # Version 1: mit input, d.h.:
    rohdaten = input("Bitte geben Sie Ihre Lottozahlen ein (6 Zahlen, durch Komma getrennt): ")
    rohdaten = rohdaten.split(",")  # Zerlegung der Eingabe in eine Liste

    return check_and_convert_rohdaten(rohdaten)

# Verarbeitung
def run_ziehung() -> list[int]:
    return random.sample(range(1, 50), 6)  # Ziehung der Lottozahlen

def check_tipp(tipp: list[int], ziehung: list[int]) -> int:
    #return list(set(tipp).intersection(set(ziehung)))
    result = []
    for wert in tipp:
        if wert in ziehung:
            result.append(wert)
    return result

# Ausgabe
def write_ziehung(ziehung: list[int]) -> None:
    print("Die gezogenen Lottozahlen sind:", ziehung)

def write_tipp(tipp: list[int]) -> None:
    print("Ihre Lottozahlen sind:", tipp)

def write_gewinne(treffer: list[int]) -> None:
    print("Sie haben folgende Zahlen richtig:", treffer)

def lotto_bude() -> None:
    print("Willkommen in der Lotto-Bude!")
    print("Hier können Sie Ihre Lottozahlen eingeben und überprüfen.")
    print("Viel Glück!")

    # Eingabe
    tipp = read_tipp()

    # Verarbeitung
    ziehung = run_ziehung()
    treffer = check_tipp(tipp, ziehung)

    # Ausgabe
    write_ziehung(ziehung)
    write_tipp(tipp)
    write_gewinne(treffer)

if __name__ == "__main__":
    lotto_bude()
    # Wenn das Modul direkt ausgeführt wird, wird die Funktion lotto_bude() aufgerufen
    # Wenn das Modul importiert wird, wird die Funktion lotto_bude() nicht aufgerufen
