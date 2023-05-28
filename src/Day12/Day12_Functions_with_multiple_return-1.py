"""
Day12: functions with single return value
functions with multiple return values

return(x1,y1,z1...)

"""

#write a program to perform arithmatic operations (add,sub,mul,div)
#using funs with single return value
#using funs with multiple return values


#define fun1 - to ADD TWO NUMBERS
def leela_add_fun(n1,n2):
     result = (n1 + n2)
     return(result)

#define fun2 - to SUBTRACT TWO NUMBERS
def leela_sub_fun(n1,n2):
     result = (n1 - n2)
     return(result)

#define fun3 - to multiply TWO NUMBERS
def leela_mul_fun(n1,n2):
     result = (n1 * n2)
     return(result)

#define fun4 - to divide TWO NUMBERS
def leela_div_fun(n1,n2):
     result = (n1 / n2)
     return(result)

#


#read the data  -- num1,num2
num1 = int(input("Enter your num1 :"))
num2 = int(input("Enter your num2 :"))
print('num1 : {} and num2 : {}'.format(num1,num2))

#process the data - call fun1
my_result_add = leela_add_fun(num1,num2)
print("result of adding two nos is :",my_result_add)

my_result_sub = leela_sub_fun(num1,num2)
print("result of subtrating two nos is :",my_result_sub)

my_result_mul = leela_mul_fun(num1,num2)
print("result of multiplying two nos is :",my_result_mul)

my_result_div = leela_div_fun(num1,num2)
print("result of dividing two nos is :",my_result_div)

#print the results