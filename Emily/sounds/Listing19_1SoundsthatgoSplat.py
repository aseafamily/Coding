import pygame, sys
import time
pygame.init()

screen = pygame.display.set_mode([640, 480])
something = True
'''while something:
    splat = pygame.mixer.Sound('C:\GitHub\Coding\Emily\sounds/splat.wav')
    splat.play()
    time.sleep(1)'''

for splaty in range(1, 6):
    splat = pygame.mixer.Sound('C:\GitHub\Coding\Emily\sounds/splat.wav')
    splat.play()
    time.sleep(1)
    
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()