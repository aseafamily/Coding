#Pre-Variables
day_choose = 1
night_choose = 2
is_royal = 101

#Welcome and Name
print("Greetings. We are about to get involved in random stories. To get started, please enter your name.")
title = input()

#Greetings
print("Hello " + str(title) + "!")

#Gender
print("Oh, and one last thing: are you a lord, or a lady? (Type in 'Lord' or 'Lady')")
gender = input()
fullname = gender + " " + title
#Greetings 2
print("Ah, it is" + " " + fullname + "? Thank you. I will verify your status of royal enrollment...")
import time
time.sleep(3)
if gender == "Lady":
    print("Yes, how could I forget? It is you," + " " + fullname + ".")
    print("Now we can continue.")
    import time
    time.sleep(2)
elif gender == "Lord":
    print("Yes, how could I forget? It is you," + " " + fullname + ".")
    print("Now we can continue.")
    import time
    time.sleep(2)
elif gender != "Lady" or "Lord":
    print("It does not appear if you are enrolled, so I cannot allow you to proceed.")
    print("Do you dare to argue against me? Y/N")
    var = input()
    import time
    time.sleep(1)
    if var == "Y":
        print("Aha, you do dare!")
        import time
        time.sleep(0.5)
        print("You are not permitted to play the game if you are a peasant!")
        print("You must leave, Peasant" + " " + title + "! (Remember to type 'Lord' or 'Lady' at the beginning without any spaces!)")
        import sys
        sys.exit()
    elif var == "N":
        print("Thank you for your efforts in trying to apply, but I'm afraid you must leave.")
        print("Remember to type 'Lord' or 'Lady' at the begininng without any spaces!")
        import sys
        sys.exit()
    elif var != "Y" or "N":
        print("Program is quitting, you have not enrolled! \n Remember to type 'Lord' or 'Lady' at the beginning without any spaces!")
        import sys
        sys.exit()
    else:
        print("Remember to type 'Lord' or 'Lady' at the beginning without any spaces!")
        import sys
        sys.exit()
#Beginning intro
print("Would you like the time to be day or night? Or would you like to quit? (Type in 'D' for day, 'N' for night, or type 'Quit' to stop running. \n Typing anything else will cause the program to stop.)")
setting = input()
import time
time.sleep(1)
#Start for Daytime, intro, path description
if setting == "D":
    day_choose = "Day"
    night_choose = "NotNight"
    print("Daylight is... always depicted as warm and promising, full of potential and sunlight.")
    print("But sunlight can burn and potential can be wasted.")
    print("Day may be innocent on the surface, but sometimes the greatest tragedies lie in the light of day.\n")
    import time
    time.sleep(4)
    print("Here you are, just as the sun rises.\n You, the last descendent of Meis--the goddess of light--have decided to train in your ancestor's ways due to a mysterious vision she had sent to you. \n")
    print("A little bit about Meis for you," + " " + fullname + "... \n")
    import time
    time.sleep(3)
    print("Meis was a young child with an exceptional prowess for light auras.")
    print("Early on, as a peasant, she was scorned by many who could not see below the surface.")
    print("But as she grew, she became more well known... and not just because of her abilities.")
    print("It was soon learned that she was the daughter of the god Irin, and she was swept up to the Otherworld to live as a goddess. \n")
    import time
    time.sleep(6)
    print("Meis lived a life of immortality and youth...")
    print("But will you unlock the her secret of immortality in the right way...")
    print("Or will you fail and perish, descendant of Meis? \n")
    print("But before embarking on your quest to learn her secrets, you must choose a path to pursue.")
    import time
    time.sleep(3)
    print("Meis's two Paths of Day are for different people...")
    print("So you must choose between these two paths: \n Path of Light \n Path of Warmth")
    import time
    time.sleep(3)
#Start for Nighttime, intro, path description
elif setting == "N":
    night_choose = "Night"
    day_choose = "NotDay"
    print("It is peculiar that you chose the night... not many dare to traverse this path.")
    print("But darkness can hide the greatest secrets.")
    print("Even though most monsters decide to hide in the night where you will be...")
    print("You can harness those monsters and your own shadow. \n")
    import time
    time.sleep(4)
    print("The gentle, silent goddess of darkness--your ancestor Lumi--watches you as you arrive with dusk, pleased with your decision to act on the mysterious vision she had sent you.")
    print("Hear about Lumi for a bit," + " " + fullname + ". \n")
    import time
    time.sleep(3)
    print("Lumi, a young girl living in the shadow of her older brother--the god Sadani--was always very quiet.")
    print("Everyone thought that Sadani would take the place of god/goddess of darkness...")
    print("But in the battle to inherit the throne of the god/goddess of shadow...")
    print("Your ancestor unleashed her hidden power and defeated her brother.")
    print("Then she was never questioned again, and reigned supreme. \n")
    import time
    time.sleep(6)
    print("She lived a life of beauty and power...")
    print("But will you unlock the secret of her power in the right way...")
    print("Or will you fail and perish, descendant of Lumi? \n")
    print("But before embarking on your quest to find her secrets, you must choose a path to pursue.")
    import time
    time.sleep(3)
    print("Lumi's two Paths of Night are for different people...")
    print("So you must choose between these two paths: \n Path of Celestials \n Path of Shadows")
    import time
    time.sleep(3)
#Anything else hopefully
else:
    print("All right. But these stories will be there if you ever need them...")
    import sys
    sys.exit()

#Continuing with Daytime!
if day_choose == "Day" and night_choose == "NotNight":
    print("Choose between 'L' for Light, and 'W' for Warmth:")
    print("Path of Light")
    print("Path of Warmth")
    day_path = input()
    if day_path == "L":
        print("Light")
        print("You have chosen the Day Path of Light.")
    elif day_path == "W":
        print("Warmth")
        print("You have chosen the Day Path of Warmth.")
    elif day_path != "L" or "W":
        print("Meis has kicked you out due to your inability to type a letter. ;P")
else:
    pass
#Continuing with Nighttime!
if night_choose == "Night" and day_choose == "NotDay":
    print("Choose between 'C' for Celestials, and 'S' for Shadows:")
    print("Path of Celestials")
    print("Path of Shadows")
    night_path = input()
    if night_path == "C":
        print("You have chosen the Night Path of Celestials.")
    elif night_path == "S":
        print("You have chosen the Night Path of Shadows.")
    elif night_path != "C" or "S":
        print("Lumi has kicked you out due to your inability to type a letter. ;P")
        import sys
        sys.exit()
else:
    print()
