"""
Write a program to read two numbers and perform addition operation
and display the sum/result.
note: use the funs with parameters
"""
#define star fun
def star_fun():
    #print("*******************************************\n")
    print("\n*******************************************")


#define the fun1 - to ADD two numbers
def leela_add_fun(num1,num2):
    #print("testing add fy")
    result_add = (num1 + num2)
    print("result of adding two numbers :{} and {} is :{}".format(num1,num2,result_add))

#define the fun2 - to SUBTRACT two numbers

#read the data - num1,num2
star_fun()
num1 = input("Enter your num1 :")
num2 = input("Enter your num2 :")
num1 = int(num1)
num2 = int(num2)
print("num1 : {} and num2 : {}".format(num1,num2))
star_fun()
#process the data  - call the fun
leela_add_fun(num1,num2)
star_fun()
#print the results
print('thanks')


#TypeError: leela_add_fun() missing 2 required positional arguments: 'num1' and 'num2'
