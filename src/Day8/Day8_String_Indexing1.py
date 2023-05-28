"""
Day8:
Agenda:
Indexing with strings   - done
Slicing with strings
list indexing
list slicing
Note: positive and negetive slicing


"""

#positive indexing and slicing always starts with 0 and goes further like 1,2,3,....
#positive indexing and slicing direction is always from left to righht

#negetive indexing and slicing always starts with -1 and goes like -2,-3....
# negetive indexing and slicing is always in the right to left direction

name1 = 'Bangalore'
name2 = 'Hyderabad'
print("name1 = {} and name2 ={}".format(name1,name2))

#indexing with strings
letter1 = name1[0]
print("name1[0] is : {}".format(name1[0]))

letter2 = name1[1]
print('name1[0] is : {}'.format(name1[1]))

letter8 = name1[8]
print('name1[8] is : {}'.format(name1[8]))

#IndexError: string index out of range
letter9 = name1[90]
print('name1[9] is : {}'.format(name1[90]))

