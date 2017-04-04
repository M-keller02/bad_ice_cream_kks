import random, pygame, sys
from pygame.locals import *
import random as rd

#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
BLUE      = (  0,   0, 255)
DARKGRAY  = ( 40,  40,  40)


class Spielfeld:
    def __init__(self, rastergroesse):
        self.felder = [[0 for xr in range(rastergroesse)] for yr in range(rastergroesse)]

        for i in range(rastergroesse):
            self.felder[0][i] = 1
            self.felder[rastergroesse-1][i] = 1
            self.felder[i][0] = 1
            self.felder[i][rastergroesse-1] = 1

        self.spieler = [16, 15]
        self.frucht =[10, 10]


def makeGUI():
    FPS = 10
    #Zellenangaben und Board
    cellx = 18
    celly = cellx
    cellsize = 40
    length = cellx * cellsize
    height = celly * cellsize
    my_feld = Spielfeld(cellx)


    #Spielfigur laden
    player = pygame.image.load('Spieler_t.png')

    #Frucht laden
    fruit=pygame.image.load("peach.png")




    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((length, height))
    pygame.display.set_caption('Bad Ice Cream')

    pygame.key.set_repeat(50, 50)

    while True:
        DISPLAYSURF.fill(WHITE)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if (event.key == K_d or event.key == K_RIGHT) and  \
                                my_feld.felder[my_feld.spieler[0]][my_feld.spieler[1] + 1] == 0:
                         my_feld.spieler[1] += 1
                elif (event.key == K_a or event.key == K_LEFT) and \
                                my_feld.felder[my_feld.spieler[0]][my_feld.spieler[1] - 1] == 0:
                    my_feld.spieler[1] -= 1
                elif (event.key == K_w or event.key == K_UP) and \
                                my_feld.felder[my_feld.spieler[0] - 1][my_feld.spieler[1]] == 0:
                    my_feld.spieler[0] -= 1
                elif (event.key == K_s or event.key == K_DOWN) and \
                                my_feld.felder[my_feld.spieler[0] + 1][my_feld.spieler[1]] == 0:
                    my_feld.spieler[0] += 1


        #Gitterlinien
        for x in range(0, length, cellsize):
            pygame.draw.line(DISPLAYSURF, BLACK, (x,0),(x,length))

        for y in range(0, height, cellsize):
            pygame.draw.line(DISPLAYSURF, BLACK, (0, y),(height,y))

        # Rand
        for i in range(len(my_feld.felder)):
            for j in range(len(my_feld.felder[i])):
                if my_feld.felder[i][j] == 1:
                    x, y = board_to_pixel_koord(i,j, cellsize)
                    feld = pygame.Rect(x, y, cellsize, cellsize)
                    pygame.draw.rect(DISPLAYSURF, BLACK, feld)

        #Spieler auf Spielfeld generieren
        DISPLAYSURF.blit(player, board_to_pixel_koord(my_feld.spieler[0], my_feld.spieler[1], cellsize))
        #Frucht auf Spielfeld generieren
        DISPLAYSURF.blit(fruit, board_to_pixel_koord(my_feld.frucht[0], my_feld.frucht[1],cellsize))


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