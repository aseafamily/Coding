letter = '*'
rows = 20
lines = 20
space = ' '
line2 = 20
#this is half
for i in range(1, lines + 1, 3):
    print(space * (rows-i) + letter * i + letter * i)
for i in range(1,line2 + 1):
    print(space * i + letter * (20-i) + letter * (rows+1-i))

#x="love";print("   x    x\nx xx x\nx   x   x".replace("x",x))
#for i in range(5):print(" "*i+x+" "*(9-i*2),x)
#print(" "*6,x)
