# Sets
l1 = [1, 2, 3, 4, 5] + [5] * 10
l2 = [4, 5, 6, 7, 8]
s1 = set(l1)
s2 = set(l2)
print(l1, "->", s1)
print(l2, "->", s2)
s3 = s1.union(s2) # s1 | s2 - Operator
print(s3)
s4 = s1.intersection(s2) # s1 & s2 - Operator
print(s4)
s5 = s1.difference(s2) # s1 - s2 - Operator
print(s5)
s6 = s1.symmetric_difference(s2) # s1 ^ s2 - Operator
print(s6)
s7 = s1.copy()
print(s7)