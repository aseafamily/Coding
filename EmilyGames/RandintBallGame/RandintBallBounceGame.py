import pygame, sys
from random import *
pygame.init()
screen = pygame.display.set_mode([800,720])
screen.fill([229,174,134])
font = pygame.font.Font(None, 50)
rext1 = font.render('You will win the lottery.', 1, (0,0,0))
screen.blit(rext1, [140, 60])
rext2 = font.render('You will never get the COVID-19.', 1, (0,0,0))
screen.blit(rext2, [140, 145])
rext3 = font.render('Your IQ will jump up by 50 tommorow.', 1, (0,0,0))
screen.blit(rext3, [140, 225])
rext4 = font.render('Someone will hand you 5 million dollars.', 1, (0,0,0))
screen.blit(rext4, [140, 305])
rext5 = font.render('Your next salary will be $230,00.', 1, (0,0,0))
screen.blit(rext5, [140, 390])
rext6 = font.render('If you run for president, you will win.', 1, (0,0,0))
screen.blit(rext6, [140, 490])
rext7 = font.render('You will win any competition today.', 1, (0,0,0))
screen.blit(rext7, [140, 585])
rext8 = font.render('You will be completely happy tommrow.', 1, (0,0,0))
screen.blit(rext8, [140, 675])
for i in range(7):
    height = (i+1) * 90
    linenumber1 = [[140, height], [800, height]]
    pygame.draw.lines(screen, [255, 0, 0], True, linenumber1, 1)

my_ball = pygame.image.load('beach_ball.png')
x = 0
y = 0
y_speed = 10

running = True
runner = 0
tery_trandom_tumber = randint(0, 250)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if runner < tery_trandom_tumber:
        pygame.time.delay(20)
        pygame.draw.rect(screen, [229,174,134], [x, y, 90, 90], 0)
        y = y + y_speed
        if y > screen.get_height() - 90 or y < 0:
            y_speed = - y_speed
        screen.blit(my_ball, [x, y])
        pygame.display.flip()
        runner = runner + 1
    
pygame.quit()