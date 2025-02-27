data = {}

while True:
    name = input('Name: ')
    if name == 'exit':
        break
    vorname = input('Vorname: ')
    plz = input('PLZ: ')
    ort = input('Ort: ')
    strasse = input('Strasse: ')
    data[name] = {'Vorname': vorname, 'Name': name, 'PLZ': plz, 'Ort': ort, 'Strasse': strasse}

for datensatz in data.values():
    print(datensatz['Name'], datensatz['Vorname'])

print("Adresssuche via Name:")
while True:
    name = input('Name: ')
    if name == 'exit':
        break
    if name in data:
        print(data[name])
    else:
        print('Name nicht gefunden')
