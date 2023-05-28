"""
Day5:
Agenda:
create a list of mixed set of values (strings,numbers, floating etc )
list operations
len()
count()
sort()
index()
"""

#read the data
#list1 = ['amala','kamala','vimala']
#print('list1 =',list1)

list1 = []    # create a list of friends which is empty initially.
friend1 = input("Enter the name of your friend1 :")
friend2 = input("Enter the name of your friend2 :")
friend3 = input("Enter the name of your friend3 :")

#process the data  - append the list of friends to the empty list
list1.append(friend1)
list1.append(friend2)
list1.append(friend3)
print("list of friends is :",list1)

#count the list of friends
size = len(list1)
print('size of the friends list =',size)

#print the results
