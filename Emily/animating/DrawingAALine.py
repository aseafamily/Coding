import pygame
pygame.init()
screen = pygame.display.set_mode([600,400])
screen.fill([229,174,134])
my_rect = pygame.Rect(10, 10, 200, 300)
pygame.draw.aaline(screen, [0,0,0], [267, 50], [438, 42], 1)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit