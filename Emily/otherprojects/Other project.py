#Welcome and Name
print('Hello! Welcome to the Adventure Story. To get started, please enter your name.')
name = input()

#Hello whatever your name is!
print('Hello ' + str(name) + "!")

#Character Options
print('Now, please choose a character, the options are...')
print('''Oracle - A famous future-teller who works for the King and worries about her public image.
Tyhnim - Oracle's son, a new apprentice who's talent isn't quite at it's peak yet.
Ellena - An orphan, who seems to have a successful life ahead.
Nym - Who despite his privelleged past is struggling with the new demands of reality.''')

#Which Character?
print('Who do you want to choose? (O/T/E/N)')
character = input()

#If you chose Oracle + some  background knowledge
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

    #Ready to continue
    print("Now let's get started.")
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
    choicefororacle1 = input()
#If user chooses Tyhnim + Background knowledge
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
    print("Now let's get started.")
    print('''Tyhnim crept through the early morning, hurrying to the mailbox, hoping for a job acceptance.
He reached his hand into the box, hoping for the slight brush and crinkle of a letter.
As his fingertips reached the end of the box, he sighed with dissapointment, and turned around to head home, when a crinkle of paper underneath him startled him.
Stooping down, he realizes it's a letter. It must have fluttered out when he opened it.
Tyhnim opens it with trembling hands, and to his delight, it's an acceptance letter.
As he reads on, he slowly realizes how low the job is. He would be working just above what his mother did when she just graduated from apprentice stage.
He has two options:
1. Accept his new job, even though the low rank might draw criticism.
2. Ignore it and wait hopefully for a higher job.
(1/2)
''')
    choicefortyhnim1 = input()
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
    print("Now let's get started.")
    print('''Ellena smiled as the bright morning sun slanted through the window of her new home.
After moving up to a higher rank position, she had been granted a new home, and she already loved every inch of it.
Her work only started at noon, she she had plenty of time to-
A soft, quiet ringing interrupted her cheery thoughts, and she crept out of her blankets, and glanced warily at the window adjacent to her front step.
To her alarm and suprise, there were orderers on her front step, stern expressions on their faces.
She opened the door a crack, "Hello?"
The larger one of the two spoke, "Hello miss, we'd like to question you about your parents some more."
Ellena forced a patient smile, "Of course, please come in."
As she led the orderers to her sitting room, she dashed off to make some tea, before hurrying back.
This time the smaller orderer spoke, clearing his throat first, "Have you seen your parents lately?"
Ellena took a sip of tea, then froze. The truth was, she had, in a way.
But that was only in a vision... then again they all took visions seriously... but it might....
Almost paralyzed with fright, she stuttered out a letter, before stopping
By now, her thoughts had cleared into two choices.
1. Say yes.
2. Say no.
(1/2)
''')
    choiceforellena1 = input()
elif character == 'N':
    print('You chose Nym.')
    print('Now for some background knowledge:')
    print('''Nym's parents are very wealthy and respected, as advisors to the king, and he is just moving on from the childhood stage to the apprentice stage.
His parents have already got him a master, who works on the rank right underneath the king, but seems to dissaprove of him.
Rather stuck-up and used to getting everything he wants, he is struggling to keep up with his master's demands, and this is just the beginning.
But his parents have enourmous faith with him, so Nym also believes that he will succeed soon.
He doesn't work hard however, and constantly scowls when his master reprinds him.
''')
    print("Now let's get started.")
    print('''Nym scowled as a rough voice startled him from his luxurious thoughts.
"Nym," Master Hurria growled, "It's time to get up." Nym bit back a sharp reply and got out of bed.
When he hadn't been apprenticed, he had slept till almost noon, dozing on and off with thoughts of a rich life ahead.
Master Hurria left the room, to his great relief and he slowly walked into the hallway, still sleepy.
As he was about to step down the stairs of Master Hurria's grand house, he heard the door open.
"Tiffina wants to see you," a gruff voice, that sounded like the messenger that commonly visited the house said.
Master Hurria's footsteps shuffled past the staircase, and Nym ducked behind a wall.
"She does now does she? Ignores me for nine moonrises, and then finally she..."
His voice trailed off and a moment later, the door slammed.
As Nym stared with slight confusion at the spot where Master Hurria had been, an idea dawned on him.
Though he knew that he was supposed to light the fire and cook himself breakfast, perhaps he could...
His frazzled mind eventually cleared and he decided that he had three options while Master Hurria was away.
1. Do his morning chores.
2. Go back to sleep.
3. Go into Master Hurria's treasury, and take what he found.
''')
