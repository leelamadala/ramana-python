#write a program to read positive and negetive indexes(staring and ending index)
# for a city and compare the resultant strings,
#display appropriate message "Strings are equal" or "Strings are ot equal

#read the data
city = input("Enter the city name :")
print('city =',city)

pos_ind_source_val = 0
pos_ind_target_val = 7

neg_ind_source_val = -13
neg_ind_target_val = -6

#process the data - compare the values
#if with else
if (city[0:7] == city[-13:-6]):
    print('both strings are equal... using positive and negetive slicing')
else:
    print('sorry.. strings are NOT equal...')

#display the results
print('thanks..')


#NameError: name 'city' is not defined

