number = -0.75
decimal = number - int(number)

if decimal >= .5:
    print(int(number) + 1)
elif 0<= decimal <.5:
    print(int(number))
elif 0> decimal > -0.5:
    print(int(number))
else:
    print(int(number) - 1)
