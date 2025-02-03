#!/usr/bin/env python3
# Dynamische Typisierung: Variablen können verschiedene Typen annehmen.
x = 42
print("x =", x, "Type:", type(x))
x = "Python"
print("x =", x, "Type:", type(x))

# Typstrenge Operation: Unzulässige Typkombinationen führen zu Fehlern.
a = 5
b = "10"
try:
    print("a + b =", a + b)
except TypeError as error:
    print("Fehler:", error)

# Umwandlungen können notwendig sein
a = 5
b = "10"

print("a + b =", a + int(b))

    