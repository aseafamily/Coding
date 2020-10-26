import pygame
pygame.init()
linenumber1 = [[0, 200], [600, 200]]
linenumber2 = [[0, 400], [600, 400]]
linenumber3 = [[200, 0], [200, 600]]
linenumber4 = [[400, 0], [400, 600]]
screen = pygame.display.set_mode([600,600])
screen.fill([255, 255, 255])
pygame.draw.lines(screen, [0,0,0], True, linenumber1, 1)
pygame.draw.lines(screen, [0,0,0], True, linenumber2, 1)
pygame.draw.lines(screen, [0,0,0], True, linenumber3, 1)
pygame.draw.lines(screen, [0,0,0], True, linenumber4, 1)

pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit