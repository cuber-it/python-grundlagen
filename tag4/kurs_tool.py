# Eingabe
def _read_file(file_name): # _ bedeutet, dass die Funktion nur innerhalb des Moduls sichtbar ist bzw genuzt werden soll
    with open(file_name, "r") as file:
        rows = file.read().splitlines()
    return rows

# Verarbeitung
def _process_data(rows):
    daten = {}
    for row in rows[1:]:
        spalten = row.split(", ")
        datum = spalten[0]
        tageswerte = { 
            'Close':  decimal.Decimal(spalten[1][1:]), 
            'Volume': int(spalten[2]), 
            'Open':   decimal.Decimal(spalten[3][1:]), 
            'High':   decimal.Decimal(spalten[4][1:]), 
            'Low':    decimal.Decimal(spalten[5][1:]) }
        daten.update({datum: tageswerte})
    return daten

def kurs_reader(kursfile): # die offizielle Funktion, die von anderen Modulen genutzt werden soll
    rows = _read_file(kursfile)
    return _process_data(rows)

def get_kurs(kursdaten, datum):
    return kursdaten.get(datum, "Nichts gefunden")

def addiere_kurse(kursdaten, datum, kurswerte):
    kursdaten[datum] = kurswerte
    return kursdaten

def aendere_kurse(kursdaten, datum, kurswerte):
    kursdaten[datum].update(kurswerte)
    return kursdaten