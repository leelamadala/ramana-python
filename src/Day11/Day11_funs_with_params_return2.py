"""
Write a program to read two numbers and perform addition operation for floating point nos
and return the result.
note: use the funs with parameters and return the value to the caller.
"""


#define star fun
def star_fun():
    print("\n*******************************************")

#define the fun1 - to ADD two numbers
def leela_add_fun(num1,num2):
    result_add = (num1 + num2)
    return(result_add)

#define the fun2 - to SUBTRACT two numbers
def leela_sub_fun(num1,num2):
    result_sub = (num1 - num2)
    return(result_sub)

#read the data - num1,num2
num1 = input("Enter your num1 :")
num2 = input("Enter your num2 :")
num1 = float(num1)
num2 = float(num2)
print("num1 : {} and num2 : {}".format(num1,num2))
star_fun()

#process the data  - call the fun
my_add_result = leela_add_fun(num1,num2)
print("result of ADDING two numbers :{} and {} is :{}".format(num1,num2,my_add_result))

my_sub_result = leela_sub_fun(num1,num2)
print("result of SUBTRACTING two numbers :{} and {} is :{}".format(num1,num2,my_sub_result))

star_fun()

#print the results
print('thanks')

