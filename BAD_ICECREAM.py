import pygame, sys
from pygame.locals import *

#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
BLUE      = (  0,   0, 255)
HBLUE      =(150,150,255)
DARKGRAY  = ( 40,  40,  40)

class Monster:
    def __init__(self):
        pass

class Fruits:
    def __init__(self):
        pass

class Spiel:
    def __init__(self, groesse):
        self.felder = [[0 for j in range(groesse)] for i in range(groesse)]

        for i in range(groesse):
            self.felder[0][i] = 1
            self.felder[groesse-1][i] = 1
            self.felder[i][0] = 1
            self.felder[i][groesse-1] = 1

def makeGUI():
    FPS = 10
    BOARD_HEIGHT = 665
    BOARD_LENGTH = BOARD_HEIGHT
    CELLSIZE = 35

    DISPLAYSURF = pygame.display.set_mode((BOARD_LENGTH, BOARD_HEIGHT))
    pygame.display.set_caption('Bad Ice Cream')


    while True:  # main game loop
        DISPLAYSURF.fill(HBLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
        else:
            for x in range(0, BOARD_LENGTH, CELLSIZE):  # draw vertical lines
                pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, BOARD_HEIGHT))
            for y in range(0, BOARD_HEIGHT, CELLSIZE):  # draw horizontal lines
                pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (BOARD_LENGTH, y))

        pygame.display.update()



if __name__ == '__main__':
    makeGUI()