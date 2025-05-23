datei="/home/ucuber/Workspace/kurse/python-grundlagen/materialien/HistoricalQuotes.csv"

# E
with open(datei) as fd:
    zeilen = fd.read().splitlines() # zerlegt und beseitigt das '\n' am Ende jeder Zeile

# V - Datenvorverarbeitung
spalten_namen = []
for name in zeilen[0].split(","):
    spalten_namen.append(name.strip())

# V - Datenvorverarbeitung
daten = []
for zeile in zeilen[1:]:
    werte = zeile.split(",")
    werte = [wert.strip() for wert in werte]
    werte = [wert.replace('$', '') for wert in werte]

    werte_dict = dict(zip(spalten_namen, werte))
    werte_dict['Date'] = werte_dict['Date'].replace('/', '-')
    werte_dict['Volume'] = int(werte_dict['Volume'])
    for key in ['Open', 'High', 'Low', 'Close/Last']:
        werte_dict[key] = float(werte_dict[key])
    daten.append(werte_dict)

# V - Auswertung etc.

# A - Ausgabe
print(spalten_namen)
print(daten[:10])