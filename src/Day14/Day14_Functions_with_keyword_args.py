"""
Day14:
Functions with keyword arguments

def funname(p1,p2,p3,p4):
     st1..
     st2..
     ...

#call fun1
funname(v1,v2,v3,v4)
or
funname(p1=v1,p2=v2,p3=v3,p4=v4)

funname(keyword1 = value1, keyword2 = value2, keyword3 = value3...)

"""
#write a program to pass 3 vegetablenames as parameters
#and define a fun, then use the concept of keyword agruments
#pass the vegetablenames in to the parameters and perform an action

#define fun1 - to pass 3 veg names
def display_veg_names_fun(v1,v2,v3):
  #create an empty list of veg (to append veg in future)
   list_of_veg = []
   v1_up = v1.upper()
   v2_up = v2.upper()
   v3_up = v3.upper()
  #append each of the veg to the empty list
   list_of_veg.append(v1_up)
   list_of_veg.append(v2_up)
   list_of_veg.append(v3_up)
   print("list of vegetables =",list_of_veg)

   return(list_of_veg)




#read the data -
veg1 = input("Enter your favourite vegetable name1:")
veg2 = input("Enter your favourite vegetable name2:")
veg3 = input("Enter your favourite vegetable name3:")
print('veg1 = {} veg2 = {} and veg3 = {}'.format(veg1,veg2,veg3))

#process the data - call fun with keyword  args
my_list =display_veg_names_fun(v1 = veg1,v2 = veg2,v3 = veg3)

#for loop to display each of the veg
for sno,veg_name in enumerate(my_list):
    print('sno --> {} and veg name --> {}'.format(sno+1,veg_name))
else:
    print('done with vegetables')

#print the results
