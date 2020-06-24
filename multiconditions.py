country = input("What country are you from? ")

if country =='USA':
    state = input("What state are you from? ")
    if state in ('Illinois', 'Ohio'):
        tax = 0.1
    elif state == 'Alabama':
        tax = 0.07
    elif state == 'Idaho':
        tax = 0.01
    else:
        tax = 0.5
else:
    tax = 0.0
print (tax)

