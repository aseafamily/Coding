import pygame, sys, random
from pygame.color import THECOLORS
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
for i in range(100):
    radius = random.randint(1, 70)
    width = random.randint(0, 250)
    height = random = random.randint(0, 100)
    color_name = random.choice(list(THECOLORS.keys()))
    color = THECOLORS[color_name]
    pygame.draw.circle(screen, color, [width, height], radius, 0)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()