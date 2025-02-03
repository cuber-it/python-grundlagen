#!/usr/bin/env python3
# Arithmetische Operatoren
a = 10
b = 3
print("a + b =", a + b)      # Addition
print("a - b =", a - b)      # Subtraktion
print("a * b =", a * b)      # Multiplikation
print("a / b =", a / b)      # Division (Float)
print("a // b =", a // b)    # Ganzzahlige Division
print("a % b =", a % b)      # Modulo
print("a ** b =", a ** b)    # Potenzierung

# Vergleichsoperatoren
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Logische Operatoren
x = True
y = False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

# Bitweise Operatoren
a = 0b1010  # 10 in Binär
b = 0b0101  # 5 in Binär
print("a & b:", bin(a & b))
print("a | b:", bin(a | b))
print("a ^ b:", bin(a ^ b))
print("~a:", bin(~a))
print("a << 1:", bin(a << 1))
print("a >> 1:", bin(a >> 1))

# Effekte bie Strings: +, *, in, not in
s1 = "Python"
s2 = "ist"
s3 = "toll"
print(s1 + " " + s2 + " " + s3)
print(s1 * 3)
print("P" in s1)

# Identitätsoperatoren
a = 10
b = 10
print("a is b:", a is b)
print("a is not b:", a is not b)
