import pygame
import time
noidea = int(input('Countdown timer: How many minutes?'))
for i in range(noidea, 0, -1):
    print(i,' ',  end='')
    for g in range(i): 
        print('*', end='')
    print()
    time.sleep(60)
print('YOUR TIMER IS UP!')

'''for i in range(5):
    for j in range(3):
        print('AB', end='')
    print()

dogs = 140
buns = 120
mus = 20
ket = 80
onions = 40

print('\tDog \tBun \tKetchup\tMustard\tOnions \tCalories')
count = 1
for dog in[0, 1]:
    for bun in [0, 1]:
        for ketchup in [0, 1]:
            for mustard in [0, 1]:
                for onion in [0, 1]:
                    print('#', count, '\t', end='')
                    print(dog, '\t', bun, '\t', ketchup,
                          '\t', end='')
                    print(mustard, '\t', onion, end='')
                    count = count + 1
                    tot_cal = ((dog * dogs) + (bun * buns) + 
                            (mustard * mus) + (ket * ketchup) + 
                            (onion * onions))
                    print('\t', tot_cal)
                    

numBlocks = int(input('How many blocks of stars do you want? '))
for block in range(1, numBlocks + 1):
    print('Block =', block)
    for line in range(1, block * 2):
        for star in range(1, (block + line) * 2):
            print('* ', end='')
        print('  line =', line, 'star =', star)
    print()

numBlocks = int(input('How many blocks of stars do you want? '))
for block in range(1, numBlocks + 1):
    for line in range(1, block * 2):
        for star in range(1, (block + line) * 2):
            print('* ', end='')
        print()
    print()
        

numBlocks = int(input('How many blocs ot stars do you want? '))
numLines = int(input('How many lines in each block? '))
numStars = int(input('How many stars per line?'))
for block in range(0, numBlocks):
    for line in range(0, numLines):
        for star in range(0, numStars):
            print('* ', end='')
        print()
    print()

numLines = int(input('How many lines of stars do you want? '))
numStars = int(input('How many stars per line? '))
for line in range(0, numLines):
    for star in range(0, numStars):
        print('* ', end='')
    print()

numStars = int(input('How many stars do you want?'))
for i in range(1, numStars+1):
    print('* ', end='')

for g in range(1, 10):
    for i in range(1, 13):
        print(i, 'x', g, '=', i * g)
    print()'''
