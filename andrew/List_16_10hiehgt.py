import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([5, 255, 255])
my_ball = pygame.image.load("beach_ball.png")
x = 50
y = 50
y_speed = 10
screen.blit(my_ball, [x, y])
pygame.display.flip()
pygame.time.delay(20)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
    pygame.time.delay(20)
    pygame.draw.rect(screen, [5, 255, 255], [x, y, 90, 90], 0)
    y = y + y_speed
    if y > screen.get_height() - 90 or y < 0:
        y_speed = - y_speed
    screen.blit(my_ball, [x, y])
    pygame.display.flip()
pygame.quit()