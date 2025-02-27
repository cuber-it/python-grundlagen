data = [
    {'Name': 'Müller', 'Vorname': 'Peter', 'PLZ': '12345', 'Ort': 'Berlin', 'Strasse': 'Hauptstrasse'},
    {'Vorname': 'Hans', 'PLZ': '54321', 'Ort': 'Hamburg', 'Strasse': 'Nebenstrasse', 'Name': 'Schmidt'},
    {'Ort': 'München','Name': 'Meier', 'Vorname': 'Willi', 'PLZ': '98765',  'Strasse': 'UmmeEcke'}
]

header = list(data[0].keys())
for i in range(len(header)):
    print(header[i], end = ':')

print('\n', '-' * 40)

for row in data:
    for column in header:
        print(row[column], end = ':')
    print()

for row in data:
    print(row['Vorname'])