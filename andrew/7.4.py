gender = input("Are you male of femle, please type in f for femle and m for male?")
age = int(input("What is your age?"))
if gender == 'f' and 10 <= age <= 12:
    print("You can go to the socer team.")
else:
    print("You can not go to the team.")
