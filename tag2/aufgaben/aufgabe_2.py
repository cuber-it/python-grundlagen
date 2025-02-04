# Aufgabe
#
# Palindrom: Ein Wort wird "vorwärts" genauso gelesen wie "rückwärts"
# Beispiel: "Anna", "Rentner", "Lagerregal"
# Gegenteil: "Haus", "Auto", "Schule"

# Der Benutzer soll ein Wort eingeben
# Das Programm prüft, ob es vorwärts und rückwärts gleich ist -> Palindorm
# oder eben nicht
#
# Hinweis: schaut mal bei den String-Methoden, ob ihr das was hilfreiches findet
# https://docs.python.org/3/library/stdtypes.html#string-methods
#
eingabe = input("Bitte geben Sie ein Wort ein: ")
# umgekehrtes_wort = eingabe.replace(" ", "")
# umgekehrtes_wort = umgekehrtes_wort[::-1] 
# oder zusammengezogen:
original = eingabe.replace(" ", "").lower()
vergleich = original[::-1]
if original == vergleich:
    print("Das Wort", eingabe, "ist ein Palindrom.")
else:
    print("Das Wort", eingabe, "ist kein Palindrom.")

