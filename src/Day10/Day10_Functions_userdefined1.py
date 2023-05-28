"""
user-defined funs
1. functions without parameters

syntax:
def <functionname>():
     statement1
     statement2
     ....

#call the fun
functionname()



2. fun with parameters
def <funname>(parameter1,parameter2...):
     st1..
     st2..
     ...

#call fun1
funname(p1,p2)
"""

#write a program to say welcome to the clients using funs without params

#define the fun to say welcome
def welcome_fun():
    print("Welcome to the clients of SLK Software , Pune...")
    print("We are conducting an Online Demo on Django on 20th May 23 at 9 PM IST..")

def add_fun():
    num1 = input("Enter the num1 :")
    num2 = input("Enter the num2 :")
    num11 = int(num1)
    num22 = int(num2)
    result_add = (num11 + num22)
    print('result of adding the two numbers is :',result_add)


#read the data
name = 'shankar'
print('name =',name)

#process the data -  call the fun
welcome_fun()
print("********************* add functionality ********\n")
add_fun()
#print the results
print("thanks")




#write a program to read two numbers and add them, display the result
#using funs
