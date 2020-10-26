import pygame, sys, random
pygame.init()
screen = pygame.display.set_mode([800, 720])
screen.fill([5, 255, 255])
my_ball = pygame.image.load("beach_ball.png")
x = 0
y = 0
y_speed = 10
screen.blit(my_ball, [x, y])
font = pygame.font.Font(None, 50)
text1 = font.render("You get 100 tickets!", 1, (0, 0, 0)) 
screen.blit(text1, [130, 60])
text2 = font.render("You will have a happy life!", 1, (0, 0, 0)) 
screen.blit(text2, [130, 150])
text3 = font.render("You will become the CEO of something!", 1, (0, 0, 0)) 
screen.blit(text3, [130, 240])
text4 = font.render("You will make your own comany!", 1, (0, 0, 0))
screen.blit(text4, [130, 330])
text5 = font.render("You will be rich!", 1, (0, 0, 0)) 
screen.blit(text5, [130, 420])
text6 = font.render("You will be famous!", 1, (0, 0, 0)) 
screen.blit(text6, [130, 510])
text7 = font.render("You will live to be 110 years old!", 1, (0, 0, 0)) 
screen.blit(text7, [130, 600])
text8 = font.render("You get 100 tickets!", 1, (0, 0, 0)) 
screen.blit(text8, [130, 690])
for i in range(7):
    height = (i + 1) * 90
    list1 = [[140, height], [800, height]]
    pygame.draw.lines(screen, [255, 0, 0], True, list1, 1)
pygame.display.flip()
pygame.time.delay(20)
running = True
runner = 0
something = random.randint(1, 250)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
    
    runner += 1
    if runner <= something:
        pygame.time.delay(20)
        pygame.draw.rect(screen, [5, 255, 255], [x, y, 90, 90], 0)
        y = y + y_speed
        if y > screen.get_height() - 90 or y < 0:
            y_speed = - y_speed
        screen.blit(my_ball, [x, y])
        pygame.display.flip()
pygame.quit()