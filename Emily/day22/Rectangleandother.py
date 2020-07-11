
multiply = int(input('Which multiplication table would you like? '))
howhigh = int(input('How high do you want to go?'))
for whatever in range(1, howhigh+1):
    print(str(multiply) + ' x ' + str(whatever) + ' = ' + str(multiply * whatever))


##Multiplication tables with the while loop
#number = int(input('What multiplication table would you like?'))
#print("Here's your table:")
#looper = 0
#while looper < 10:
    #looper += 1
    #print(str(number) + ' x ' + str(looper) + ' = ' + str(number * looper))

#Multiplications tables with the for loop
#number = int(input('What multiplication table would you like?'))
#print("Here's your table:")
#for whatever in range(1,11):
    #print(str(number)  + ' x ' + str(whatever) + ' = ' + str(number * whatever))

#for answer in range(10, 0, -2):
    #print(answer)

#for i in range(1,6):
    #print()
    #print('i =', i, '', end='')
    #print('Hello, how ', end='')
    #if i == 3:
        #break
    #print('are you today?', end='')
#print()

#print('Type 3 to continue, anything else to quit.')
#someInput = input()
#while someInput == '3':
    #print('Thank you for the 3. Very kind of you.')
    #print('Type 3 to continue, anything else t quit.')
    #someInput = input()
#print("That's not 3, so I'm quitting now.")

#for cool_guy in ['Spongebob', 'Spiderman', 'Alan Walker', 'My Dad']:
    #print(cool_guy, 'is the coolest guy ever!')
