"""
list of fruits

"""

#create a list of fruits which empty list, and then add new items to it
list_of_fruits = []
print('list of fruits =',list_of_fruits)

#append a new item to it
list_of_fruits.append('kiwi')
list_of_fruits.append('mango')
list_of_fruits.append('banana')
list_of_fruits.append('guava')

print('list of fruits updated =',list_of_fruits)

#find the position
#fruit_name1 = list_of_fruits[0]
#print("fruit is :",fruit_name1)

print("fruit_name1 =",list_of_fruits[0])
print("fruit_name2 = ",list_of_fruits[1])
print('fruit_name3 =',list_of_fruits[2])
print('fruit_name4 =',list_of_fruits[3])

#print(list_of_fruits[3])

#range(max)
"""
syntax of for loop:
for <loopvariable> in <sequence>:
     statement1..
     statement2..
     ....
     
syntax2: of for loop (else part)
for <loopvariable> in <sequence>:
    statement1..
    statement2..
else:
    statement11...
    
syntax of for loop with range()
for <loopvariable> in range(min,max):
     st1..
     st2..
else:
     st3..
     
     
syntax3: for <loopvariable> in range(min,max,stepby):
              st1..
              st2..
              
         else:
               st...
    
"""

#range(min,max)    -- by default, the increment value is 1
#range(min), by default, starts with 0 as the min value
#range(min,max,stepby)  - by default , the increment value is1

print("**************** range(min,max) *******")
for i in range(0,10):
    print('i =',i)
else:
    print("done with for loop...")

print("**************** range(max) *******")
for j in range(5):    #one value here means it's max value
    print('     j = ',j)
else:
    print("done with min... in for loop")

print("**************** range(min,max,stepby) *******")
for j in range(2,22,2):
    print('j = ',j)
else:
    print("**** done with min,max,stepby")


#range(min,max,stepby)





