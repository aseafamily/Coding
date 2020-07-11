ForC = input("Please put in C which is = to Celsius to Fahrenhiet. F = Fahrenhiet to Celsuis.")
number = input("Please enter a number.")
if ForC == "F":
    C=(float(number)- 32)/1.8
    print(C)
elif ForC == "C":
    F=(float(number)*1.8+32
    print(F)
else:
    print("How dare you.")
