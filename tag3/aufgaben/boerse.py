import os
import sys
import locale
import datetime

import decimal

datei_name = r"materialien/HistoricalQuotes.csv"

# Set locale to German (Germany)
locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')

# E ingabe
with open(datei_name, "r") as file:
    rows = file.read().splitlines() 

# Vorverarbeitung/Aufbereitung
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
    # key = datum, value = tageswerte
    #daten[datum] = tageswerte
    daten.update({datum: tageswerte})

# Verarbeiung/Hauptaufgabe
while True:
    datum = input("Bitte geben Sie ein Datum ein (MM/DD/YYYY) oder first oder last: ")
    if datum == "exit":
        break
    if datum == "first":
        datum = list(daten.keys())[-1] # Daten laufen von hoch zu niedrigem Datum, deswegen hier -1
    if datum == "last":
        datum = list(daten.keys())[0] # Daten laufen von hoch zu niedrigem Datum, deswegen hier 0
    date_obj = datetime.datetime.strptime(datum, "%m/%d/%Y")
    # Formatierte Ausgabe gemäß Locale
    formatted_date = date_obj.strftime("%x") 
    print(formatted_date, daten.get(datum, "Nichts gefunden"))

# Ausgabe