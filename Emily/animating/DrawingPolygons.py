import pygame
pygame.init()
poly1 = [[300, 50], [150, 170], [200, 350], [400, 350], [450, 170]]
screen = pygame.display.set_mode([600,400])
screen.fill([229,174,134])
pygame.draw.polygon(screen, [255,0,0], poly1, 5)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit