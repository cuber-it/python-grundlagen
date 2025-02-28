# Die Funktinalität der Lottobude mit Funktionen aufbauen
import random

def read_tipp(prompt):
    return input(prompt).split()

def check_tipp(tipp):
    if len(tipp) != 6:
        raise ValueError("Ungültige Anzahl")

    for zahl in tipp:
        if not zahl.isdigit():
            raise ValueError("Ungültige Zahl")
        
    for zahl in tipp:
        if int(zahl) < 1 or int(zahl) > 49:
            raise ValueError("Ungültige Zahl")
        
    for zahl in tipp:
        if tipp.count(zahl) > 1:
            raise ValueError("Doppelte Zahl")

def convert_tipp(tipp):
    return [int(zahl) for zahl in tipp]

def prepare_tipp(tipp):
    check_tipp(tipp)
    return convert_tipp(tipp)

def generate_zufallszahlen():
    return random.sample(range(1, 50), 6)

def compare_tipp(tipp, zahlen):
    return list(set(zahlen).intersection(tipp))

def report(tipp, ziehung, treffer):
    result = "Ergebnisse der Ziehung\n"
    
    result += "Ihr Tipp:\n"
    for i, zahl in enumerate(tipp, 1):
        result += f"Zahl {i}: {zahl}\n"

    result += "Die Zahlen der Ziehung:\n"
    for i, zahl in enumerate(ziehung, 1):
        result += f"Zahl {i}: {zahl}\n"

    result += "Treffer:\n"
    for i, zahl in enumerate(treffer, 1):
        result += f"Zahl {i}: {zahl}\n"

    return result

if __name__ == "__main__":
    tipp = read_tipp("Bitte geben Sie Ihren Tipp ab: ")
    try:
        tipp = prepare_tipp(tipp)
        zahlen = generate_zufallszahlen()
        treffer = compare_tipp(tipp, zahlen)
        print(report(tipp, zahlen, treffer))
    except ValueError as e:
        print("Fehler aufgetreten, Programmabbruch:", e)

