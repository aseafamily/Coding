import pygame, sys
import time
pygame.init()
pygame.mixer.music.load('C:/GitHub/Coding/Emily/sounds/bg_music.mp3')
pygame.mixer.music.set_volume(0.30)
pygame.mixer.music.play()
splat = pygame.mixer.Sound('C:/GitHub/Coding/Emily/sounds/splat.wav')
splat.set_volume(0.50)
splat.play()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()