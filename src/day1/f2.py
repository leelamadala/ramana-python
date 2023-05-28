"""
variable naming conventions

1. variable names should start with alphabets (A to Z or a to z)
2. variable names can have numbers, but it should NOT start with a number
3. variable names can also start with underscore (_)
4. variable names should NOT have spaces inbetween two parts.
5. Variable names allows camelcase
6. variable names cannot have special chars like %^& except underscore

"""
#valid variable name
name = 'ramana'
print('name =',name)

#valid variable name, as it's starting with an alphabet (cap or small is ok)
Name = 'Shankar'
print("Name =",Name)

#valid
NAME = 'leela shankar'
print('NAME =',NAME)

# invalid variable
# 123name = 'ramana'

# valid name
name123 = 'ramana'

# valid variable name as per python, but it's NOT a good practice
first123name = 'ramana'

# it's not recommended to use _ in the beginning of the word
_name = 'ramana'
_college = 'Loyola'

print("my name is :",_name)

#valid and recommended practice
first_name = 'ramana'

savings_account_number = 1234556

savings_acc_no = 222
current_acc_no = 333
rd_acc_no = 2232332
loan_acc_no = 'LT23455'
electical_bill_val_sep23 = 888

Feb_salary = 99999.99
#feb sal = 9999


#camel case is allowed
febSal = 99999

febMonthSalRs = 9888888
janMonthSalDollars = 1000
marMonthSal_USD = 222

#invalid
g123456 = 'ramana'

#special char $ is NOT allowed
#first$name = 'ramana'
#first%name = 'ramana'

# first_name = 'ramana'
# first-name = 'murthy'

# FirstName
