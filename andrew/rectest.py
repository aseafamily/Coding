import pygame, sys
pygame.init()
screen = pygame.display.set_mode([600, 400])
screen.fill([5, 255, 255])
my_rect = pygame.Rect(250, 150, 300, 200)
pygame.draw.rect(screen, [250, 0, 0], my_rect, 2)
#my_list = [250, 150, 300, 200]
#pygame.draw.rect(screen, [250, 0, 0], my_list, 0)
# pygame.draw.circle(screen, [239, 51, 64], [300, 200], 100, 100)
pygame.display.flip()
running = True
while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
pygame.quit()