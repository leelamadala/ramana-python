"""
list operations

"""

list1 = ['brinjal','potato','ladyfinger']
print('list1 =',list1)

#how to get the position of elements
mypos = list1.index('brinjal')
print('position is ',mypos)

#mypos2 = list1.index('Ladyfinger')
#print('position of the given element is :',mypos2)


#list1['ladyfinger'] ''' error''''
#ValueError: 'Ladyfinger' is not in list

list1 = ['Ladyfinger']


mypos2 = list1.index('Ladyfinger')
print('position of the given element is :',mypos2)
