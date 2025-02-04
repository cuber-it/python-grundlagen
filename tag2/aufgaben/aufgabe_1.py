# Aufgabe:
# Es soll eine digitale Lottobude gebaut werden
#
# Spiel 6 aus 49
#
# Der Spieler soll 6 Zahlen eingeben können
#
# Reegeln für die Zahlen:
# - Zahl muss eine Ganzzahl sein
# - Zahl muss zwischen 1 und 49 liegen
# Wenn das nicht zutrifft, soll eine Fehlermeldung ausgegeben werden
# Wenn das zutrifft, soll ein Zähler hochgezählt werden
# Wenn der Zähler 6 erreicht, soll die Eingabeschleife beendet werden
#
counter = 0

while counter < 6:
    number = input("Bitte geben Sie eine Zahl zwischen 1 und 49 ein (exit für Abbruch): ")
    if number.lower() == "exit":
        break
    try:
        number = int(number) # str -> int, str wegen input
        if number >= 1 and number <= 49:
            print("Zahl:", number, "ist korrekt")
            counter = counter + 1 # Kürzer geschrieben: counter += 1
        else:
            print("Fehler: Die Zahl muss zwischen 1 und 49 liegen und nicht", number)
    except ValueError:
        print("Fehler: Bitte geben Sie eine Zahl ein und nicht", number)
print("Fertig")