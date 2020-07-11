# Listing_10-1_skier.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

# canged by andrew

import pygame, sys, random

skier_images = ["skier_down.png", "skier_right1.png",
                "skier_right2.png", "skier_left2.png",
                "skier_left1.png"]

# Creates skier
class SkierClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("skier_down.png")
        self.rect = self.image.get_rect()
        self.rect.center = [320, 100]
        self.angle = 0

    # Turns skier
    def turn(self, direction):
        self.angle = self.angle + direction
        if self.angle < -2:  self.angle = -2
        if self.angle >  2:  self.angle =  2
        center = self.rect.center
        self.image = pygame.image.load(skier_images[self.angle])
        self.rect = self.image.get_rect()
        self.rect.center = center
        speed = [self.angle, 6 - abs(self.angle) * 2]
        return speed

    # Moves skier left and right
    def move(self, speed):
        self.rect.centerx = self.rect.centerx + speed[0]
        if self.rect.centerx < 20:  self.rect.centerx = 20
        if self.rect.centerx > (screen_width - 20): self.rect.centerx = (screen_width - 20)

# Creates trees and flags
class ObstacleClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, obs_type):
        pygame.sprite.Sprite.__init__(self)
        self.image_file = image_file
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.obs_type = obs_type
        self.passed = False

    # Makes scenery scroll up
    def update(self):
        global speed
        self.rect.centery -= speed[1]
        # Deletes obstacles that have scrolled off the top of the screen
        if self.rect.centery < -32:
            self.kill()

# Creates one screen full of random trees and flags
def create_map():
    global obstacles
    locations = []
    for i in range(10):
        row = random.randint(0, 15)
        col = random.randint(0, 15)
        location  = [col * 64 + 20, row * 64 + 20 + screen_width]
        if not (location in locations):
            locations.append(location)
            obs_type = random.choice(["tree", "flag"])
            if obs_type == "tree": img = "skier_tree.png"
            elif obs_type == "flag":  img = "skier_flag.png"
            obstacle = ObstacleClass(img, location, obs_type)
            obstacles.add(obstacle)

# Redraws screen
def animate():
    screen.fill([50, 206, 235])
    obstacles.draw(screen)
    screen.blit(skier.image, skier.rect)
    screen.blit(score_text, [10, 10])
    pygame.display.flip()

# ask name
name = input("Please put in your name.")

# Gets everything ready
screen_width = 1000
screen_height = 1000

pygame.init()
screen = pygame.display.set_mode([screen_width,screen_height])
clock = pygame.time.Clock()
skier = SkierClass()
speed = [0, 9]
obstacles = pygame.sprite.Group()
map_position = 0
points = 0
create_map()
font = pygame.font.Font(None, 50)

# Starts main loop
ticker = 30
running = True
while running:
    clock.tick(ticker)  # Updates graphics ticker times per second
    # Checks for keypresses or window close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = skier.turn(-1)
            elif event.key == pygame.K_RIGHT:
                speed = skier.turn(1)
    skier.move(speed)  # Moves skier

    map_position += speed[1]  # Scrolls scenery

    # Creates a new screen full of scenery
    if map_position >= screen_width:
        create_map()
        map_position = 0

    # Checks for hitting trees and getting flag
    hit = pygame.sprite.spritecollide(skier, obstacles, False)
    if hit:
        if hit[0].obs_type == "tree" and not hit[0].passed:
            points = points - 100
            skier.image = pygame.image.load("skier_crash.png")
            animate()
            pygame.time.delay(1000)
            skier.image = pygame.image.load("skier_down.png")
            ticker -= 5
            screen_width += 10
            screen_height += 10
#            running = False
#            print(name + "Score: " + str(points), 1, (0, 0, 0))
#            skier.angle = 0
#            speed = [0, 6]
            hit[0].passed = True
        elif hit[0].obs_type == "flag" and not hit[0].passed:
            points += 5
            ticker += 5
            hit[0].kill()
            screen_width -= 10
            screen_height -= 10
    obstacles.update()
    all_text = name + " Score: " + str(points) + " Speed: " + str(ticker)
    score_text = font.render(all_text, 1, (0, 0, 0))  # Displays score
    animate()
    if points >= 200:
        print("You win!!!!!")
        running = False
    elif ticker >= 150:
        print('You won!')
        running = False
    elif points <= -1000:
        print("You lost!!!!!!!!!!!")
        running = False
    elif points == 30:
         screen_width -= 10
         screen_height -= 10
#        else:
#        print("You win!!!")
pygame.quit()
