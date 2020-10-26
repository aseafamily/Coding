import pygame, sys
import time
pygame.init()

screen = pygame.display.set_mode([640, 480])
something = True

pygame.mixer.music.load('C:\GitHub\Coding\Emily\sounds/bg_music.mp3')
pygame.mixer.music.play()
    
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()