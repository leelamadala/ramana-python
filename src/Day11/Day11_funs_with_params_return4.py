"""
Write a program to read two numbers and perform
all the arithmatic operations like addition,subtraction,multiplication,division
 modulus  operation for floating point nos
and return the results.
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

#define the fun3 - to MULTIPLY two numbers
def leela_mul_fun(num1,num2):
    result_mul = (num1 * num2)
    return(result_mul)

#define the fun4 - to DIVIDE two numbers
def leela_div_fun(num1,num2):
    result_div = (num1 / num2)
    return(result_div)

#define the fun5 - to modulus of two numbers
def leela_mod_fun(num1,num2):
    result_mod = (num1 % num2)
    return(result_mod)




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

my_mul_result = leela_mul_fun(num1,num2)
print("result of MULTIPLYING two numbers :{} and {} is :{}".format(num1,num2,my_mul_result))

my_div_result = leela_div_fun(num1,num2)
print("result of DIVIDING two numbers :{} and {} is :{}".format(num1,num2,my_div_result))

star_fun()

my_mod_result = leela_mod_fun(num1,num2)
print('modulus is :',my_mod_result)
#print the results
print('thanks')


"""  output of modulus 
Enter your num1 :10
Enter your num2 :3
num1 : 10.0 and num2 : 3.0

*******************************************
result of ADDING two numbers :10.0 and 3.0 is :13.0
result of SUBTRACTING two numbers :10.0 and 3.0 is :7.0
result of MULTIPLYING two numbers :10.0 and 3.0 is :30.0
result of DIVIDING two numbers :10.0 and 3.0 is :3.3333333333333335

*******************************************
modulus is : 1.0
thanks
"""

#ZeroDivisionError: float division by zero
