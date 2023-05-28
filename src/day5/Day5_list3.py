"""
Day5:
read the friends names in a loop
append them to the emptylist
display the list of friends
sort()

"""

#read the data
list1 = []    # create a list of friends which is empty initially.

no_of_friends = input("How many friends ? ")
n = int(no_of_friends)

for i in range(n):
    friend_name = input("Enter the name of your friend # {}:".format(i+1))
    print("friend name {} is :{}".format(i+1,friend_name))
    print('-------------------------------------------------')
    list1.append(friend_name.upper())
else:
    print("done with reading the friends names....")
    print("***** list of friends :",list1)
    list1.sort()
    print("****** list of friends in sorted order is :",list1)
    print("****** convert the names in to uppercase and then print ***\n")
    print("***** modify the name of the person in index 1")
    list1[1] = list1[1] + " " + 'RAO'
    print("*************** list of values is ********\n")
    print("list1 =",list1)


