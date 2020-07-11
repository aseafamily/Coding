print('Hello! Welcome to the Adventure Story. To get started, please enter your name.')
name = input()
print('Hello ' + str(name) + "!")
print('Now, please choose a character, the options are...')
print('''Oracle - A famous future-teller who works for the King and worries about her public image.
Tyhnim - Oracle's son, a new apprentice who's talent isn't quite at it's peak yet.
Ellena - An orphan, who seems to have a successful life ahead.
Nym - Who despite his privelleged past is struggling with the new demands of reality.''')
print('Who do you want to choose? (O/T/E/N)')
character = input()

if character == 'O':
    print('You chose Oracle.')
    print('Now for some background knowledge:')
    print('''Oracle graduated from the apprentice stage twelve years ago and was immeditely assigned a lower rank position because of her family's status.
Her oveseer noticed her talent for future-seeing, and moved her up after a couple moonrises(months).
She kept moving steadiliy up, gaining little attention, until she replaced one of the king's assistants and guided a prince to the throne.
King Ares hired her after that, and she became famous and known for her precise future-seeing.
She birthed a son, Tyhnim, about a dozen moonrises after she started working for the king, and started spending a little less time on her job.
This was probably the reason why her talent slowly decreased, but no one really noticed... yet.
''')
    print("Now let's get started, are you ready to continue you? (y/n)")
    ready = input()
    if ready == 'y':
        print("Alright then! Let's get started!")
        print('''When Oracle awoke and looked outside, she was already late for work.
She closed her eyes, trying to pretend it was just a dream, but only humans had dreams, so she threw off the covers and leapt out of bed.
She raced through the maze of hallways in her spacious house, pausing only to smile hurridedly at her son, Tyhnim, before she was out the door.
As she telerided through all of the stations that led to the castle, she inwardly cursed herself for sleeping in.
It wasn't exactly her fault though, she had spent the night trying to help Tyhnim apply to new jobs, and had a fitful sleep.
She wondered how she was going to explain that to the king...
But when she approaced the small but majestic castle, and saw the guard's stern face, she knew that she only had two choices.
1. Plead for forgiveness and explain
2. Try this new-fangled excuse down on earth called a lie...
(1/2)
''')
        
    elif ready == 'n':
        print('Waiting... waiting... press y to start.')
        readyagain = input()
        if readyagain == 'y':
            print("Alright then! Let's get started!")
    else:
        print('Sorry, that is not an option.')

elif character == 'T':
    print('You chose Tyhnim.')
    print('Now for some background knowledge:')
    print('''Tyhnim was born to Oracle and an unknown father, instantly being born into a famous family.
He strived to meet the expectations that were set out before him moonrises before he was born, and just barely completed them.
Currently, he just graduated from the apprentice stage, and is expecting a high-ranked position, due to his family.
Despite being under a lot of pressure, he still manages to have fun and is relaxed most of the time.
Even though he has a famous doting mother, he stil wonders about his father, whom he never met.
He feels his talent deep inside it, but only manages to cling onto it, not fully envelop it, which is drawing a couple critics, but not much... for now anyways.
''')
    print("Now let's get started, are you ready to continue you? (y/n)")
    ready = input()
    if ready == 'y':
        print("Alright then! Let's get started!")
        print('''Tyhnim crept through the early morning, hurrying to the mailbox, hoping for a job acceptance.
He reached his hand into the box, hoping for the slight brush and crinkle of a letter.
As his fingertips reached the end of the box, he sighed with dissapointment, and turned around to head home, when a crinkle of paper underneath him startled him.
Stooping down, he realizes it's a letter. It must have fluttered out when he opened it.
Tyhnim opens it with trembling hands, and to his delight, it's an acceptance letter.
As he reads on, he slowly realizes how low the job is. He would be working just above what his mother did when she just graduated from apprentice stage.
He has two options:
1. Accept his new job, even though the low rank might draw criticism.
2. Ignore it and wait hopefully for a higher job.
''')
    elif ready == 'n':
        print('Waiting... waiting... press y to start.')
        readyagain = input()
        if readyagain == 'y':
            print("Alright then! Let's get started!")
    else:
        print('Sorry, that is not an option.')

elif character == 'E':
    print('You chose Ellena.')
    print('Now for some background knowledge:')
    print('''Ellena is an orphan, her parents either dead or alive but not caring about her.
However, she doesn't really care about them and is focusing all her attention on her new job, which she got right after graduating.
It is clear to everyone that she has enourmous talent, as well as ambition, and is becoming a very talented guider and future-seer.
Her only weakness apparent to her overseer is her inablity to connect with her assigned human, but that hardly ever gets in the way and is usually ignored.
Though she does ocassionaly wonder about her parents, and though she does get questioned by the orderers(police) about them, they are off her mind almost all of the time.
Her idol is Oracle, and she hopes to work for the king one day, which is likely, based on how quickly she is improving.
''')
    print("Now let's get started, are you ready to continue you? (y/n)")
    ready = input()
    if ready == 'y':
        print("Alright then! Let's get started!")
    elif ready == 'n':
        print('Waiting... waiting... press y to start.')
        readyagain = input()
    if readyagain == 'y':
            print("Alright then! Let's get started!")
    elif ready == 'n':
        print('Waiting... waiting... press y to start.')
        readyagain = input()
        if readyagain == 'y':
            print("Alright then! Let's get started!")
    else:
        print('Sorry, that is not an option.')

elif character == 'N':
    print('You chose Nym.')
    print('Now for some background knowledge:')
    print('''Nym's parents are very wealthy and respected, as advisors to the king, and he is just moving on from the childhood stage to the apprentice stage.
His parents have already got him a master, who works on the rank right underneath the king, but seems to dissaprove of him.
Rather stuck-up and used to getting everything he wants, he is struggling to keep up with his master's demands, and this is just the beginning.
But his parents have enourmous faith with him, so Nym also believes that he will succeed soon.
He doesn't work hard however, and constantly scowls when his master reprinds him.
''')
    print("Now let's get started, are you ready to continue you? (y/n)")
    ready = input()
    if ready == 'y':
        print("Alright then! Let's get started!")
    elif ready == 'n':
        print('Waiting... waiting... press y to start.')
        readyagain = input()
        if readyagain == 'y':
            print("Alright then! Let's get started!")
    else:
        print('Sorry, that is not an option.')
