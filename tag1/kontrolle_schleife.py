#!/usr/bin/env python3
# Schleifen

# Offene Schleife: while
i = 0
while i < 5:
    print("-->", i)
    i += 1 # i = i + 1
print("Fertig: i =", i)

# Geschlossene Schleife: for
for i in range(5): # range(5) = [0, 1, 2, 3, 4], ist ein Generator
    print("-->", i)
print("Fertig: i =", i)

# mit enumerate
for i, item in enumerate(["a", "b", "c", "d", "e"]):
    print(i, item)

# mit break - Schleife abbrechen
for i in range(5):
    if i == 3:
        break
    print("-->", i)
print("Fertig: i =", i)

# mit continue - springt zum nächsten Schleifendurchlauf
for i in range(5):
    if i == 3:
        continue
    print("-->", i)
print("Fertig: i =", i)

# mit else - wird ausgeführt, wenn die Schleife normal beendet wurde
for i in range(5):
    print("-->", i)
else:
    print("Fertig: i =", i)



