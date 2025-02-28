import funktionen

#-------------------------------------------------------------------------
daten = funktionen.read_file("materialien/HistoricalQuotes.csv")
print(daten)
funktionen.write_file("materialien/HistoricalQuotes_copy.csv", daten)
print("Datei kopiert")

kurse = funktionen.process_data(daten)
print(kurse)
print("Daten verarbeitet")