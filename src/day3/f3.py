"""
Day3: Leela Shankar - Guntur
write a program to read and also use the variables which are given
store some data and print them in some order, using the format()
use float(), int() etc funs
"""

#read the data
name1 = input("Enter your firstname :")
name2 = input('Enter your lastname :')
marks_subject1 = input("Enter your marks in maths :")
marks_subject2  = input("Enter your marks in science :")
marks_subject3 = input("Enter your marks in social :")

print("**********************************************\n")
print("my firstname is :",name1)
print("my lastname is :",name2)
print("**********************************************\n")
maths_marks = marks_subject1
science_marks = marks_subject2
social_marks = marks_subject3

print("marks1:{},marks2:{} and marks3:{}".format(maths_marks,science_marks,social_marks))

#process the data - convert the string data into float
m1 = float(maths_marks)
m2 = float(science_marks)
m3 = float(social_marks)

total = (m1 + m2 + m3)
print('marks in maths, science and social total is :{}'.format(total))
print("*************************************************\n")

#calculate the avg marks of 3 subjects
avg = (total/3)
print('avg marks in given three subjects is :{}'.format(avg))
print("*************** Thanks *****************")




#ValueError: could not convert string to float: ''