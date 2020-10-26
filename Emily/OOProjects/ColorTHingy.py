import os
os.system("cls")

#Colors
white = "\u001b[37;1m"
red = "\u001b[31;1m"
green = "\u001b[32;1m"
yellow = "\u001b[33;1m"
blue = "\u001b[34;1m"
magenta = "\u001b[35;1m"
cyan = "\u001b[36;1m"
pink = "\033[38;5;206m"

#ScrollText
import sys
def scrollTxt(text):
    for char in text:
    	sys.stdout.write(char)
    	sys.stdout.flush()
    	import time
    	time.sleep(0.0001)

#ArghModule
import random
arghColors = ['white', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'pink']
choosingColors = random.choice(arghColors)
if choosingColors == 'white':
    arghChosen = white + "Argh \n"
elif choosingColors == "red":
    arghChosen = red + "Argh \n"
elif choosingColors == "green":
    arghChosen = green + "Argh \n"
elif choosingColors == "yellow":
    arghChosen = yellow + "Argh \n"
elif choosingColors == "blue":
    arghChosen = blue + "Argh \n"
elif choosingColors == "magenta":
    arghChosen = magenta + "Argh \n"
elif choosingColors == "cyan":
    arghChosen = cyan + "Argh \n"
elif choosingColors == "pink":
    arghChosen = pink + "Argh \n"

scrollTxt(arghChosen)
import time
time.sleep(2)
scrollTxt("There are flashing colors in this; do not proceed if you are sensitive to flashing colors. You will be given five seconds to decide. \n")
scrollTxt("It goes on forever so close it when you want to. \n \n")
import time
time.sleep(5)

#ArghModule * 25
time25 = 25
x10Randomizer = True
while x10Randomizer == True:
    arghColors = ['white', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'pink']
    choosingColors = random.choice(arghColors)
    if choosingColors == 'white':
        arghChosen = white + "Argh \n"
    elif choosingColors == "red":
        arghChosen = red + "Argh \n"
    elif choosingColors == "green":
        arghChosen = green + "Argh \n"
    elif choosingColors == "yellow":
        arghChosen = yellow + "Argh \n"
    elif choosingColors == "blue":
        arghChosen = blue + "Argh \n"
    elif choosingColors == "magenta":
        arghChosen = magenta + "Argh \n"
    elif choosingColors == "cyan":
        arghChosen = cyan + "Argh \n"
    elif choosingColors == "pink":
        arghChosen = pink + "Argh \n"
    scrollTxt(arghChosen)
    time25 -= 1
    if time25 <= 0:
        break
    else:
        continue

#ArghModule Infinite
infinite = True
while infinite == True:
    arghColors = ['white', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'pink']
    choosingColors = random.choice(arghColors)
    if choosingColors == 'white':
        arghChosen = white + "Argh \n"
    elif choosingColors == "red":
        arghChosen = red + "Argh \n"
    elif choosingColors == "green":
        arghChosen = green + "Argh \n"
    elif choosingColors == "yellow":
        arghChosen = yellow + "Argh \n"
    elif choosingColors == "blue":
        arghChosen = blue + "Argh \n"
    elif choosingColors == "magenta":
        arghChosen = magenta + "Argh \n"
    elif choosingColors == "cyan":
        arghChosen = cyan + "Argh \n"
    elif choosingColors == "pink":
        arghChosen = pink + "Argh \n"
    scrollTxt(arghChosen)
    continue
