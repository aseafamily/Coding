import time
letter = '*'
rows = 20
lines = 20
space = ' '
for i in range(1, lines + 1, 2):
    print(space * (20 - i) + letter * i + letter * i)
#    time.sleep(1)
for i in range(1, lines + 1):
    print(space * i + letter * (20 - i) + letter * ((rows + 1) - i))
#    time.sleep(1)
#x="love";print("   x    x\nx xx x\nx   x   x".replace("x",x))
#for i in range(5):print(" "*i+x+" "*(9-i*2),x)
#print(" "*6,x)

