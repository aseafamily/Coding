import pygame, sys
pygame.init()

'''
dots = [[221, 432], [225, 331], [133, 342], [141, 310], 
    [51, 230], [74, 217], [58, 153], [114, 164],
    [123, 135], [176, 190], [159, 77], [193, 93],
    [230, 28], [267, 93], [301, 77], [284, 190],
    [327, 135], [336, 164], [402, 153], [386, 217],
    [409, 230], [319, 310], [327, 342], [233, 331],
    [237, 432]]
    '''
dots = [[30, 200], [570, 200]]
dots1 = [[30, 400], [570, 400]]
dots2 = [[200, 30], [200, 570]]
dots3 = [[400, 30], [400, 570]]
screen = pygame.display.set_mode([600, 600])
screen.fill([5, 255, 255])
pygame.draw.lines(screen, [255, 0, 0], True, dots, 2)
pygame.draw.lines(screen, [255, 0, 0], True, dots1, 2)
pygame.draw.lines(screen, [255, 0, 0], True, dots2, 2)
pygame.draw.lines(screen, [255, 0, 0], True, dots3, 2)
pygame.display.flip()
running = True
while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
pygame.quit()