import pygame
pygame.init()
linenumber1 = [[0, 0], [400,0]]
linenumber2 = [[0,0], [0, 400]]
linenumber3 = [[400, 0], [400, 400]]
linenumber4 = [[0, 400], [400, 400]]

linenumber5a = [[200, 0], [200, 400]]
linenumber6a = [[0, 200], [400, 200]]
linenumber7a = [[0, 0], [400, 400]]
linenumber8a = [[400, 0], [0, 400]]
screen = pygame.display.set_mode([400,400])
screen.fill([229,174,134])
pygame.draw.lines(screen, [255,0,0], True, linenumber1, 5)
pygame.draw.lines(screen, [255,0,0], True, linenumber2, 5)
pygame.draw.lines(screen, [255,0,0], True, linenumber3, 5)
pygame.draw.lines(screen, [255,0,0], True, linenumber4, 5)

pygame.draw.lines(screen, [200, 10, 10], True, linenumber5a, 2)
pygame.draw.lines(screen, [200, 10, 10], True, linenumber6a, 2)
pygame.draw.lines(screen, [200, 10, 10], True, linenumber7a, 2)
pygame.draw.lines(screen, [200, 10, 10], True, linenumber8a, 2)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit