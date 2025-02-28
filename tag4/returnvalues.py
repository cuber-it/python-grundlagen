def mach_was(namen):
    result = []
    counter = 0

    while counter < len(namen):
        result.append((counter, namen[counter]))
        counter += 1
    return result

for i, name in mach_was(["Willi", "Heinz", "Karl"]):
    print(i, name)

#-----
# einfacher return value
def add(a, b):
    return a + b

# Liste als returnvalue
def zero_liste(anzahl):
    return [0] * anzahl # Gibt Liste mit anzahl Nullen zurück

# Dictionary als returnvalue
def zero_dict(anzahl):
    return {i: 0 for i in range(anzahl)}

# Kombination von String und Liste
def string_liste(anzahl):
    return "Hallo", [0] * anzahl # Gibt Tupel zurück (String, Liste) -> ("Hallo", [0, 0, 0, 0, 0])


# ERgebniszuordnung von return-Werten
a = add(1, 2)
l = zero_liste(5) # l = [0, 0, 0, 0, 0]
d = zero_dict(5)
s, l = string_liste(5)
w1, w2, *werte = zero_liste(5) # w1 = 0, w2 = 0, werte = [0, 0, 0]
print(w1, w2, werte)
