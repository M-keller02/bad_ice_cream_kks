import random, pygame, sys
from pygame.locals import *

#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
BLUE      = (  0,   0, 255)
DARKGRAY  = ( 40,  40,  40)



class Spiel:
    def __init__(self, groesse):
        self.felder = [[0 for j in range(groesse)] for i in range(groesse)]

        for i in range(groesse):
            self.felder[0][i] = 1
            self.felder[groesse-1][i] = 1
            self.felder[i][0] = 1
            self.felder[i][groesse-1] = 1

        self.der_rote = [random.randint(2, groesse-2), random.randint(2, groesse-2)]


def makeGUI():
    FPS = 10
    WINDOWWIDTH = 540
    WINDOWHEIGHT = WINDOWWIDTH
    CELLSIZE = 20

    assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
    assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
    CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
    CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

    my_feld = Spiel(CELLWIDTH)


    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Gitterbeispiel')

    #pygame.key.set_repeat(50, 50)
    while True: # the main game loop
        DISPLAYSURF.fill(WHITE)

        for event in pygame.event.get(): # event handling loop

            if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Der Rote
                if event.key == pygame.K_DOWN and  \
                                my_feld.felder[my_feld.der_rote[0] + 1][my_feld.der_rote[1]] == 0:
                     my_feld.der_rote[0] += 1
                elif event.key == pygame.K_UP and \
                                my_feld.felder[my_feld.der_rote[0] - 1][my_feld.der_rote[1]] == 0:
                    my_feld.der_rote[0] -= 1
                elif event.key == pygame.K_LEFT and \
                                my_feld.felder[my_feld.der_rote[0]][my_feld.der_rote[1]-1] == 0:
                    my_feld.der_rote[1] -= 1
                elif event.key == pygame.K_RIGHT and \
                                my_feld.felder[my_feld.der_rote[0]][my_feld.der_rote[1]+1] == 0:
                    my_feld.der_rote[1] += 1


        for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
             pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
        for y in range(0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
             pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))

        for i in range(len(my_feld.felder)):
            for j in range(len(my_feld.felder[i])):
                if my_feld.felder[i][j] == 1:
                    x, y = board_to_pixel_koord(i,j, CELLSIZE)
                    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
                    pygame.draw.rect(DISPLAYSURF, BLACK, appleRect)

        make_rectangle_red(my_feld.der_rote, DISPLAYSURF, CELLSIZE)

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def board_to_pixel_koord(i,j,width):
    return j*width, i*width

def pixel_to_board_koord(x,y,width):
    return y // width, x // width

def make_rectangle_red(liste, display, size):
    x, y = board_to_pixel_koord(liste[0], liste[1], size)
    the_rect = pygame.Rect(x, y, size, size)
    pygame.draw.rect(display, RED, the_rect)


if __name__ == '__main__':
    makeGUI()