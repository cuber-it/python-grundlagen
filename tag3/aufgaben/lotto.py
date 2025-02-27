# Aufgabe:
#
# Einlesen von 6 Zahlen zwischen 1 und 49 von der Tastatur (input) in eine Liste
# - Umwandlung und Prüfung
# Prüfung -> wo kann man von Mengen profitieren?
# Erzeugen von 6 Zufallszahlen (random) zwischen 1 und 49 in eine Liste
# Vergleich der beiden Listen 
#  a. "klassich" mit for-Schleifen
#  b. mit Mengenoperationen
# Ausgabe der Anzahl der Übereinstimmungen

import random
eingabe = input("Bitte 6 Zahlen zwischen 1 und 49 eingeben: ")
try:
    eingabe = eingabe.split() # split() ohne Argumente trennt nach Leerzeichen
    eingabe = [int(zahl) for zahl in eingabe] # list comprehension zur Umwanldung mit Fehler bei nicht int  
    for zahl in eingabe: # Prüfung der Zahlen 
        if not 1 <= zahl <= 49: # Prüfung der Zahlen auf Wertebereich 1 - 49
            raise ValueError
    if len(set(eingabe)) != 6: # Prüfung auf 6 verschiedene Zahlen
        raise ValueError
except:
    print("Fehler bei der Eingabe")
    exit()

ziehung = random.sample(range(1,50), 6) # Ziehung von 6 Zufallszahlen

ergebnis = list( # 
    set(eingabe).intersection( # Schnittmenge der Eingabe mit ...
        set(ziehung) # ... Umwandlung in Menge
    )
) 
# oder:
# ergebnis = []
# for zahl in eingabe:
#     if zahl in ziehung:
#         ergebnis.append(zahl)

print("Treffer:", len(ergebnis), "Richtige:", sorted(ergebnis)) # Ausgabe der Treffer und der richtigen Zahlen
print("Eingabe:", sorted(list(eingabe))) # Ausgabe der Eingabe, sortiert
print("Ziehung:", sorted(list(ziehung))) # Ausgabe der Ziehung, sortiert
