import pygame
pygame.init()
screen = pygame.display.set_mode([600, 400])
screen.fill([255,255,255])
pygame.draw.rect(screen, [0,0,0], [240, 190, 120, 20])
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()