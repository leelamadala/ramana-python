"""
negetive slicing with strings
"""

str = 'calcutta'
print('str =',str)

#size of the given string
print("size = ",len(str))

#negetive indexing  -'calcutta'
my_val = str[-1]
print('my_val =',my_val)

#IndexError: string index out of range
#my_val2 =str[7]

#negetive indexing   - calcutta
my_val2 =str[-1]

#print('positive slicing of string is:',my_val2[7])
#print('positive slicing of string is:',my_val2[6])
print('my_val2 =',my_val2)

#calcutta
str1 = 'calcutta'
print('str1 =',str1)

#negetive indexing -- find the position of the letter 'u'
neg_slice = str1[-4]
print('letter at the given position using negetive slicing =',neg_slice)