dateiname = input("Eingabe-Dateiname: ")

with open(dateiname, "r") as datei:
    inhalt = datei.read()

# Verarbeitung: ....

dateiname = input("Ausgabe-Dateiname: ")

with open(dateiname, "w") as datei:
    datei.write(inhalt)
