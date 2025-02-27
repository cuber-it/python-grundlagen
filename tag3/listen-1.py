import pprint

list1 = [1,2,3,4,5]
list2 = list("12345")

print(list1)
print(list2)

list3 = [list1, list2]
print(list3)

list4 = list1 + list2
print(list4)

list5 = list1 * 3
print(list5)

list6 = [0] * 10
print(list6)

list7 = [None] * 10
print(list7)

list8 = [1, 'a', 'Willi', 3.14, True, [1,2,3], [1,2, [1234]], {1,2,3}, (1,2,3), {'a':1, 'b':2}]
print(list8)
pprint.pprint(list8)

matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix)
pprint.pprint(matrix)