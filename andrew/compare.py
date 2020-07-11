num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 < num2:
    print(num1, "is less than ", num2)
elif num1 > num2:
    print(num1, "is greater thatn ", num2)
elif num1 == num2:
    print(num1, "is equal to ", num2)
else:
    print(num1, "is not equal to ", num2)
