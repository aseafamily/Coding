import pygame, sys, time
pygame.init()
screen = pygame.display.set_mode([640, 480])
splat = pygame.mixer.music.load("bg_music.mp3")
pygame.mixer.music.set_volume(0.30)
splat = pygame.mixer.Sound("C:/GitHub/Coding/andrew/splat.wav")
splat.set_volume(0.50)
for i in range(0, 5):
    splat.play()
    pygame.mixer.music.play()
    time.sleep(1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit