import pygame
pygame.init()
screen = pygame.display.set_mode([600, 400])
screen.fill([255,255,255])
pygame.draw.rect(screen, [0,0,0], [240, 140, 120, 20])
pygame.draw.rect(screen, [0,0,0], [210, 220, 200, 20])
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()