#Changed by Emily/Daisy :p

import pygame, sys, random

skier_images = ["skier_down.png", "skier_right1.png",
                "skier_right2.png", "skier_left2.png",
                "skier_left1.png"]

# Creates skier
class SkierClass(pygame.sprite.Sprite): #kinda like a stamp
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
        if self.rect.centerx > 620: self.rect.centerx = 620

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
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        location  = [col * 64 + 20, row * 64 + 20 + 640]
        if not (location in locations):
            locations.append(location)
            obs_type = random.choice(["tree", "flag"])
            if obs_type == "tree": img = "skier_tree.png"
            elif obs_type == "flag":  img = "skier_flag.png"
            obstacle = ObstacleClass(img, location, obs_type)
            obstacles.add(obstacle)

# Redraws screen
def animate():
    screen.fill([135, 206, 255])
    obstacles.draw(screen)
    screen.blit(skier.image, skier.rect)
    screen.blit(score_text, [10, 10])
    pygame.display.flip()

#Ask User's Name
print('''Hello, Welcome to the Skier Game.
The goal of this game is to get flags, and avoid trees.
Left and right keys to move, press them twice if you want to turn even more.
Now, please enter your name:''')
name = input()

# Gets everything ready
pygame.init()
screen = pygame.display.set_mode([640, 640])
clock = pygame.time.Clock()
skier = SkierClass()
speed = [0, 6]
obstacles = pygame.sprite.Group()
map_position = 0
points = 0
create_map()
font = pygame.font.Font(None, 50)
clocktick = 20
# Starts main loop
running = True
while running:
    clock.tick(clocktick)  # Updates graphics 30 times per second
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

    map_position += speed[1]# Scrolls scenery

    # Creates a new screen full of scenery
    if map_position >= 640:
        create_map()
        map_position = 0

    # Checks for hitting trees and getting flag
    hit = pygame.sprite.spritecollide(skier, obstacles, False)
    if hit:
        if hit[0].obs_type == "tree" and not hit[0].passed:
            points = points - 50
            skier.image = pygame.image.load("skier_crash.png")
            animate()
            pygame.time.delay(1000)
            skier.image = pygame.image.load("skier_down.png")
            skier.angle = 0
            speed = [0, 6]
            clocktick -= 10
            hit[0].passed = True
            
        elif hit[0].obs_type == "flag" and not hit[0].passed:
            points += 10
            clocktick += 3
            hit[0].kill()

    obstacles.update()
    score_text = font.render(name + "'s Score: " + str(points) +  ' Speed: ' + str(clocktick), 1, (0, 0, 0))  # Displays score
    animate()
    if points >= 200:
        running = False
        print('Congratulations ' + name + '! You won the skier game!')
        print('Your final score was ' + str(points) + '!')
        print('Your final speed was ' + str(clocktick) + '!')
    elif points <= -200:
        running = False
        print('Sorry ' + name + ', but you lost the skier game. Try harder next time!')
        print('Your final score was ' + str(points) + '.')
        print('Your final speed was ' + str(clocktick) + '.')

pygame.quit()
