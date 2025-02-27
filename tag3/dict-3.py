data = { 'Name': 'Müller', 'Vorname': 'Peter', 'PLZ': '12345', 'Ort': 'Berlin', 'Strasse': 'Hauptstrasse' }
print(data)

print(data.keys())
print(data.values())
print(data.items())
print('-' * 40)
for key in data.keys():
    print(key, data[key])
print('-' * 40)
for value in data.values():
    print(value)
print('-' * 40)
for key, value in data.items():
    print(key, value)

# Zugriff lesend
print(data['Name']) # KeyError, wenn nicht vorhanden
print(data.get('Name')) # None, wenn nicht vorhanden
print(data.get('Telefon')) # None, wenn nicht vorhanden
print(data.get('Telefon', 'nicht vorhanden'))   # Defaultwert 'nicht vorhanden', wenn nicht vorhanden
print('-' * 40)

# Zugriff neu schreibend/Neuanlage des Keys
data['Telefon'] = '123456'
print(data)

# Zugriff überschreibend/auf existierenden Key
data['Telefon'] = '654321'
print(data)

data.update({'Telefon': '123456'})
print(data) # Telefon wird überschrieben    

# Zahlen als KEys, Objekte als Keys
data.clear()
# Zahlen - kommt vor
data[1] = 'ein Wert'
data[2] = 'noch ein Wert'
data[3] = 'noch ein Wert'
print(data)

data.clear() 
# Tupel - exotisch
data[(1, 2, 3)] = 'ein Wert'
data[(4, 5, 6)] = 'noch ein Wert'
data[(7, 8, 9)] = 'noch ein Wert'
print(data)

data.clear()
# dict mit dict als Keys - sehr exotisch
data[{'a': 1, 'b': 2}] = 'ein Wert'
data[{'c': 3, 'd': 4}] = 'noch ein Wert'
data[{'e': 5, 'f': 6}] = 'noch ein Wert'
print(data)