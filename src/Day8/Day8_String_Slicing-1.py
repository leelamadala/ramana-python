"""
slicing with strings
"""

#assign a value of bangalore to the string variable named city
city = "BANGALORE"
print('city =',city)

#indexing in reverse direction
print("city[-1] = ",city[-1])

#"BANGALORE"
print("city[-6] = ",city[-6])

#"BANGALORE"
print("city[3] = ",city[3])

#if statements  - comparision of two values
city = "BANGALORE"
if (city[3] == city[-6]):
    print("the comparision works out to be the same letter...{}".format(city[3]))
else:
    print("sorry.. comparision did not workout to be the same letter...")

print("***************************\n")

#if statements  - comparision of two values
city = "CHENNAI"
if (city[3] == city[-1]):
    print("the comparision works out to be the same letter...{}".format(city[3]))
else:
    print("sorry.. comparision did not workout to be the same letter...")
    #pass

print("thanks... for cooperating...")
#
#IndentationError: expected an indented block after 'else' statement on line 30
