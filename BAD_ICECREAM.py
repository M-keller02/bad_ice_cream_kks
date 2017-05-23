import pygame, sys, random
from pygame.locals import *


#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
BLUE      = (  0,   0, 255)
DARKGRAY  = ( 40,  40,  40)
VIOLETTE=   (139, 0, 139)


class Spielfeld:
    def __init__(self, rastergroesse):
        self.felder = [[0 for x in range(rastergroesse)] for y in range(rastergroesse)]

        for i in range(rastergroesse):
            self.felder[0][i] = 1
            self.felder[rastergroesse-1][i] = 1
            self.felder[i][0] = 1
            self.felder[i][rastergroesse-1] = 1

        self.spieler = [14, 14]
        self.frucht =[13, 10]
        self.frucht2=[5,1]
        self.feind=[10,10]

positions_walls_level1= [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11],
                    [0, 12], [0, 13], [0, 14], [0, 15], [0, 16], [0, 17], [0, 18],
                    [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0],
                    [12, 0], [13, 0], [14, 0], [15, 0], [16, 0], [17, 0], [18, 0],
                    [1, 17], [2, 17], [3, 17], [4, 17], [5, 17], [6, 17], [7, 17], [8, 17], [9, 17], [10, 17],
                    [11, 17], [12, 17], [13, 17], [14, 17], [15, 17], [16, 17], [17, 17],
                    [17, 1], [17, 2], [17, 3], [17, 4], [17, 5], [17, 6], [17, 7], [17, 8], [17, 9], [17, 10],
                    [17, 11], [17, 12], [17, 13], [17, 14], [17, 15], [17, 16], [17, 17],[2,2]]

positions_walls_level2= [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11],
                    [0, 12], [0, 13], [0, 14], [0, 15], [0, 16], [0, 17], [0, 18],
                    [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0],
                    [12, 0], [13, 0], [14, 0], [15, 0], [16, 0], [17, 0], [18, 0],
                    [1, 17], [2, 17], [3, 17], [4, 17], [5, 17], [6, 17], [7, 17], [8, 17], [9, 17], [10, 17],
                    [11, 17], [12, 17], [13, 17], [14, 17], [15, 17], [16, 17], [17, 17],
                    [17, 1], [17, 2], [17, 3], [17, 4], [17, 5], [17, 6], [17, 7], [17, 8], [17, 9], [17, 10],
                    [17, 11], [17, 12], [17, 13], [17, 14], [17, 15], [17, 16], [17, 17],[15,15]]
# Spielfigur laden
player = pygame.image.load('Spieler_t.png')
# Frucht laden
fruit = pygame.image.load("peach.png")
# gegner laden
enemy = pygame.image.load("feind.png")
# boden laden
floor = pygame.image.load("hint.jpg")
# wand laden
wall = pygame.image.load("wand.png")

menu=pygame.image.load("menu.jpg")



def makeMenu(Status):
    FPS = 10
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((720, 720))
    pygame.display.set_caption('Bad Ice Cream')

    pygame.key.set_repeat(50, 50)

    font = pygame.font.SysFont('comicsansms', 75)
    text_1 = font.render('Level 1', True, WHITE)
    text_2 = font.render('Level 2', True, WHITE)

    text_rect_1 = text_1.get_rect()
    text_rect_2 = text_2.get_rect()

    text_rect_1.center = (175, 300)
    text_rect_2.center = (525, 300)


    while True:
        DISPLAYSURF.fill(DARKGRAY)
        DISPLAYSURF.fill(DARKGRAY, text_rect_1)
        DISPLAYSURF.fill(DARKGRAY, text_rect_2)
        DISPLAYSURF.blit(text_1, text_rect_1)
        DISPLAYSURF.blit(text_2, text_rect_2)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > 75 and x < 275 and y < 325 and y > 275:
                    pygame.quit()
                    return (1)
                elif x > 425 and x < 625 and y < 325 and y > 275:
                    pygame.quit()
                    return (2)
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def makeGUI(Level):
    FPS = 10
    cellx = 18
    celly = cellx
    cellsize = 40
    length = cellx * cellsize
    height = celly * cellsize
    my_feld = Spielfeld(cellx)
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((length, height))
    pygame.display.set_caption('Bad Ice Cream')
    pygame.key.set_repeat(50, 50)

# Schrift
    font = pygame.font.SysFont('comicsansms', 72)
    font2 = pygame.font.SysFont('comicsansms', 36)
    text = font.render('GAME OVER!', True, BLACK)
    text2 = font2.render('PRESS ESC TO QUIT', True, BLACK)
    text3 = font.render('LEVEL COMPLETED!', True, BLACK)
    text4 = font2.render('PRESS R TO RESTART OR M FOR THE MENU', True, BLACK)
    textRect = text.get_rect()
    textRect2 = text2.get_rect()
    textRect3 = text3.get_rect()
    textRect4 = text4.get_rect()
    textRect.center = (length / 2, height / 2 - 20)
    textRect2.center = (length / 2, height / 2 + 40)
    textRect3.center = (length / 2, height / 2 - 20)
    textRect4.center = (length / 2, height / 2 + 75)

#variabeln

    eaten_fruit=0
    feind_kill=0

    if Level==1:
        positions_walls=positions_walls_level1
    elif Level==2:
        positions_walls=positions_walls_level2


    while True:
        DISPLAYSURF.fill(WHITE)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

#Bewegung des Spielers
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


            if my_feld.spieler[0] == my_feld.frucht[0] and my_feld.spieler[1] == my_feld.frucht[1]:
                print("Frucht weg")
                my_feld.frucht[0] = cellx + 1
                my_feld.frucht[1] = celly + 1
                eaten_fruit += 1

            if my_feld.spieler[0] == my_feld.frucht2[0] and my_feld.spieler[1] == my_feld.frucht2[1]:
                print("Frucht weg")
                my_feld.frucht2[0] = cellx + 1
                my_feld.frucht2[1] = celly + 1
                eaten_fruit += 1

            if my_feld.spieler[0] == my_feld.feind[0] and my_feld.spieler[1] == my_feld.feind[1]:
                print("Du bist tot")
                my_feld.feind[0] = cellx + 1
                my_feld.feind[1] = celly + 1
                feind_kill += 1


#Gitterlinien
        for x in range(0, length, cellsize):
            pygame.draw.line(DISPLAYSURF, BLACK, (x,0),(x,length))

        for y in range(0, height, cellsize):
            pygame.draw.line(DISPLAYSURF, BLACK, (0, y),(height,y))

#Boden
        draw_ground(floor, cellsize, DISPLAYSURF)

#Wand
        draw_walls(positions_walls, wall, cellsize, DISPLAYSURF)

#Spieler auf Spielfeld generieren
        DISPLAYSURF.blit(player, board_to_pixel_koord(my_feld.spieler[0], my_feld.spieler[1], cellsize))

#Frucht auf Spielfeld generieren
        DISPLAYSURF.blit(fruit, board_to_pixel_koord(my_feld.frucht[0], my_feld.frucht[1],cellsize))
        DISPLAYSURF.blit(fruit, board_to_pixel_koord(my_feld.frucht2[0], my_feld.frucht2[1], cellsize))

#Gegener auf Spielfeld generieren
        DISPLAYSURF.blit(enemy, board_to_pixel_koord(my_feld.feind[0], my_feld.feind[1], cellsize))


        if eaten_fruit == 2:
            DISPLAYSURF.fill(GREEN)
            DISPLAYSURF.blit(text3, textRect3)
            DISPLAYSURF.blit(text2, textRect2)
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                        pygame.quit()
                        sys.exit()

# Feind
        fein_bewegen(my_feld.feind, my_feld.spieler)
        if (my_feld.spieler[0] == my_feld.feind[0] and my_feld.spieler[1] == my_feld.feind[1]):
            DISPLAYSURF.fill(RED)
            DISPLAYSURF.blit(text, textRect)
            DISPLAYSURF.blit(text2, textRect2)
            DISPLAYSURF.blit(text4, textRect4)
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == pygame.K_r:
                            makeGUI(Level)
                        elif event.key==pygame.K_m:
                            makeMenu(Level)

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def board_to_pixel_koord(i, j, width):
    return j * width, i * width

#Boden
def draw_ground(picture, zellgroesse, DISPLAYSURF):
    DISPLAYSURF.blit(picture, board_to_pixel_koord(0, 0, zellgroesse))

#Wand aussen
def draw_walls(positions, picture, zellgroesse, DISPLAYSURF):
    for i in range (0,(len(positions))):
        DISPLAYSURF.blit(picture, board_to_pixel_koord(positions[i][0], positions[i][1], zellgroesse))

#Feindbewegen
def fein_bewegen(feind, spieler):

    x=random.randint(0,1)
    if x==0:
        if spieler[0]>feind[0]:
            feind[0]+=0.5
        elif spieler[0]< feind[0]:
            feind[0]-=0.5
        else:
            if spieler[1] > feind[1]:
                feind[1] += 0.5
            elif spieler[1] < feind[1]:
                feind[1] -= 0.5
            else:
                pass
    elif x==1:
        if spieler[1]>feind[1]:
            feind[1]+=0.5
        elif spieler[1]< feind[1]:
            feind[1]-=0.5
        else:
            if spieler[0] > feind[0]:
                feind[0] += 0.5
            elif spieler[0] < feind[0]:
                feind[0] -= 0.5
            else:
                pass



def make_rectangle_ice(dict, display, size):
    x, y = board_to_pixel_koord(dict["x"], dict["y"], size)
    the_rect = pygame.Rect(x, y, size, size)
    pygame.draw.rect(display, BLACK, the_rect)


if __name__ == '__main__':
    v=True
    while (v==1):
        Level= makeMenu(1)
        v=makeGUI(Level)