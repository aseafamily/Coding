import pygame, sys, time
pygame.init()

screen = pygame.display.set_mode([640, 480])
splat = pygame.mixer.music.load("bg_music.mp3")
for i in range(0, 5):
    pygame.mixer.music.play()
    time.sleep(1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit