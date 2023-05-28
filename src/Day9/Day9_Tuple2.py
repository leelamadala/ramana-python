"""
Day9: tuples

creation of tuples
methods on tuples (index,count)
add an element
access the position of an element
modify an element
delete an element
"""

#create a tuple
tuple_of_aadhar = ('1111-2222-3333','1234-5678-9808','ramana','leela')
print('tuple is :',tuple_of_aadhar)

#get the position of the person named leela
ele = tuple_of_aadhar[3]
print("element is :",ele)

#modify the name 'leela' to 'leelashankar'
#tuple_of_aadhar[3] = 'leelashankar'
#TypeError: 'tuple' object does not support item assignment

#delete an element from the tuple
#tuple_of_aadhar.delete('ramana')
#AttributeError: 'tuple' object has no attribute 'delete'

#for loop to iterate the tuple elements
for element in range(len(tuple_of_aadhar)):
    print('element =',tuple_of_aadhar[element])

