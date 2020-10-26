import pygame, sys

pygame.init()
linenumber1 = [[200, 0], [200,600]]
linenumber2 = [[400,0], [400, 600]]
linenumber3 = [[0, 200], [600, 200]]
linenumber4 = [[0, 400], [600, 400]]

screen = pygame.display.set_mode([600,600])
screen.fill([255,255,255])

playerlist = [0,0,0,0,0,0,0,0,0]
playercross = 1
playerball = 2

font = pygame.font.Font(None, 50)
rext1 = font.render('0', 1, (48,25,52))
screen.blit(rext1, [170, 5])
rext2 = font.render('1', 1, (0,0,0))
screen.blit(rext2, [370, 5])
rext3 = font.render('2', 1, (0,0,0))
screen.blit(rext3, [570, 5])
rext4 = font.render('3', 1, (0,0,0))
screen.blit(rext4, [170, 205])
rext5 = font.render('4', 1, (0,0,0))
screen.blit(rext5, [370, 205])
rext6 = font.render('5', 1, (0,0,0))
screen.blit(rext6, [570, 205])
rext7 = font.render('6', 1, (0,0,0))
screen.blit(rext7, [170, 405])
rext8 = font.render('7', 1, (0,0,0))
screen.blit(rext8, [370, 405])
rext9 = font.render('8', 1, (0,0,0))
screen.blit(rext9, [570,405])

pygame.draw.lines(screen, [0,0,0], True, linenumber1, 5)
pygame.draw.lines(screen, [0,0,0], True, linenumber2, 5)
pygame.draw.lines(screen, [0,0,0], True, linenumber3, 5)
pygame.draw.lines(screen, [0,0,0], True, linenumber4, 5)
ball55 = 55
ball255 = 255
ball455 = 455
my_ball = pygame.image.load('C:/GitHub/Coding/Emily/homework/BallBouncingGames/beach_ball.png')
my_cross = pygame.image.load('C:\GitHub\Coding\Emily\homework\BallBouncingGames/cross.png')
evenorodd = 1
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            my_image = my_ball
            my_player = playerball
            donothing = 0
            if evenorodd % 2 != 0:
                my_image = my_cross
                my_player = playercross 
            if event.key == pygame.K_0:
                if playerlist[0] == 0:
                    screen.blit(my_image, [ball55, ball55])
                    playerlist[0] = my_player
                else:
                    donothing = 1
            elif event.key == pygame.K_1:
                if playerlist[1] == 0:
                    screen.blit(my_image, [ball255, ball55])
                    playerlist[1] = my_player
                else:
                    donothing = 1                
            elif event.key == pygame.K_2:
                if playerlist[2] == 0:
                    screen.blit(my_image, [ball455, ball55])
                    playerlist[2] = my_player
                else:
                    donothing = 1
            elif event.key == pygame.K_3:
                if playerlist[3] == 0:
                    screen.blit(my_image, [ball55, ball255])
                    playerlist[3] = my_player
                else:
                    donothing = 1
            elif event.key == pygame.K_4:
                if playerlist[4] == 0:
                    screen.blit(my_image, [ball255, ball255])
                    playerlist[4] = my_player
                else:
                    donothing = 1
            elif event.key == pygame.K_5:
                if playerlist[5] == 0:
                    screen.blit(my_image, [ball455, ball255])
                    playerlist[5] = my_player
                else:
                    donothing = 1
            elif event.key == pygame.K_6:
                if playerlist[6] == 0:
                    screen.blit(my_image, [ball55, ball455])
                    playerlist[6] = my_player
                else:
                    donothing = 1
            elif event.key == pygame.K_7:
                if playerlist[7] == 0:
                    screen.blit(my_image, [ball255, ball455])
                    playerlist[7] = my_player
                else:
                    donothing = 1
            elif event.key == pygame.K_8:
                if playerlist[8] == 0:
                    screen.blit(my_image, [ball455, ball455])
                    playerlist[8] = my_player
                else:
                    donothing = 1
            if donothing == 0:
                evenorodd = evenorodd + 1
                print(playerlist)                   
    pygame.display.flip()
pygame.quit()