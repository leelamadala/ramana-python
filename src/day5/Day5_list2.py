"""
Day5:
"""

#read the data
list1 = []    # create a list of friends which is empty initially.

no_of_friends = input("How many friends ? ")
n = int(no_of_friends)

for i in range(n):
    friend_name = input("Enter the name of your friend # {}:".format(i+1))
    print("friend name {} is :{}".format(i+1,friend_name))
    print('-------------------------------------------------')
    list1.append(friend_name)
else:
    print("done with reading the friends names....")
    print("finally, list of friends :",list1)