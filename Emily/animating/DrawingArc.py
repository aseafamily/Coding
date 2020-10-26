import pygame
pygame.init()
screen = pygame.display.set_mode([600,400])
screen.fill([229,174,134])
my_rect = pygame.Rect(10, 10, 200, 300)
pygame.draw.arc(screen, [0,0,0], my_rect, 10, 20)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit