# Listcomprehension
# Listcomprehension is a compact way of creating a list in Python. It is a short way to create a new list by performing an operation on each item in an existing list. Listcomprehension is enclosed in square brackets, which contain an expression followed by a for clause, then zero or more for or if clauses. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.

list = [1, 2, 3, 4, 5]
list2 = [element * 2 for element in list] # list2 = [2, 4, 6, 8, 10]
print(list2)

# long form:
list2 = []
for element in list:
    list2.append(element * 2)

list3 = [element * 2 for element in list if element % 2 == 0] # list3 = [4, 8] - only even numbers fitlered by if
print(list3)

#long form:
list3 = []
for element in list:
    if element % 2 == 0:
        list3.append(element * 2)
        
# Dictionary Comprehension
# Dictionary Comprehension is a concise way to create dictionaries. It is enclosed in curly braces, which contain key-value pairs separated by a colon. The key-value pairs are separated by a comma. The result will be a new dictionary containing the key-value pairs.

dict1 = {1: 'a', 2: 'b', 3: 'c'}
dict2 = {value: key for key, value in dict1.items()} # dict2 = {'a': 1, 'b': 2, 'c': 3} - key and value are swapped
print(dict2)

# long form:
dict2 = {}
for key, value in dict1.items():
    dict2[value] = key



dict3 = {key: value for key, value in dict1.items() if key % 2 == 0} # dict3 = {2: 'b'} - only even keys are filtered by if
print(dict3)

#long form:
dict3 = {}
for key, value in dict1.items():
    if key % 2 == 0:
        dict3[key] = value



