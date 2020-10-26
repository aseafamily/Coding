import pygame
pygame.init()
screen = pygame.display.set_mode([600, 400])
screen.fill([255,255,255])
pygame.draw.rect(screen, [0,0,0], [150, 100, 300, 200])
pygame.draw.rect(screen, [255,255,255], [180, 130, 50, 140])
pygame.draw.rect(screen, [255,255,255], [270, 130, 50, 140])
pygame.draw.rect(screen, [255,255,255], [360, 130, 50, 140])
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()