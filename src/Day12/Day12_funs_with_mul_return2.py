"""
Day12: functions with single return value
functions with multiple return values

return(x1,y1,z1...)

"""
#write a program to perform arithmatic operations (add,sub,mul,div)
#using funs with multiple return values

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


#read the data  -- num1,num2
num1 = int(input("Enter your num1 :"))
num2 = int(input("Enter your num2 :"))
opr = input("Enter the Arithmatic Operation (ADD,SUB,MUL,DIV) : ")
print('num1 :{} and num2 :{} Operation is :{}'.format(num1,num2,opr))

if (opr == 'ADD'):
    print('Operation to be performed is : ADDITION!')
elif(opr == 'SUB'):
    print('Operation to be performed is : SUBTRACTION!')
elif(opr == 'MUL'):
    print('Operation to be performed is : MULTIPLICATION!')
elif (opr == 'DIV'):
    print('Operation to be performed is : DIVISION!')

#process the data - call fun1
result = leela_ARITHMATIC_OPS_fun(num1,num2,opr)
print('result =',result)








"""
print("result of ADDING two nos is :",r1)
print("result of SUBTRACTING two nos is :",r2)
print("result of MULTIPLYING two nos is :",r3)
print("result of DIVIDING two nos is :",r4)
print(r5)
"""
