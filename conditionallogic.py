price = input ('Please enter the price you paid ')
price = float (price)

if price > 1.00:
    tax = 0.07
else:
    tax = 0
total = price * tax
print ('Tax is' + str(total))