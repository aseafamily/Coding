'''import pygame, sys
pygame.init()
screen = pygame.display.set_mode([600, 400])
screen.fill([255, 255, 255])
pygame.draw.circle(screen, [255, 0, 0], [300, 120], 100, 100)
pygame.draw.circle(screen, [0, 255, 0], [230, 270], 100, 100)
pygame.draw.circle(screen, [0, 0, 255], [400, 270], 100, 100)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False'''
#pygame.quit()
import pygame, sys
pygame.init()
screen = pygame.display.set_mode([600, 400])
screen.fill([255, 255, 255])
pygame.draw.circle(screen, [239, 51, 64], [300, 200], 100, 100)
pygame.display.flip()
running = True
while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
pygame.quit()
'''import pygame
pygame.init()
screen = pygame.display.set_mode([640, 480])
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
import pygame
pygame.init()
screen = pygame.display.set_mode([640, 480])'''