"""
list is a collection of elements seperated by comma
and enclosed with in square brackets.

listname = [element1,element2....]
"""

#create a list of fruits
list1 = ['mango','guava','banana',"apple",'tomato']
print('list1 =',list1)

#add a new element to a list - append()
list1.append('kiwi')

#add few elements simultaneously in to a list
#list1.append('fruit1','fruit2','fruit3')

#TypeError: list.append() takes exactly one argument (3 given)

list1.append('fruit1')
list1.append('fruit2')
list1.append('fruit3')
print('list1 modifed =',list1)


#iterate on list
for fruit in list1:
    print('fruit =',fruit)
else:
    print('done with for loop..')

