import pygame, sys
pygame.init()
screen = pygame.display.set_mode([600, 400])
screen.fill([5, 255, 255])
my_rect = pygame.Rect(150, 100, 300, 150)
pygame.draw.rect(screen, [250, 0, 0], my_rect, 0)
my_rect1 = pygame.Rect(170, 120, 60, 110)
pygame.draw.rect(screen, [5, 255, 255], my_rect1, 0)
my_rect2 = pygame.Rect(270, 120, 60, 110)
pygame.draw.rect(screen, [5, 255, 255], my_rect2, 0)
my_rect3 = pygame.Rect(370, 120, 60, 110)
pygame.draw.rect(screen, [5, 255, 255], my_rect3, 0)
pygame.display.flip()
running = True
while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
pygame.quit()