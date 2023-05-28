list1 = [101,'ram','sales',44444.44,True,
         102,'shyam','marketing',55555.55, False,
         211,'girija','development',66666.66,False,
         345,'murthy','testing',99999.99,True]

print("list1 =",list1)

#process the data - iterate the list
size = len(list1)
print("size of the list is :",size)

for i in range(size):
    print("SNO # {} ---> value :{}".format(i+1,list1[i]))
    #simple if statement
    if (i == 4):
        print("----------------------------------------")
    if (i == 9):
        print("----------------------------------------")
    if (i == 14):
        print("----------------------------------------")
    if (i == 19):
        print("----------------------------------------")

else:
    print("thanks..")

