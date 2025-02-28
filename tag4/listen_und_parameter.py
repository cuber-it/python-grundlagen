def summe(werte): # Annahme: werte ist eine Liste
    summe = 0
    for wert in werte:
        summe += wert
    return summe    

werte = [1, 2, 3, 4, 5]
ergebnis = summe(werte)
print("Summe:", ergebnis)

ergebnis = summe([1, 2, 3, 4, 5])
print("Summe:", ergebnis)

def summe(*werte): # Annahme: werte ist eine Folge von Einzelwerten
    summe = 0
    for wert in werte:
        summe += wert
    return summe

ergebnis = summe(1, 2, 3, 4, 5)
print("Summe:", ergebnis)

werte = [1, 2, 3, 4, 5]
# ergebnis = summe(werte) # Fehler: werte ist eine Liste
ergebnis = summe(*werte) # Entpacken der Liste in Einzelwerte
print("Summe:", ergebnis)