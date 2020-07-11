import time
number = int(input("Which multiplication table would you like?"))
high = int(input("How high do you want to go?"))
print("Here's your table:")
for i in  range(1, high + 1):
    print(str(i) + ' x ' + str(number) + " = " + str(i * number))
    time.sleep(1)
#for i in range(8):
#    print(i)
#for i in range(2, 9, 2):
#    print(i)
#userinput = input("Please enter a number.")
#number = float(userinput)
#print(type(number))
