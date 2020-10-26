import pygame, sys
pygame.init()
screen = pygame.display.set_mode([600, 400])
screen.fill([5, 255, 255])
#Aaline
#pygame.draw.aaline(screen, [2, 3, 4], [30, 90], [90, 5])
#Arc
#my_rect = pygame.Rect(12, 150, 300, 200)
#pygame.draw.arc(screen, [255, 5, 255], my_rect, 300, 500)
#Ellipse
#my_rect = pygame.Rect(250, 150, 300, 200)
#pygame.draw.ellipse(screen, [255, 255, 5], my_rect)
#Polygon
#my_list = [[300, 50], [450, 100], [450, 300], [300, 350], [100, 200], [50, 50]]
#pygame.draw.polygon(screen, (123, 234, 23), my_list)
pygame.display.flip()
running = True
while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
pygame.quit()