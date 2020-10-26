# import pygame
# pygame.init()
# screen = pygame.display.set_mode([600, 600])
# screen.fill([255,255,255])
# pygame.draw.circle(screen, (0, 255, 0),[300,200], 125, 0)
# pygame.draw.circle(screen, (0,0,255),[200,400],125,0)
# pygame.draw.circle(screen, (255,0,0),[400,400],125,0)
# pygame.display.flip()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
# pygame.quit()

import pygame
pygame.init()
screen = pygame.display.set_mode([600, 400])
screen.fill([255,255,255])
pygame.draw.circle(screen, [188,0,45],[300, 200], 105, 0)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()

# import pygame
# pygame.init()
# screen = pygame.display.set_mode([600, 400])
# screen.fill([0,103,71])
# pygame.draw.circle(screen, [218,41,28],[250, 200], 110, 0)
# pygame.display.flip()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
# pygame.quit()