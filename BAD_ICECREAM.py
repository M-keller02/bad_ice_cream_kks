import random, pygame, sys
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

class Ice:
    def __init__(self):
        self.koord={"x":1,"y":1}
        self.richtung={"dx":0,"dy":0}

class Spiel:
    def __init__(self, groesse):
        self.felder = [[0 for j in range(groesse)] for i in range(groesse)]

        for i in range(groesse):
            self.felder[0][i] = 1
            self.felder[groesse - 1][i] = 1
            self.felder[i][0] = 1
            self.felder[i][groesse - 1] = 1


def makeGUI():
    FPS = 10
    BOARD_HEIGHT = 665
    BOARD_LENGTH = BOARD_HEIGHT
    CELLSIZE = 35

    assert BOARD_LENGTH % CELLSIZE == 0
    assert BOARD_HEIGHT % CELLSIZE == 0
    CELLWIDTH = int(BOARD_LENGTH / CELLSIZE)
    CELLHEIGHT = int(BOARD_HEIGHT / CELLSIZE)

    ice=Ice()

    my_feld=Spiel(CELLSIZE)


    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((BOARD_LENGTH, BOARD_HEIGHT))
    pygame.display.set_caption('Bad Ice Cream')


    while True:  # main game loop
        DISPLAYSURF.fill(HBLUE)

        for event in pygame.event.get():

                if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        if ice.richtung["dx"] == 0:
                            ice.richtung["dx"] = -1
                            ice.richtung["dy"] = 0
                        elif ice.richtung["dx"] == 1:
                            ice.richtung["dx"] == 0
                            ice.richtung["dy"] = 0
                    elif event.key == pygame.K_s:
                        if ice.richtung["dx"] == -1:
                            ice.richtung["dx"] = 0
                            ice.richtung["dy"] = 0
                        elif ice.richtung["dx"] == 0:
                            ice.richtung["dx"] = 1
                            ice.richtung["dy"] = 0
                    elif event.key == pygame.K_a:
                        if ice.richtung["dy"] == 0:
                            ice.richtung["dy"] = -1
                            ice.richtung["dx"] = 0
                        elif ice.richtung["dy"] == 1:
                            ice.richtung["dy"] = 0
                            ice.richtung["dx"] = 0
                    elif event.key == pygame.K_d:
                        if ice.richtung["dy"] == -1:
                            ice.richtung["dy"] = 0
                            ice.richtung["dx"] = 0
                        elif ice.richtung["dy"] == 0:
                            ice.richtung["dy"] = 1
                            ice.richtung["dx"] = 0



        for x in range(0, BOARD_LENGTH, CELLSIZE):
            pygame.draw.line(DISPLAYSURF, BLACK, (x, 0), (x, BOARD_HEIGHT))
        for y in range(0, BOARD_HEIGHT, CELLSIZE):
            pygame.draw.line(DISPLAYSURF, BLACK, (0, y), (BOARD_LENGTH, y))

        if my_feld.felder[ice.koord['x'] + ice.richtung['dx']][ice.koord['y'] + ice.richtung['dy']] == 0:
            ice.koord['x'] = ice.koord['x'] + ice.richtung['dx']
            ice.koord['y'] = ice.koord['y'] + ice.richtung['dy']
        else:
            my_feld.ice['dy'] = 0
            my_feld.ice['dx'] = 0

        make_rectangle_ice(ice.koord, DISPLAYSURF, CELLSIZE)

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def board_to_pixel_koord(i, j, width):
    return j * width, i * width


def make_rectangle_ice(dict, display, size):
    x, y = board_to_pixel_koord(dict["x"], dict["y"], size)
    the_rect = pygame.Rect(x, y, size, size)
    pygame.draw.rect(display, BLACK, the_rect)


if __name__ == '__main__':
    makeGUI()