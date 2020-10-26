import pygame
pygame.init()
linenumber1 = [[0, 0], [600, 0]]
linenumber2 = [[0, 0], [300, 600]]
linenumber3 = [[600,0], [300, 600]]
acrossline1 = [[200, 0], [200, 200]]
acrrosline2 = [[300, 0], [400, 400]]
screen = pygame.display.set_mode([600,600])
screen.fill([229,174,134])
pygame.draw.lines(screen, [255,0,0], True, linenumber1, 3)
pygame.draw.lines(screen, [255,0,0], True, linenumber2, 3)
pygame.draw.lines(screen, [255,0,0], True, linenumber3, 3)
pygame.draw.lines(screen, [200, 10, 10], True, acrossline1, 1)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit