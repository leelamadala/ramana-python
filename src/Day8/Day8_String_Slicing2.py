"""
slicing with strings
"""

city = 'visakhapatnam'
print("city =",city)

#positive slicing with string
#print('city[0:6] =',city[0:6])
print('city[0:7] =',city[0:7])

#output as patnam
#use positive slicing with strings
#print('city[7:12] = ',city[7:12])
#print('city[7:13] = ',city[7:13])

print('city[7:130] = ',city[7:130])

#negetive slicing with strings   - try to print patnam
#visakhapatnam
#print("city[-6:-1] = ",city[-6:-1])
print("city[-6:] = ",city[-6:])

#negetive slicing with strings - try to print visakha in
# visakhapatnam
print('city[-13:-6] =',city[-13:-6])


#if with else
if (city[0:7] == city[-13:-6]):
    print('both strings are equal... using positive and negetive slicing')
else:
    print('sorry.. strings are NOT equal...')

print('thanks..')