def totalchange(quarters, dimes, nickels, pennies):
    total = quarters*25 + dimes*10 + nickels*5 + pennies
    return total
quarters25 = float(input('How many quarters?'))
dimes10 = float(input('How many dimes?'))
nickles5 = float(input('How many nickles?'))
pennies1 = float(input('How many pennies?'))
printtotal = totalchange(quarters25, dimes10, nickles5, pennies1)
print('$' + str(printtotal/100))

##def question2(name, address, street, city, state, postalcode, country):
##    print(name)
##    print(address + ',', street)
##    print(city + ',' +  state, ',', country)
##    print(postalcode)
##question2(input('What is your name?'), input('What is your address?'), input('What is your street?'), input('What is your city?'), input('What is your state or province?'), input('What is your postalcode?'), input('What country do you live in?'))


##def letters():
##    print('Emily')
##letters()

##def calculateTax(price, tax_rate):
##    total = price + (price * tax_rate)
##
##    my_price = 10000
##    print('my_price (inside function) - ', my_price)
##    return total
##
##my_price = float(input('Enter a price: '))
##totalPrice = calculateTax(my_price, 0.06)
##print('price = ', my_price, 'Total price =', my_price)
##print('my_price (outside function) = ', my_price)

##def calculateTax(price, tax_rate):
##    total = price + (price * tax_rate)
##    print(my_price)
##    return total
##
##my_price = float(input('Enter a price: '))
##totalPrice = calculateTax(my_price, 0.06)
##print('price = ', my_price, 'Total price =', totalPrice)

##def calculateTax(price, tax_rate):
##    total = price + (price * tax_rate)
##    return total
##
##my_price = float(input('Enter a price: '))
##totalPrice = calculateTax(my_price, 0.1)
##print('price = ', my_price, ' Total price = ', totalPrice)

##def calculateTax(price, tax_rate):
##    taxTotal = price + (price * tax_rate)
##    return taxTotal
##totalprice = calculateTax(7.99, 9.06)
##print(totalprice)
##total = calculateTax(7.99, 0.06) + calculateTax(6.59, 0.08)
##print(total)

##def printMyAddress(aName, houseNum):
##    print(aName)
##    print(houseNum, 'NE 110th Way')
##    print('Redmond, Washington, USA')
##    print('98052')
##    print()
##printMyAddress('neighbor1', '67870')
##printMyAddress('Emily Ma', '546576')
##printMyAddress('Andrew Ma', '12345')
##printMyAddress('Alex Ma', '4623768')
##printMyAddress('Sherri Li', '2q43656758')
