import pygame, sys
pygame.init()

dots = [[100, 0], [100, 700]]
dots1 = [[200, 0], [200, 700]]
dots2 = [[300, 0], [300, 700]]
dots3 = [[400, 0], [400, 700]]
dots4 = [[500,0], [500,700]]
dots5 = [[600,0], [600,700]]
screen = pygame.display.set_mode([700, 700])
screen.fill([255, 255, 255])
pygame.draw.lines(screen, [0,0,0], True, dots, 2)
pygame.draw.lines(screen, [0,0,0], True, dots1, 2)
pygame.draw.lines(screen, [0,0,0], True, dots2, 2)
pygame.draw.lines(screen, [0,0,0], True, dots3, 2)
pygame.draw.lines(screen, [0,0,0], True, dots4, 2)
pygame.draw.lines(screen, [0,0,0], True, dots5, 2)
A = pygame.mixer.Sound("noteA.wav")
B = pygame.mixer.Sound("noteB.wav")
C = pygame.mixer.Sound("noteC.wav")
D = pygame.mixer.Sound("noteD.wav")
E = pygame.mixer.Sound("noteE.wav")
F = pygame.mixer.Sound("noteF.wav")
G = pygame.mixer.Sound("noteG.wav")
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            # Find which key is clicked
            if x < 100:
                print('A')
                A.play()
            elif 100 < x < 200:
                print('B')
                B.play()
            elif 200 < x < 300:
                print('C')
                C.play()
            elif 300 < x < 400:
                print('D')
                D.play()
            elif 400 < x < 500:
                print('E')
                E.play()
            elif 500 < x < 600:
                print('F')
                F.play()
            elif 600 < x < 700:
                print('G')
                G.play()
            
pygame.quit()