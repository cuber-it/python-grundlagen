
import decimal

# Schema einer Funktion:
#def funktions_name(parameter):
#    # Codeblock
#    pass
#    # optional: return wert(e)

# Eingabe
def read_file(file_name):
    with open(file_name, "r") as file:
        rows = file.read().splitlines()
    return rows

# Verarbeitung
def process_data(rows):
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

# Ausgabe
def write_file(file_name, rows):
    with open(file_name, "w") as file:
        for row in rows:
            file.write(row + "\n")
            

