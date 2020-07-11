import random, easygui
secert = random.randint(1, 100)
guess = 0
tries = 0
easygui.msgbox('''Hi, you have 6 tries to get my secert number.
It is from 1-100. ''')
while guess != secert and tries < 6:
    guess = easygui.integerbox("Please guess.", upperbound=100)
    if not guess: break
    if guess < secert:
        easygui.msgbox(str(guess) + " thats to low.")
    elif guess > secert:
        easygui.msgbox(str(guess) + " thats to high.")
    tries = tries + 1
if guess == secert:
    easygui.msgbox("You have my secert number.")
else:
    easygui.msgbox("Ran out of guess. My number was " + str(secert) + ".")
