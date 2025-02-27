matrix = [[1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11, 12]]

element = matrix[1][1]
zeile = matrix[1]
print(element)
print(zeile)

print(len(matrix))
print(len(matrix[0]))
print(len(matrix[1]))  
print(len(matrix[2]))

letzes_element = matrix[len(matrix)-1][len(matrix[len(matrix)-1])-1]
print(letzes_element)
letzes_element = matrix[-1][-1] # -1 is the last element of the list
print(letzes_element)

list1 = [1,2,3,4,5]
element_start = list1[0]
element_ende = list1[-1]
element_mitte = list1[len(list1)//2] # // is integer division
print(element_start)
print(element_ende)
print(element_mitte)

# Slicing
list1 = ['a', 'b', 'c', 'd', 'e']
list2 = list1[1:4] # list2 = [b,c,d] - immer n-1 für das Ende denken!
print(list2)
list3 = list1[1:]  # list3 = [b,c,d,e]
print(list3)
list4 = list1[:3]  # list4 = [a,b,c]
print(list4)
list5 = list1[:]  # list5 = [a,b,c,d,e]
print(list5)
list6 = list1[::2]# list6 = [a,c,e]
print(list6)
list7 = list1[::-1]# list7 = [e,,d,c,b,a]
print(list7)
list8 = list1[1:4:2]# list8 = [b,d]
print(list8)
list9 = list1[-3:-1]# list9 = [c,d]
print(list9)
list10 = list1[-3:]# list10 = [c,d,e]
print(list10)