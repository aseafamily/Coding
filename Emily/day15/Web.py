quarters = int(input('How many quarters do you have?'))
dimes = int(input('How many dimes do you have?'))
nickles = int(input('How many nickles do you have?'))
pennies = int(input('How many pennies do you have?'))
if quarters < 0 or dimes < 0 or nickles < 0 or pennies < 0:
    print('*gasp THAT IS ILLEGAL!')
else:
    totalquarters = quarters * 25
    totaldimes = dimes * 10
    totalnickles = nickles * 5
    totalpennies = pennies * 1
    totalcents = totalquarters + totaldimes + totalnickles + totalpennies
    print('You total amount of spare change in cents is ' + str(totalcents) + ' cents.')
    totaldollars = totalcents/100
    print('Your total amount of cents in dollars is $' + str(totaldollars) + '.')


#width = float(input('What is the width, in feet of the rectangular room?'))
#length = float(input('Now what is the length, in feet of the rectangular room?'))
#priceperyard = float(input('One more thing, how much does the carpet cost per square yard.'))
#if priceperyard <= 0:
    #print('The carpet is free!')
#else:
    #area_in_feet = width * length
    #are_in_yards = area_in_feet/9
    #total_cost_of_carpet = priceperyard * are_in_yards
    #print('The total amount of carpet needed to cover the room is ' + str(area_in_feet) + ' feet.')
    #print('The total amount of carpet need to cover the room, in yards, is ' + str(are_in_yards) + '.')
    #print('The total cost of the carpet is' + '$' + str(total_cost_of_carpet) + '.')


#firstname = input('Please enter your first name:')
#lastname = input('Now please enter your last name:')
#print(firstname + ' ' + lastname)

#print('My ', end='')
#print('name ', end='')
#print('is ', end='')
#print('Emily.', end='')
#import urllib.request
#file = urllib.request.urlopen('http://helloworldbook3.com/data/message.txt')
#message = file.read()
#print(message)
