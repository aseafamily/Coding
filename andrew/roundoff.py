number = -0.8
decmail = number - int(number) 
if decmail >= .5:
    number += 1
    print(int(number))
elif decmail >= 0:
    print(int(number))    
elif 0 >= decmail >= -0.5:
    print(int(number))
else:
    print(int(number)- 1)
