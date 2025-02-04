# Beispiel: Addition von 0.1 und 0.2
a = 0.1
b = 0.2
result = a + b

print("Erwartet: 0.3")
print("Tatsächlich:", result)

# Vergleich mit 0.3
print("Ist das Ergebnis gleich 0.3?", result == 0.3)

# Verstärktes Beispiel
a = 0.1
b = 3

result = (a * b) / b

print("Erwartet:", a)
print("Tatsächlich:", result)
print("Ist das Ergebnis gleich a?", result == a)

from decimal import Decimal

a = Decimal('0.1')
b = Decimal('3')

result = (a * b) / b

print("Mit Decimal:", result)
print("Ist das Ergebnis gleich a?", result == a)