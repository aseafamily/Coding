import pygame, sys
pygame.init()
linenumber1 = [[200, 0], [200,600]]
linenumber2 = [[400,0], [400, 600]]
linenumber3 = [[0, 200], [600, 200]]
linenumber4 = [[0, 400], [600, 400]]

screen = pygame.display.set_mode([600,600])
screen.fill([229,174,134])

pygame.draw.lines(screen, [255,0,0], True, linenumber1, 5)
pygame.draw.lines(screen, [255,0,0], True, linenumber2, 5)
pygame.draw.lines(screen, [255,0,0], True, linenumber3, 5)
pygame.draw.lines(screen, [255,0,0], True, linenumber4, 5)

ballx1 = 55
bally1 = 55
ballx2 = 255
bally2 = 55
ballx3 = 455
bally3 = 55
my_ball = pygame.image.load('C:/GitHub/Coding/Emily/homework/BallBouncingGames/beach_ball.png')
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                screen.blit(my_ball, [ballx1, bally1])
                bally1 = bally1 + 200
            elif event.key == pygame.K_UP:
                screen.blit(my_ball, [ballx2, bally2])
                bally2 = bally2 + 200
            elif event.key == pygame.K_RIGHT:
                screen.blit(my_ball, [ballx3, bally3])
                bally3 = bally3 + 200
        
    pygame.display.flip()
pygame.quit()