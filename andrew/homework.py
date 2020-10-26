#import random, time
#for i in range(0, 10):
#    j = random.random()
#    print(j)
#    time.sleep(1)
#import random
#for i in range(0, 5):
#    k = random.randint(1, 20)
#    print(k)
#fst = input("Please put in a rock, paper, and scissors, r for rock, p for paper, s for scissors.")
#snd = input("Please put in a rock, paper, and scissors, r for rock, p for paper, s for scissors.")
#if fst == 'r' and snd == 'r':
##    print("This is a tie because you both did rock.")
#elif fst == 'r' and snd == 'p':
#    print("The second user won because the 1st one did rock and the second one did paper.")
#elif fst == 'r' and snd == 's':
#    print("The first user won because the first person did rock and the second person did scissors.")
#elif fst == 'p' and snd == 'p':
#    print("Tie is tie because you both did paper.")
#elif fst == 'p' and snd == 's':
#    print("The second player won because the second player did scissors and the first player did paper.")
#elif fst == 'p' and snd == 'r':
#    print("The first player won because the first player did paper and the second player did rock.")
#elif fst == 's' and snd == 's':
#    print("This is a tie because you both did scissors.")
#elif fst == 's' and snd == 'p':
#    print("The first player won because the first player did scissors and th second player did paper.")
#elif fst =='s' and snd == 'r':
#    print("The second player won because the first player did scissors and the second player did rock.")
#else:
#    print("I could not uderstand one of you.")
#quarters = int(input("How many quarters do you have?"))
#dimes = int(input("How many dimes do you have?"))
#nickes = int(input("How many nickes do you have"))
#pennies = int(input("How many pennies do you have"))
#total_cents = quarters * 25 + dimes * 10 + nickes * 5 + pennies
#print("This is how much chance you have " + str(total_cents) "cents.")
#width = float(input("Please put in the width of the roon that you are in, in feet."))
#length = float(input("Please put in a number that is the room that you are in, in feet."))
#area_in_feet = width * length
#area_in_yards = area_in_feet / 9
#sqaure_per_yard_cost = float(input("Please put in how much the carpet costs per square yard."))
#cost_of_square_yards = sqaure_per_yard_cost * area_in_yards 
#print("This is how much the carpet you will need in feet of the room that you are in." + str(area_in_feet))
#print("This is how much the carpet you wil need in yards of the room that you are in." + str(area_in_yards))
#print("This is how much the carpet will cost." + str(cost_of_square_yards))