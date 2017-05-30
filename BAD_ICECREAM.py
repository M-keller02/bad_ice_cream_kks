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

        self.feind=[10,10]

positions_walls_level1= [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11],
                    [0, 12], [0, 13], [0, 14], [0, 15], [0, 16], [0, 17], [0, 18],
                    [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0],
                    [12, 0], [13, 0], [14, 0], [15, 0], [16, 0], [17, 0], [18, 0],
                    [1, 17], [2, 17], [3, 17], [4, 17], [5, 17], [6, 17], [7, 17], [8, 17], [9, 17], [10, 17],
                    [11, 17], [12, 17], [13, 17], [14, 17], [15, 17], [16, 17], [17, 17],
                    [17, 1], [17, 2], [17, 3], [17, 4], [17, 5], [17, 6], [17, 7], [17, 8], [17, 9], [17, 10],
                    [17, 11], [17, 12], [17, 13], [17, 14], [17, 15], [17, 16], [17, 17],[3,6],[3,7],[3,8],[3,9],[3,10],[3,11],
                    [6,3],[7,3],[8,3],[9,3], [10, 3],[11,3],[14,6],[14,7],[14,8],[14,9],[14,10],[14,11],[6,14],[7,14],[8,14],
                    [9,14],[10,14],[11,14],[7,6], [7,7], [6,7],[6,10],[7,10], [7,11],[10,6],[10,7],[11,7],[10,10],[10,11],[11,10]]

positions_fruit_level1= [[3,3],[3,14],[14,3],[14,14],[6,6],[6,11],[11,6],[11,11]]

positions_walls_level2= [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11],
                    [0, 12], [0, 13], [0, 14], [0, 15], [0, 16], [0, 17], [0, 18],
                    [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0],
                    [12, 0], [13, 0], [14, 0], [15, 0], [16, 0], [17, 0], [18, 0],
                    [1, 17], [2, 17], [3, 17], [4, 17], [5, 17], [6, 17], [7, 17], [8, 17], [9, 17], [10, 17],
                    [11, 17], [12, 17], [13, 17], [14, 17], [15, 17], [16, 17], [17, 17],
                    [17, 1], [17, 2], [17, 3], [17, 4], [17, 5], [17, 6], [17, 7], [17, 8], [17, 9], [17, 10],
                    [17, 11], [17, 12], [17, 13], [17, 14], [17, 15], [17, 16], [17, 17],[2,7],[2,8],[2,9],[2,10],[3,8],[3,9],
                    [2,2],[2,3],[2,4],[3,2],[4,2],[2,15],[2,14],[2,13],[3,15],[4,15],[4,13],[6,13],[5,13],[6,15],[7,15],[8,15],
                    [9, 15],[10,15],[11,15],[11,13],[12,13],[13,13],[13,15],[14,15],[15,15],[15,14],[15,13],[15,7],[15,8],[15,9],[15,10],
                    [14,8],[14,9], [15,2], [15,3], [15,4],[14,2],[13,2],[13,4],[12,4],[11,4],[11,2],[10,2],[9,2],[8,2],[7,2],[6,2],[6,4],[4,4],
                    [7,7],[7,8],[7,10],[8,8],[8,9],[8,10],[9,7],[9,8],[9,9],[10,7],[10,9],[10,10],[5,4]]

positios_fruit_level2= [[1,1],[1,16],[16,1],[16,16],[7,9],[8,7],[9,10],[10,8]]

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



def makeMenu():
    FPS = 10
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((720, 720))
    pygame.display.set_caption('Bad Ice Cream')

    pygame.key.set_repeat(50, 50)

    font = pygame.font.SysFont('comicsansms', 75)
    font2=pygame.font.SysFont('comicsansms', 30)
    text_1 = font.render('Level 1', True, WHITE)
    text_2 = font.render('Level 2', True, WHITE)
    text_3= font2.render('Created by Luca and Michael', True, WHITE)

    text_rect_1 = text_1.get_rect()
    text_rect_2 = text_2.get_rect()
    text_rect_3=text_3.get_rect()
    text_rect_4=menu.get_rect()

    text_rect_1.center = (175, 350)
    text_rect_2.center = (525, 350)
    text_rect_3.center= (360,500)
    text_rect_4.center=(360,150)


    while True:
        DISPLAYSURF.fill(DARKGRAY)
        DISPLAYSURF.fill(DARKGRAY, text_rect_1)
        DISPLAYSURF.fill(DARKGRAY, text_rect_2)
        DISPLAYSURF.blit(text_1, text_rect_1)
        DISPLAYSURF.blit(text_2, text_rect_2)
        DISPLAYSURF.blit(text_3,text_rect_3)
        DISPLAYSURF.blit(menu, text_rect_4)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > 75 and x < 275 and y < 375 and y > 325:
                    pygame.quit()
                    return (1)
                elif x > 425 and x < 625 and y < 375 and y > 325:
                    pygame.quit()
                    return (2)
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def makeGUI(Level,Fruit):
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
    if Fruit==1:
        positions_furcht=positions_fruit_level1
    elif Fruit==2:
        positions_furcht=positios_fruit_level2


    while True:
        DISPLAYSURF.fill(WHITE)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

#Bewegung des Spielers
            elif event.type == KEYDOWN:
                if event.key == K_d and check_walls(positions_walls, my_feld, 'down') != 0:
                         my_feld.spieler[1] += 1

                elif event.key == K_a and check_walls(positions_walls, my_feld, 'up') != 0:
                    my_feld.spieler[1] -= 1

                elif event.key == K_w and check_walls(positions_walls, my_feld, 'left') != 0:
                    my_feld.spieler[0] -= 1

                elif event.key == K_s and check_walls(positions_walls, my_feld, 'right') != 0:
                    my_feld.spieler[0] += 1

# Frucht essen
            check_fruits(positions_furcht, my_feld)
            for i in range(len(positions_furcht)):
                if positions_furcht== my_feld.spieler and my_feld.positions_furcht[i][1] == my_feld.spieler:
                    eaten_fruit += 1
                    print("Frücht weg")

            if eaten_fruit == len(positions_furcht):
                DISPLAYSURF.fill(GREEN)
                DISPLAYSURF.blit(text3, textRect3)
                DISPLAYSURF.blit(text2, textRect2)
                pygame.display.update()
                while True:
                    for event in pygame.event.get():
                        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                            pygame.quit()
                            sys.exit()

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
        draw_fruits(positions_furcht,fruit, cellsize,DISPLAYSURF)
#Gegener auf Spielfeld generieren
        DISPLAYSURF.blit(enemy, board_to_pixel_koord(my_feld.feind[0], my_feld.feind[1], cellsize))


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
                            makeMenu()

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
#Fruechte zeichnen
def draw_fruits(positions, picture, zellgroesse, DISPLAYSURF):
    for i in range(0, (len(positions))):
        DISPLAYSURF.blit(picture, board_to_pixel_koord(positions[i][0], positions[i][1], zellgroesse))

def check_fruits(positions, my_feld):
    for i in range(len(positions)):
        e = 0
        if my_feld.spieler[0] == positions[i][0] and my_feld.spieler[1] == positions[i][1]:
            positions[i][0] = 30
            positions[i][1] = 30
            e = 1

#Feindbewegen
def fein_bewegen(feind, spieler):

    x=random.randint(0,1)
    if x==0:
        if spieler[0]>feind[0]:
            feind[0]+=0.25
        elif spieler[0]< feind[0]:
            feind[0]-=0.25
        else:
            if spieler[1] > feind[1]:
                feind[1] += 0.25
            elif spieler[1] < feind[1]:
                feind[1] -= 0.25
            else:
                pass
    elif x==1:
        if spieler[1]>feind[1]:
            feind[1]+=0.25
        elif spieler[1]< feind[1]:
            feind[1]-=0.25
        else:
            if spieler[0] > feind[0]:
                feind[0] += 0.25
            elif spieler[0] < feind[0]:
                feind[0] -= 0.25
            else:
                pass


def check_walls(positions, my_feld, direction):
        if direction == 'right':
            for i in range (len(positions)):
                if (my_feld.spieler[0]+1) == positions[i][0] and my_feld.spieler[1] == positions[i][1]:
                    return(0)
        if direction == 'left':
            for i in range (len(positions)):
                if (my_feld.spieler[0]-1) == positions[i][0] and my_feld.spieler[1] == positions[i][1]:
                    return(0)
        if direction == 'up':
            for i in range (len(positions)):
                if (my_feld.spieler[0]) == positions[i][0] and (my_feld.spieler[1]-1) == positions[i][1]:
                    return(0)
        if direction == 'down':
            for i in range (len(positions)):
                if (my_feld.spieler[0]) == positions[i][0] and (my_feld.spieler[1]+1) == positions[i][1]:
                    return(0)



def make_rectangle_ice(dict, display, size):
    x, y = board_to_pixel_koord(dict["x"], dict["y"], size)
    the_rect = pygame.Rect(x, y, size, size)
    pygame.draw.rect(display, BLACK, the_rect)


if __name__ == '__main__':
    v=True
    while (v==1):
        Level= makeMenu()
        Fruit= Level
        v=makeGUI(Level,Fruit)