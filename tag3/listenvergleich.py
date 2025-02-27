liste1 = [1, 2, 3, 4, 5] + [5] * 10
liste2 = [4, 5, 6, 7, 8]

# Doubletten ausfiltern in liste1 mit for und in Operator, ergebnis Liste ohne Doubletten
liste1_ohne_doppelte = []
liste1_doubletten = []
for element in liste1:
    if element not in liste1_ohne_doppelte:
        liste1_ohne_doppelte.append(element)
    else:
        liste1_doubletten.append(element)
print(liste1_doubletten)
print(liste1_ohne_doppelte)

liste1_ohne_doppelte = list(set(liste1))
print(liste1_ohne_doppelte)

# Doubletten in liste1 auf einmaliges Auftreten reduzieren mit for und in Operator
liste1_ohne_doppelte = []
for element in liste1:
    if liste1.count(element) == 1:
        liste1_ohne_doppelte.append(element)
print(liste1_ohne_doppelte)

liste1_ohne_doppelte = [element for element in liste1 if liste1.count(element) == 1]
print(liste1_ohne_doppelte)

# Doubletten finden mit for-Schleife und in Operator
doppelte = []
for element in liste1:
    if element in liste2:
        doppelte.append(element)
print(doppelte)

doppelte = list(set(liste1).intersection(set(liste2)))
print(doppelte)

