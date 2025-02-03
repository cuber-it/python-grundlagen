#!/usr/bin/env python3
from decimal import Decimal

# Ungenauigkeit von float
print("float: 0.1 + 0.2 =", 0.1 + 0.2)  # Ergebnis: 0.30000000000000004

# Alternative mit Decimal für präzisere Berechnungen
a = Decimal("0.1")
b = Decimal("0.2")
print("Decimal: 0.1 + 0.2 =", a + b)     # Ergebnis: 0.3
