"""
Day13:
functions with default arguments

default arguments are those which are defined/passed with value
 at the time of defining the function.

syntax:
def funname(param1,param2,param3=40):
   st1..
   st2..
   ...


#call the fun with default arg
#funname(val1,val2)
funname(val1,val2,val3)

Note: At the time of calling the function,
We NEED NOT pass any value to the parameter which is defined
with default value

"""

#write a program to read your marks in English, Telugu, Hindi
# and define hindi marks with default passing score of 24 out of 100.
#and for English and Telugu, the pass marks is 35.
#calculate the total scrore in english,telugu and hindi


#define fun2 - to add the float marks
def add_float_marks(m1,m2,m3):
    return(m1 + m2 + m3)





#define default value fun1  -  to convert the given marks into float
def convert_to_float(p1,p2,p3=24):
    marks_eng_flo = float(p1)
    marks_tel_flo = float(p2)
    marks_hin_flo = float(p3)
    return(marks_eng_flo,marks_tel_flo,marks_hin_flo)

#define star fun
def star_fun(param_format= "*** ",count = 10):
    #param_format = "*** " * count
    new_param_format = param_format * count
    print(new_param_format)

#read the data - eng,tel,hin
stud_name = input("Enter the Student First_Name :")
marks_eng = input("Enter your marks in English :")
marks_tel = input("Enter your marks in Telugu :")
marks_hin = input('Enter your marks in Hindi :')

#process the  - convert the marks in to float - call convert_to_float_fun
m1,m2,m3 = convert_to_float(marks_eng,marks_tel,marks_hin)
star_fun()
print("floating point marks in English :",m1)
print("floating point marks in Telugu :",m2)
print("floating point marks in Hindi :",m3)

#process the data - add float marks
#function with keyword args
star_fun(count = 16)
#star_fun("--- ",16)
my_lang_tot_marks =add_float_marks(m1,m2,m3)
print("total marks scored by the student :{} in 3 languages :{}".format(stud_name,my_lang_tot_marks))


#print the results


