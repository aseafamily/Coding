print ("Hello, this is the Minecraft choose your person and start your Adventure.")
print('''These are you choices:
-James : A famer who lives in a village
-Connor : A explorer who doesn't have a home
-Luke : A person who steals and lives near the desert temple
-Alex : A person who is a farmer and a miner. 
Choose(j/c/l/a)''')
when_you_die = 1

while when_you_die == 1:    

    choise = input()

    if choise == 'j':
        print("You are James.")
        print("You live in a village, have plenty of food, and protect the village from harm.")
        print("You have a good mine and are mining for iron and diamonds for things.")
        print('''When you do find the ores you are looking for then you will trade them with the blacksmith for armor.
        You are also looking for emeralds to trade for things like books and other things you might want.
        Then night falls and you remember that you made the iron golem to protect the village at night so there is no need to go out.''')
        print("You hear a zombies moan in the distance and the iron golem killing them.")
        print('''Then the iron golem sound goes away and the zombie sounds are still there,
        then you hear viilager screaming and shouting.''')
        print('''You think of the things you can do:
        -Put on your armor and find other things that you need and go out to fight
        or
        -Stay in bed and hope that this will go away
        or
        -Go outside with nothing and just take a look
        or
        -Look out the window and see what is happening
        You can choose(p/s/g/l)''')
        choose = input()
        if choose == 'p':
            print("You put on some armor, grab your sowrd and go outside.")
            print("There is a spider right there in front the door.")
            print("You hit the spider until dies.")
            print('''Then you see a creeper.
            You don't know what to do.
            The creeper comes closer.''')
            print("You are scared to look at the creeper.")
            print('''You think of the things that you can do:
            go to face the creeper
            or
            walk inside fast
            or
            stay still and hope that the creeper does not see you
            or
            run to the creeper and try to suprise it to scare it and make it run away
            You can choose(g/w/s/r)''')
            choose4 = input()
            if choose4 == g:
                print("You run to the creeper and hit it with your sword")
                print("It starts to flash but you keep on hitting it.")
                print("You kill it just in time.")
                print('''Or at least thats what you think.
                There are monsters all over the place.
                There are so many zombies moaning and walking to you.''')
            elif choose4 == w:
                print("You start to walk inside as fast as you can but it is to late and the creeper starts to flash.")
                print("")
        elif choose == 's':
            print("You stay put and go under the cover.")
            print("You stay there then you hear a spider hiss.")
            print("You go more under the cover.")
            print('''You hear the hiss of a creeper.
            KABOOM!!!
            You died and failed the village, maybe next time you will win.''')
            when_you_die += 1
        elif choose == 'g':
            print("You run out the door.")
            print("When you go outside a spider is right in front of you.")
            print("After a few seconds you are dead.")
            print('''You are dead!!!
            You failed your job of prtecting the village and you to dieded.
            Maybe next time you will win not lose.''')
            when_you_die += 1
        elif choose == 'l':
            print("You look out the window and see a spider right at the window.")
            print("You run to your chest and grab some things to protect your self for self denfense.")
            print("Then you hear a creeper hiss.")
            print('''You hide in the back of the room.
            KABOOM!!!
            You still are alive but mosters are everywhere.''')
        else:
            print("That was not a thing!!")
            when_you_die += 1
    elif choise == 'c':
        print("You are Connor.")
        print("You planning in a house after your last adventure.")
        print("You think about where to go.")
        print('''You think you should go to a temple because you have not been to one in a long time.
        You think that the desert temple or jungle temple might be a good idea because you have a diamond sword. 
        Then night falls and you have to go to sleep.''')
        print("You wake up but it is still night fall.")
        print('''There are mobs outside and you want to do something with them.
        You think.''')
        print('''You come up with somethings to do:
        -Stay inside and don't do anthing
        -Look and see what it is
        -Run outside to see what it is
        -Grab your things and head out.
        You can choose(s/l/r/g/)''')
        choose1 = input()
        if choose1 == s:
            print("You stay put and the cover on you.")
            print("You hear lots of mobs.")
    elif choise == 'l':
        print("You are Luke.")
        print("You are planning to make a trap in the desert temple near you.")
        print("You think that you can do it because you stole some TNT from a person.")
        print('''You want to hid in one of the traps that are inside, break it and make a new one.
        You are gathering the things you need to do this.
        Then night falls and you go to sleep.''')

    elif choise == 'a':
        print("You are Alex.")
        print("You are looking at the sky to see if it is almost night time.")
        print("You look at the sky and see that it is almost nighttime so you go inside")
        print('''When you go inside you pick up the things that you left in the fireplace to cook.
        Then you cook more and then put some things inside of the chest.
        Then you go to sleep because it is nighttime.''')

    else:
        print("What in the bla bla bla bla bla bla.")
        when_you_die += 1
