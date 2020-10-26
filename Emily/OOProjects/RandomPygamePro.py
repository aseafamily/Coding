from time import sleep
import pygame
pygame.init()
print('Welcome to Stopwatch & Timer!')
which = input('''Would you like to set a stopwatch or a timer?(s/t)
''')
if which == 't':
    long = input('Alright, would you like to set a timer in seconds, minutes, or hours?(seconds/minutes/hours)')
    thetime = int(input('Okay, how long would you like the timer to be? Put it in  your earlier preferred units.'))
    print('Okay then! One more thing, a white screen with a red circle will pop up when your timer is up.')
    if long == 'seconds':
        thetime = thetime
    elif long == 'minutes':
        thetime = thetime*60
    elif long == 'hours':
        thetime = thetime*60*60
    else:
        print("Sorry, that isn't an option.")
    for i in range(thetime, 0, -1):
        print(i)
        sleep(1)
    screen = pygame.display.set_mode([600, 600])
    screen.fill([255,255,255])
    pygame.draw.circle(screen, (255,0,0),[300,300],150,0)
    pygame.display.flip()
    running = True
    while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.quit()
elif which == 's':
    stopwatchfy = input('Alright, Stopwatch starting! Type stop when you want to stop the stopwatch.')
    
else:
    print('Sorry, that is not an option!')