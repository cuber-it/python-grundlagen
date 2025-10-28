"""
Programmiere das klassische Wort-Ratespiel Hangman!
Spielregeln:

Das Programm wählt ein geheimes Wort aus
Der Spieler sieht nur Unterstriche: _ _ _ _ _ (für ein Wort mit 5 Buchstaben)
Der Spieler rät einzelne Buchstaben
Richtige Buchstaben werden angezeigt
Bei falschen Buchstaben verliert der Spieler ein Leben
Gewonnen: Wort komplett erraten
Verloren: Alle Leben aufgebraucht (z.B. 6 + 4 Versuche für ein Wort mit 6 Buchstaben)
"""
import random

# Wortliste
wortliste = ["python", "Entwicklung", "Programmieren", "Hangman", "Datenbank"]

wort = random.choice(wortliste)
leben = len(wort) + len(wort) // 2 # Etwas Kulanz damit der Spiele eine Chance hat
display = "_" * len(wort)

print("Das Spiel geht los! Du hast", leben, "Leben.")
print(display)

treffer = ""

while leben > 0 and "_" in display:
    buchstabe = input("Bitte einen Buchstaben eingeben: ")

    if buchstabe in wort:
        print("Richtig!")
        treffer += buchstabe
        # Update display
        display = ""
        for c in wort:
            if c in treffer:
                display += c
            else:
                display += "_"
        print(display)
    else:
        print("Falsch!")
        print(display)
        leben -= 1
    print("Du hast noch", leben, "Leben.")

if "_" not in display:
    print("Du hast gewonnen")
else:
    print("Du hast verloren. Das Wort war:", wort)
