import easygui

when_you_die = 1

while when_you_die == 1:    

    choise = easygui.buttonbox ('''Hello, this is the Minecraft choose your person and start your Adventure.
These are you choices:
-James : A famer who lives in a village
-Connor : A explorer who doesn't have a home
-Luke : A person who steals and lives near the desert temple
-Alex : A person who is a farmer and a miner. 
Choose(j/c/l/a)''',
                   choices=['j', 'c', 'l', 'a'])

    if choise == 'j':
        easygui.msgbox('''You are James.
        You live in a village, have plenty of food, and protect the village from harm.
        You have a good mine and are mining for iron and diamonds for things.
        When you do find the ores you are looking for then you will trade them with the blacksmith for armor.
        You are also looking for emeralds to trade for things like books and other things you might want.''')
        choose = easygui.buttonbox('''Then night falls and you remember that you made the iron golem to protect the village at night so there is no need to go out.
        You hear a zombies moan in the distance and the iron golem killing them.
        Then the iron golem sound goes away and the zombie sounds are still there,
        then you hear viilager screaming and shouting.
        You think of the things you can do:
        -Put on your armor and find other things that you need and go out to fight
        or
        -Stay in bed and hope that this will go away
        or
        -Go outside with nothing and just take a look
        or
        -Look out the window and see what is happening
        You can choose(p/s/g/l)''',
                                   choices=['p', 's', 'g', 'l'])

        if choose == 'p':
            easygui.buttonbox('''You put on some armor, grab your sowrd and go outside.
            There is a spider right there in front the door.
            You hit the spider until dies.
            Then you see a creeper.
            You don't know what to do.
            The creeper comes closer.''')
        elif choose == 's':
            easygui.msgbox('''You stay put and go under the cover.
            You stay there then you hear a spider hiss.
            You go more under the cover.
            You hear the hiss of a creeper.
            KABOOM!!!
            You died and failed the village, maybe next time you will win.''')
            when_you_die += 1
        elif choose == 'g':
            easygui.msgbox('''You run out the door.
            When you go outside a spider is right in front of you.
            After a few seconds you are dead.
            You are dead!!!
            You failed your job of prtecting the village and you to dieded.
            Maybe next time you will win not lose.''')
            when_you_die += 1
        else:
            easygui.buttonbox('''You look out the window and see a spider right at the window.
            You run to your chest and grab some things to protect your self for self denfense.
            Then you hear a creeper hiss.
            You hide in the back of the room.
            KABOOM!!!
            You still are alive but mosters are everywhere.''')
    elif choise == 'c':
        easygui.msgbox('''You are Connor.
        You planning in a house after your last adventure.
        You think about where to go.
        You think you should go to a temple because you have not been to one in a long time.
        You think that the desert temple or jungle temple might be a good idea because you have a diamond sword. 
        Then night falls and you have to go to sleep.''')
        choose1 = easygui.buttonbox('''You wake up but it is still night fall.
        There are mobs outside and you want to do something with them.
        You think.
        You come up with somethings to do:
        -Stay inside and don't do anthing
        -Look and see what it is
        -Run outside to see what it is
        -Grab your things and head out.
        You can choose(s/l/r/g/)''')
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

    else:
        print("You are Alex.")
        print("You are looking at the sky to see if it is almost night time.")
        print("You look at the sky and see that it is almost nighttime so you go inside")
        print('''When you go inside you pick up the things that you left in the fireplace to cook.
        Then you cook more and then put some things inside of the chest.
        Then you go to sleep because it is nighttime.''')
