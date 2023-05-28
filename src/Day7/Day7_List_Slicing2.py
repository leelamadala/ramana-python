"""
slicing with strings:
   indexing with strings
"""

city = 'Bangalore'
print("city =",city)

#size of city
size = len(city)
print('size =',size)

#index

letter1 = city[0]
letter2 = city[1]
letter3 = city[2]
letter4 = city[3]
letter5 = city[4]

print("{} - {} - {} - {} - {}".format(letter1,letter2,letter3,letter4,letter5))


#use a for loop and append the letters to an empty list
list1 = []
print('list1 is empty :',list1)

#use a for loop and append each of the letters till position 3 to the empty list
#and display the list
for i in range(len(city)):
    print(" i = {} and letter :{}".format(i,city[i]))


#slicing with strings
city_new = 'Hyderabad'
print("new city =",city_new)

#Hyder
my_str =city_new[0:5]
print("my str =",my_str)

#Hydera
my_str2 =city_new[0:6]
print("my str2 =",my_str2)

#Hyderabad
my_str3 =city_new[0:9]
print("my str3 =",my_str3)

#rab
my_str4 = city_new[4:7]
print('my str4 =',my_str4)

#bad
my_str5 = city_new[6:9]
print('my str5 =',my_str5)

#pune
str_city = 'pune'
my_str6 = str_city[0:4]
print('my_str6 =',my_str6)

#empty, before colon (will start from 0th position)
my_str66 = str_city[:4]
print('my_str66 =',my_str66)

#un
my_str7 = str_city[1:3]
print('my_str7 =',my_str7)

#pune
my_str8 = str_city[0:4]
print('my_str8 =',my_str8)

#empty, after colon (will continue  till end position)
my_str9 = str_city[0:]  #by default, it will go till the end
print('my_str9 =',my_str9)

#ne
my_str10 = str_city[2:4]  #by default, it will go till the end
print('my_str10 =',my_str10)

#ne  with empty , next to colon
my_str11= str_city[2:]  #by default, it will go till the end
print('my_str11 =',my_str11)

state = 'telangana'
print('state = ',state)

my_output = state[:]
print('my_output =',my_output)
