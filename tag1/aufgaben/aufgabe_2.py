#!/usr/bin/env python3
# Aufgabe
# Simuliere ein einfaches Aufzugsystem mit 3 Aufzügen (A, B, C) und 8 Etagen (1 bis 8).
# Der Benutzer gibt an, in welche Etage er möchte, und das System entscheidet, welcher Aufzug den Ruf übernimmt.
#
# Die Aufzüge starten zu Beginn alle in der 1. Etage.
#
# Der Benutzer sagt, in welcher Ebene er sich befindet und wo er hinwill.
# Das System entscheidet, welcher Aufzug fährt.
#
# Beispiel: Der Benutzer befindet sich in der 3. Etage und möchte in die 6. Etage.
# Eingabe-1: von oder exit
# Eingabe-2: bis
# 
# Regeln für die Aufzugwahl:
#
#    Der Aufzug, der am nächsten zur Ziel-Etage ist, fährt.
#    Bei gleicher Entfernung entscheidet die Reihenfolge der Aufzüge (A vor B vor C).
#    Nach jeder Fahrt aktualisiert sich die Position des Aufzugs
#
# Anforderungen:
#
#    Eingabe: Start-Etage (1–8)
#             Ziel-Etage (1–8)
#    Ausgabe: Welcher Aufzug fährt und von welcher Etage
#    Fehlerprüfung: Ungültige Etagen abfangen
#    Abbruch: Mit "exit" kann das Programm beendet werden

# Initialpositionen der Aufzüge
aufzug_a = 1
aufzug_b = 1
aufzug_c = 1
erdgeschoss = 0
skyfloor = 8

print("Willkommen zur Aufzug-Simulation!")
print(f"Es gibt 3 Aufzüge: A, B und C. Die Etagen reichen von {erdgeschoss} (Erdgeschoss) bis {skyfloor} (Skyfloor).")
print('Gib "exit" ein, um das Programm zu beenden.\n')

while True:
    eingabe = input("Eingabe-1: von (Etage) oder exit: ").strip().lower()
    if eingabe == "exit":
        print("Simulation beendet.")
        break

    try:
        # Start-Etage eingeben
        startpunkt = int(eingabe)
        if startpunkt < erdgeschoss or startpunkt > skyfloor:
            print("Ungültige Etage. Bitte gib eine gültige Etage ein.")
            continue
        endpunkt = int(input("Eingabe-2: bis (Etage): "))
        if endpunkt < erdgeschoss or endpunkt > skyfloor:
            print("Ungültige Etage. Bitte gib eine gültige Etage ein.")
            continue    
        if startpunkt == endpunkt:
            print("Du bist bereits in der gewünschten Etage.")
            continue

        # Berechnung des nächstgelegenen Aufzugs (zum Startpunkt des Benutzers)
        dist_a = abs(aufzug_a - startpunkt)
        dist_b = abs(aufzug_b - startpunkt)
        dist_c = abs(aufzug_c - startpunkt)

        # Aufzugsauswahl basierend auf der kürzesten Entfernung
        if dist_a <= dist_b and dist_a <= dist_c:
            gewaehlter_aufzug = "A"
            aufzug_position = aufzug_a
            aufzug_a = endpunkt
        elif dist_b <= dist_c:
            gewaehlter_aufzug = "B"
            aufzug_position = aufzug_b
            aufzug_b = endpunkt
        else:
            gewaehlter_aufzug = "C"
            aufzug_position = aufzug_c
            aufzug_c = endpunkt
        # Ausgabe: Fahrt von der aktuellen Position zum Benutzer und dann zur Ziel-Etage
        print(f"Aufzug {gewaehlter_aufzug} fährt von Etage {aufzug_position} zur Etage {startpunkt}, um dich abzuholen.")
        print(f"Dann fährt Aufzug {gewaehlter_aufzug} von Etage {startpunkt} nach Etage {endpunkt}.\n")

        # Aktueller Status der Aufzüge
        print("Aktueller Aufzug-Status:")
        print(f"Aufzug A befindet sich jetzt auf Etage {aufzug_a}")
        print(f"Aufzug B befindet sich jetzt auf Etage {aufzug_b}")
        print(f"Aufzug C befindet sich jetzt auf Etage {aufzug_c}\n")

    except ValueError:
        print("Ungültige Eingabe. Bitte gib eine gültige Zahl ein.")
        continue