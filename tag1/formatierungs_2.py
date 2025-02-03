a = "X"
b = 5
c = 1234.56789
d = 0.756
e = 255

# 1. Standardformatierung
print(f"Projekt {a} erzeugt {b} Treffer")

# 2. Ganzzahl mit führenden Nullen
print(f"Treffer mit führenden Nullen: {b:03d}")

# 3. Rechtsbündig mit Breite
print(f"Rechtsbündig (Breite 10): |{b:>10}|")

# 4. Links bündig mit Breite
print(f"Linksbündig (Breite 10): |{b:<10}|")

# 5. Zentriert mit Breite
print(f"Zentriert (Breite 10): |{b:^10}|")

# 6. Fließkommazahl (Standard)
print(f"Fließkommazahl: {c}")

# 7. Fließkommazahl mit 2 Nachkommastellen
print(f"Fließkommazahl (2 Nachkommastellen): {c:.2f}")

# 8. Wissenschaftliche Notation
print(f"Wissenschaftliche Notation: {c:.2e}")

# 9. Prozentformat
print(f"Prozent: {d:.2%}")

# 10. Hexadezimaldarstellung
print(f"Hexadezimal: {e:x}")

# 11. Oktal
print(f"Oktal: {e:o}")

# 12. Binär
print(f"Binär: {e:b}")

# 13. Mit Tausender-Trennzeichen
print(f"Zahl mit Tausender-Trennzeichen: {c:,.2f}")

# 14. Kombination von Formatierungen
print(f"Treffer: {b:03d}, Wert: {c:,.1f}, Prozent: {d:.1%}, Hex: {e:X}")
