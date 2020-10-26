import pygame, sys
pygame.init()
linenumber1 = [[200, 0], [200,600]]
linenumber2 = [[400,0], [400, 600]]
linenumber3 = [[0, 200], [600, 200]]
linenumber4 = [[0, 400], [600, 400]]

screen = pygame.display.set_mode([600,600])
screen.fill([255,255,255])

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
            if evenorodd % 2 != 0:
                my_image = my_cross 
                if event.key == pygame.K_1:
                    screen.blit(my_image, [ball55, ball55])
                elif event.key == pygame.K_2:
                    screen.blit(my_image, [ball255,ball55])
                elif event.key == pygame.K_3:
                    screen.blit(my_image, [ball455, ball55])
                elif event.key == pygame.K_4:
                    screen.blit(my_image, [ball55, ball255])
                elif event.key == pygame.K_5:
                    screen.blit(my_image, [ball255, ball255])
                elif event.key == pygame.K_6:
                    screen.blit(my_image, [ball455, ball255])
                elif event.key == pygame.K_7:
                    screen.blit(my_image, [ball55, ball455])
                elif event.key == pygame.K_8:
                    screen.blit(my_image, [ball255, ball455])
                elif event.key == pygame.K_9:
                    screen.blit(my_image, [ball455, ball455])
                evenorodd = evenorodd + 1                   
    pygame.display.flip()
pygame.quit()