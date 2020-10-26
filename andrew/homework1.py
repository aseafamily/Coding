import pygame, sys
pygame.init()
screen = pygame.display.set_mode([400, 400])
screen.fill([255, 0, 255])
list1 = [[0, 0], [400, 400]]
list2 = [[400, 0], [0, 400]]
list3 = [[0, 200], [400, 200]]
list4 = [[200, 0], [200, 600]]
pygame.draw.lines(screen, [5, 255, 255], True, list1, 3)
pygame.draw.lines(screen, [5, 255, 255], True, list2, 3)
pygame.draw.lines(screen, [5, 255, 255], True, list3, 3)
pygame.draw.lines(screen, [5, 255, 255], True, list4, 3)
pygame.display.flip()
running = True
while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
pygame.quit()
