#oddoreven = int(input("Please put in a number and I tell you if it is even our odd."))
#R = oddoreven % 2
#if R == 0:
#    print("The number you entered was even.")
#else:
#    print("The number that you put in was odd.")
number = int(input("What is the number that you want to add together from the start"))
number1 = int(input("What is the number that you want to end with?"))
answer = 0
for i in range (number1, number + 1) :
    thing = i + number + number1
    if i + 2 == 0:
        print(thing)
    print(i)
    answer = answer + i

