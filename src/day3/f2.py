"""
Day3: Leela Shankar - Guntur
write a program to read and also use the variables which are given
store some data and print them in some order.
"""

#read the data
name1 = input("Enter your firstname :")
name2 = input('Enter your lastname :')
m1 = input("Enter your marks in maths :")
m2 = input("Enter your marks in science :")
m3 = input("Enter your marks in social :")

print("my firstname is :",name1)
print("my lastname is :",name2)
#print("marks1 :",marks1)
#print('marks2 :',marks2)
#print('marks3 :',marks3)

#print("marks1 : {}, marks2 :{} and marks3 :{}".format(marks1,marks2,marks3))
print("marks1:{},marks2:{} and marks3:{}".format(m1,m2,m3))

#process the data - calculate total

#convert the string data into integer
m1 = int(m1)
m2 = int(m2)
m3 = int(m3)

total = (m1 + m2 + m3)
#print("total marks in three subjects is :{}".format(total))
print('marks in maths, science and social total is :{}'.format(total))
#print('marks in maths, science and social total is :{}'.format())

#




#NameError: name 'marks1' is not defined
#IndexError: Replacement index 0 out of range for positional args tuple