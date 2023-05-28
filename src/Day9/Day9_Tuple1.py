"""
Day9:
Tuple:
methods and functions using tuples
diff. between list and tuple
for loop using tuple
"""

#tuple is a collection of elements seperated by comma
#and enclosed with in parenthesis

#create a tuple
tuple1 = ()

#create a tuple with all strings
tuple1 = ('amala','kamala','vimala')
print('tuple1 =',tuple1)

#how to find the datatype
dt1 = type(tuple1)
print('datatype is :',dt1)

#create a list of fruits
list_of_fruits = ['apple',
                  'kiwi',
                  'mango']

print('list of fruits =',list_of_fruits)


#how to find the datatype
dt2 = type(list_of_fruits)
print('datatype is :',dt2)

name = 'ramana'
print('name =',name)

#how to find the datatype
dt3 = type(name)
print('datatype is :',dt3)

#tuple elements are immutable (cann't change)
#list is mutable (can be changed)

tuple2 = ('amala','kamala','vimala','ramana','leela')
print('tuple2=',tuple2)

#display the earlier list
print("earlier list =",list_of_fruits)

#can we add a new element to a list? - yes
list_of_fruits.append('guava')
print("list of fruits updated =",list_of_fruits)

#can we add a new element to a tuple? - no (because the tuple is immutable)
#tuple2.append('lalitha')

#can we modify an element
tuple2 = ('amala','leela','kamala','vimala','ramana','leela','kamala','leela','leela')

#using the index method of the tuple, get the positon of a particular element in the tuple
pos_leela = tuple2.index('leela')
print("position of leela in the tuple is :",pos_leela)

#count the no. of occurances of the particular element -leela
n =tuple2.count("leela")
print('no. of occurances of leela is ',n)