import time
number = int(input("Countdown timer: How many secounds? "))
for i in range(number, 0, -1):
    print(i, end='')
    for f in range(i):
        print('*', end='')
    time.sleep(1)
    print()
print("Blast off!")
import time
number = int(input("Countdown timer: How many secounds? "))
for i in range(number, 0, -1):
    print(i)
    time.sleep(1)
print("Blast off!")
for i in range(5):
    for j in range(3):
        print('AB', end='')
    print()
dog_cal = 140
bun_cal = 120
mus_cal = 20
ket_cal = 80
onion_cal = 40
print("\tDog \tBun \tKetchup\tMustard\tOnions\ttotal cal")
count = 1
for dog in [0, 1]:
    for bun in [0, 1]:
        for ketchup in [0, 1]:
            for mustard in [0, 1]:
                for onion in [0, 1]:
                    tot_cal = ((dog * dog_cal) + (bun * bun_cal) + 
                           (mustard * mus_cal) + (ketchup * ket_cal) + 
                           (onion * onion_cal))
                    print("#", count, "\t", end='')
                    print(dog, "\t", bun, "\t", ketchup, "\t", end='')
                    print(mustard, "\t", onion, "\t", tot_cal)
                    count = count + 1
print("\tDog \tBun \tKetchup \tMustard \tOnions")
count = 1
for dog in [0, 1]:
    for bun in [0, 1]:
        for ketchup in [0, 1]:
            for mustard in [0, 1]:
                for onion in [0, 1]:
                    print("#", count, "\t", end='')
                    print(dog, "\t", bun, "\t", ketchup, "\t", end='')
                    print(mustard, "\t", onion, '\t')
                    count = count + 1
numBlockes = int(input("How many blocks of stars do you want? "))
for block in range(1, numBlockes + 1):
    print('block =', block)
    for line in range(1, block * 2):
        for star in range(1, (block + line) * 2):
            print('* ', end='')
        print(' line =', line, 'star =', star)
    print()
numBlockes = int(input("How many blocks of stars do you want? "))
for block in range(1, numBlockes + 1):
    for line in range(1, block * 2):
        for star in range(1, (block + line) * 2):
            print('* ', end='')
        print()
    print()
numBlockes = int(input("How many blocks of stars do you want? "))
numLines = int(input("How many lines in each block? "))
numStars = int(input("How many stars per line? "))
for block in range(0, numBlockes):
    for line in range(0, numLines):
        for star in range(0, numStars):
            print('* ', end='')
        print()
    print()
numLines = int(input("How many lines of stars do you want? "))
numStars = int(input("How many stars per line? "))
for line in range(0, numLines):
    for star in range(0, numStars):
        print('* ', end='')
    print()
numStars = int(input("How many stars do you want? "))
for i in range(0, numStars):
    print("* ", end=' ')
for i in range(13):
    for k in range(1, 13):
        print(k, "x", i, "=", k * i)
    print()
