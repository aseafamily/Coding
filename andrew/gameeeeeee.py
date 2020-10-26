import pygame, sys

def ifAdd(index, image, player, pos):
    if playlist[index] == 0:
        screen.blit(image, pos)
        playlist[index] = player
        return 1
    else:
        return 0

pygame.init()
screen = pygame.display.set_mode([640, 480])
background = pygame.Surface(screen.get_size())
background.fill([255, 255, 255])
clock = pygame.time.Clock()
'''class Ball(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        if self.rect.left <= screen.get_rect().left or  \
                self.rect.right >= screen.get_rect().right:
            self.speed[0] = -self.speed[0]
        newpos = self.rect.move(self.speed)
        self.rect = newpos'''
dots = [[30, 200], [570, 200]]
dots1 = [[30, 400], [570, 400]]
dots2 = [[200, 30], [200, 570]]
dots3 = [[400, 30], [400, 570]]
playlist = [0, 0, 0, 0, 0, 0, 0, 0, 0]
playercross = 1
playerball = 2
screen = pygame.display.set_mode([600, 600])
screen.fill([255, 255, 255])
pygame.draw.lines(screen, [5, 255, 255], True, dots, 2)
pygame.draw.lines(screen, [5, 255, 255], True, dots1, 2)
pygame.draw.lines(screen, [5, 255, 255], True, dots2, 2)
pygame.draw.lines(screen, [5, 255, 255], True, dots3, 2)
pygame.display.flip()
my_ball = pygame.image.load('beach_ball.png')
my_cross = pygame.image.load('cross.png')
font = pygame.font.Font(None, 50)
text1 = font.render("0", 1, (0, 0, 0)) 
screen.blit(text1, [180, 30])
text2 = font.render("1", 1, (0, 0, 0)) 
screen.blit(text2, [380, 30])
text3 = font.render("2", 1, (0, 0, 0)) 
screen.blit(text3, [550, 30])
text4 = font.render("3", 1, (0, 0, 0)) 
screen.blit(text4, [180, 210])
text5 = font.render("4", 1, (0, 0, 0)) 
screen.blit(text5, [380, 210])
text6 = font.render("5", 1, (0, 0, 0)) 
screen.blit(text6, [550, 210])
text7 = font.render("6", 1, (0, 0, 0)) 
screen.blit(text7, [180, 400])
text8 = font.render("7", 1, (0, 0, 0)) 
screen.blit(text8, [380, 400])
text9 = font.render("8", 1, (0, 0, 0)) 
screen.blit(text9, [550, 400])
# x = 50
# y = 50
# x1 = 50
# y1 = 250
# x2 = 50
# y2 = 450
thing = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            things = thing % 2
            my_image = my_ball
            my_player= playerball
            added = 0
            if things != 0:
                my_image = my_cross
                my_player = playercross
            if event.key == pygame.K_0:
                added = ifAdd(0, my_image, my_player, [50, 50])
            elif event.key == pygame.K_1:
                added = ifAdd(1, my_image, my_player, [250, 50])
            elif event.key == pygame.K_2:
                added = ifAdd(2, my_image, my_player, [450, 50])
            elif event.key == pygame.K_3:
                added = ifAdd(3, my_image, my_player, [50, 250])
            elif event.key == pygame.K_4:
                added = ifAdd(4, my_image, my_player, [250, 250])
            elif event.key == pygame.K_5:
                added = ifAdd(5, my_image, my_player, [450, 250])
            elif event.key == pygame.K_6:
                added = ifAdd(6, my_image, my_player, [50, 450])
            elif event.key == pygame.K_7:
                added = ifAdd(7, my_image, my_player, [250, 450])
            elif event.key == pygame.K_8:
                added = ifAdd(8, my_image, my_player, [450, 450])
            if added == 1:
                thing += 1
                print(playlist)
            #screen.blit(my_ball, [x, y])
    #clock.tick(30)
    #screen.blit(background, (0, 0))
    #my_ball.move()
    #screen.blit(my_ball.image, my_ball.rect)
    pygame.display.flip()
pygame.quit()