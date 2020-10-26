Invalid = input("You are Invalid. Tpye some thing to make your self not Invalid.")
thing = True
while thing:
    if Invalid == 'um':
        Invalid1 = input("You are even more Invalid. Tpye some thing useful to make your self Invalid again before you lose.")
        if Invalid1 == 'um':
            print("You are Invalid even more the computers does not like you!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            thing = False
        elif Invalid1 == "Yes I am Invalid":
            Invalid2 = input("Very well you are now not Invalid now tpye some thing in to make yourself not Invalid.")
        else:
            print("The compter does not like you!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            thing = False
    elif Invalid == "Yes I am Invalid":
        print("The compter likes you!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        thing = False
    else:
        Invalid1 = input("You are even more Invalid. Tpye some thing useful to make your self Invalid again before you lose.")
        if Invalid1 == 'um':
            print("You are Invalid even more the computers does not like you!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            thing = False
        elif Invalid1 == "Yes I am Invalid":
            Invalid2 = input("Very well you are now not Invalid now tpye some thing in to make yourself not Invalid.")
        else:
            print("The compter does not like you!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            thing = False