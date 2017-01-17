import pygame, sys
from pygame.locals import *

#             R    G    B
WHITE     = (255, 255, 255)
SNOW       =(255,255,190)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
BLUE      = (  0,   0, 255)
DARKGRAY  = ( 40,  40,  40)


def make_GUI():
    FPS = 20
    BOARD_LENGTH = 600
    BOARD_HEIGHT = BOARD_LENGTH
    Cellsize = BOARD_LENGTH/12

    pygame.init()

    DISPLAYSURF = pygame.display.set_mode((BOARD_LENGTH, BOARD_HEIGHT))
    pygame.display.set_caption('BAD ICECREAM')

    DISPLAYSURF.fill(SNOW)
    while True: # main game loop
        for event in pygame.event.get():  # event handling loop

            if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Der Rote
                if event.key == pygame.K_DOWN and \
                                my_feld.felder[my_feld.der_rote[0] + 1][my_feld.der_rote[1]] == 0:
                    my_feld.der_rote[0] += 1
                elif event.key == pygame.K_UP and \
                                my_feld.felder[my_feld.der_rote[0] - 1][my_feld.der_rote[1]] == 0:
                    my_feld.der_rote[0] -= 1
                elif event.key == pygame.K_LEFT and \
                                my_feld.felder[my_feld.der_rote[0]][my_feld.der_rote[1] - 1] == 0:
                    my_feld.der_rote[1] -= 1
                elif event.key == pygame.K_RIGHT and \
                                my_feld.felder[my_feld.der_rote[0]][my_feld.der_rote[1] + 1] == 0:
                    my_feld.der_rote[1] += 1

        pygame.display.update()

make_GUI()
print("Hallo Luka")
