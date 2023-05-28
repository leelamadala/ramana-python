"""
Day12: functions with single return value
functions with multiple return values

return(x1,y1,z1...)

"""
#write a program to perform arithmatic operations (add,sub,mul,div)
#using funs with multiple return values

#define fun1 - to perform all arithmatic operations, keeping the operation as parameter)
def leela_ARITHMATIC_OPS_fun(num1,num2,operation):
    if (operation == 'ADD'):
        res_add = (num1 + num2)
        return(res_add)
    elif (operation == 'SUB'):
        res_sub = (num1 - num2)
        return(res_sub)
    elif (operation == 'MUL'):
        res_mul = (num1 * num2)
        return(res_mul)
    elif (operation == 'DIV'):
        res_div = (num1 / num2)
        return(res_div)
    else:
        res_other = "perform any valid arithmatic operation!!"
        return(res_other)


#define a fun1 - to read the data
def leela_read_data_fun():
    num1 = int(input("Enter your num1 :"))
    num2 = int(input("Enter your num2 :"))
    opr = input("Enter the Arithmatic Operation (ADD,SUB,MUL,DIV) : ")
    print('num1 :{} and num2 :{} Operation is :{}'.format(num1, num2, opr))
    return(num1,num2,opr)

#read the data  -- num1,num2
my_num1,my_num2,my_opr = leela_read_data_fun()

if (my_opr.upper() == 'ADD'):
    print('Operation to be performed is : ADDITION!')
elif(my_opr.upper() == 'SUB'):
    print('Operation to be performed is : SUBTRACTION!')
elif(my_opr.upper() == 'MUL'):
    print('Operation to be performed is : MULTIPLICATION!')
elif (my_opr.upper() == 'DIV'):
    print('Operation to be performed is : DIVISION!')


#process the data - call fun1
result = leela_ARITHMATIC_OPS_fun(my_num1,my_num2,my_opr.upper())
print('result =',result)








"""
print("result of ADDING two nos is :",r1)
print("result of SUBTRACTING two nos is :",r2)
print("result of MULTIPLYING two nos is :",r3)
print("result of DIVIDING two nos is :",r4)
print(r5)
"""
