#!/usr/bin/env python3

name = "Alice"
alter = 30
preis = 19.99
pi = 3.1415926535

# 1. f-String (empfohlen, Python 3.6+)
print(f"Hallo, mein Name ist {name} und ich bin {alter} Jahre alt.")
print(f"Der Preis beträgt {preis:.2f} Euro.")  # Zwei Nachkommastellen
print(f"Pi auf 4 Nachkommastellen: {pi:.4f}")

# 2. f-String mit Berechnungen
a, b = 5, 3
print(f"Die Summe von {a} und {b} ist {a + b}.")
print(f"Das Quadrat von {b} ist {b**2}.")

# 3. f-String mit Formatierung (Ausrichtung)
print(f"|{'Links':<10}|{'Mitte':^10}|{'Rechts':>10}|")

# 4. String.format() (älterer Stil, aber noch verbreitet)
print("Hallo, mein Name ist {} und ich bin {} Jahre alt.".format(name, alter))
print("Pi auf 4 Nachkommastellen: {:.4f}".format(pi))

# 5. %-Operator (veraltet, aber manchmal noch in älterem Code zu finden)
print("Hallo, mein Name ist %s und ich bin %d Jahre alt." % (name, alter))
print("Pi auf 4 Nachkommastellen: %.4f" % pi)
