firstName = input('Please enter your first name: ')
lastName = input('Please enter your last name: ')
# print ('Hello ' + firstName.capitalize() + ' ' + lastName.capitalize())
output = 'Hello, {0} {0}' .format (firstName, lastName)
print (output)
output = f'Hello, {firstName}, {lastName}'
print (output)