from random import *
number = randint(1,100)
running = 1
tries = 0
while running == 1:    
    guess = int(input('''Please guess my number. It's from 0 - 100.
'''))
    tries = tries +1
    if guess > number :
        print("Your guess is larger than my number. You tried " + str(tries) + " times.")
    elif guess < number :
        print('Your guess is smaller than mine. You tried ' + str(tries) + ' times.')
    else:
        print('You guessed my number. You tried ' + str(tries) + ' times.')
        running = 0

#How to print variables that aren't numbers
    # name = "this can be anything you want"
    # print("Hello World " + name)