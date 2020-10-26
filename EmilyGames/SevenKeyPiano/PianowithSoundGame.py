#random beginning things
import pygame, sys
pygame.init()

#coordinates for the lines
linenumber1 = [[100, 0], [100, 600]]
linenumber2 = [[200, 0], [200, 600]]
linenumber3 = [[300, 0], [300, 600]]
linenumber4 = [[400, 0], [400, 600]]
linenumber5 = [[500, 0], [500, 600]]
linenumber6 = [[600, 0], [600, 600]]
linewhat = [[0,0], [700,0]]
lineever = [[0,596], [700,596]]

#screen stuff
screen = pygame.display.set_mode([700,600])
screen.fill([255,255,255])

#drawing lines
pygame.draw.lines(screen, [0,0,0], True, linenumber1, 2)
pygame.draw.lines(screen, [0,0,0], True, linenumber2, 2)
pygame.draw.lines(screen, [0,0,0], True, linenumber3, 2)
pygame.draw.lines(screen, [0,0,0], True, linenumber4, 2)
pygame.draw.lines(screen, [0,0,0], True, linenumber5, 2)
pygame.draw.lines(screen, [0,0,0], True, linenumber6, 2)
pygame.draw.lines(screen, [0,0,0], True, linewhat, 4)
pygame.draw.lines(screen, [0,0,0], True, lineever, 4)

#importing sound files
#splaty = pygame.mixer.Sound('C:/GitHub/Coding/Emily/OOProjects/splat.wav')
notea = pygame.mixer.Sound('C:/GitHub/Coding/Emily/OOProjects/NoteA.wav')
noteb = pygame.mixer.Sound('C:/GitHub/Coding/Emily/OOProjects/NoteB.wav')
notec = pygame.mixer.Sound('C:/GitHub/Coding/Emily/OOProjects/NoteC.wav')
noted = pygame.mixer.Sound('C:/GitHub/Coding/Emily/OOProjects/NoteD.wav')
notee = pygame.mixer.Sound('C:/GitHub/Coding/Emily/OOProjects/NoteE.wav')
notef = pygame.mixer.Sound('C:/GitHub/Coding/Emily/OOProjects/NoteF.wav')
noteg = pygame.mixer.Sound('C:/GitHub/Coding/Emily/OOProjects/NoteG.wav')
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_1:
        #         pygame.mixer.music.play()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousex, y = event.pos
            if mousex < 100:
                notea.play()
            elif 100 < mousex < 200:
                noteb.play()
            elif 200 < mousex < 300:
                notec.play()
            elif 300 < mousex < 400:
                noted.play()
            elif 400 < mousex < 500:
                notee.play()
            elif 500 < mousex < 600:
                notef.play()
            elif 600 < mousex < 700:
                noteg.play()
    pygame.display.flip()
pygame.quit()