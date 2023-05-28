"""
how to iterate over the list of values using a for loop
"""

#read the data
list_of_fruits = ['banana','apple','kiwi','pine-apple']
print("list of fruits =",list_of_fruits)

fruit_name = input("Enter the fruit name :")
print('fruit_name =',fruit_name)

#process the data
#find the size of list - len()
n = len(list_of_fruits)
print('no. of fruits originally =',n)

#how to iterate over the list using the size
for i in range(0,len(list_of_fruits)):
    #print('i =',i)
    #print(list_of_fruits[i])
    print('fruit # {} ---> fruit name :{}'.format(i,list_of_fruits[i]))
else:
    print("******* done with for loop *******\n")

#append the new item
list_of_fruits.append(fruit_name)
print('updated list =',list_of_fruits)