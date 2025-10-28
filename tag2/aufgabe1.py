"""
Ein Palindrom ist ein Wort, das vorwärts und rückwärts gelesen identisch ist.
Beispiele für Palindrome:

Anna
anna

otto
reliefpfeiler
rentner

Keine Palindrome:

hallo
python
computer

Deine Aufgabe:
Schreibe ein Programm, das:

Den Benutzer nach einem Wort fragt
Das Wort rückwärts aufbaut (mit einer Schleife)
Prüft, ob das ursprüngliche Wort und das umgedrehte Wort identisch sind
Eine entsprechende Meldung ausgibt
"""
# Hilfsfunktion
def log(text):
    print("[LOG]:", text, "\n")
    input('Drücke Enter zum Fortfahren...')

# Eingabe
wort = input("Bitte ein Wort eingeben: ").lower()

# Verarbeitung
palindrom = ""

for buchstabe in wort:
    palindrom = buchstabe + palindrom
    log(palindrom)
# Ausgabe
if palindrom == wort:
    print(f"{wort} ein Palindrom")
else:
    print(f"{wort} kein Palindrom")
