import pygame, sys, random, time
from pygame. locals import *

#         R   G   B
white = (255 ,255 ,255)
black = (0, 0, 0)
grey  = (80, 80, 80)
red   = (255, 0, 0)
green = (50, 205, 50)


class Board:
    def __init__(self, rastergroesse):
        self.felder = [[0 for i in range(rastergroesse)] for j in range(rastergroesse)]

        for i in range(rastergroesse):
            self.felder[0][i] = 1
            self.felder[rastergroesse-1][i] = 1
            self.felder[i][0] = 1
            self.felder[i][rastergroesse-1] = 1

        self.spieler1 = [10, 10]
        self.enemy1 = [2, 2]
        self.enemy2 = [2, 18]
        self.enemy3 = [18, 18]
        self.enemy4 = [18, 2]

positions_fruits = []
positions_walls_Level1 = [[11,7],[12,7],[12,8],[12,11],[12,12],[11,12],[8,12],[7,12],[7,11],[7,8],[7,7],[8,7],[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],[0,10],[0,11],[0,12],[0,13],[0,14],[0,15],[0,16],[0,17],[0,18],[0,19],[19,0],[19,1],[19,2],[19,3],[19,4],[19,5],[19,6],[19,7],[19,8],[19,9],[19,10],[19,11],[19,12],[19,13],[19,14],[19,15],[19,16],[19,17],[19,18],[19,19],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0],[13,0],[14,0],[15,0],[16,0],[17,0],[18,0],[1,19],[2,19],[3,19],[4,19],[5,19],[6,19],[7,19],[8,19],[9,19],[10,19],[11,19],[12,19],[13,19],[14,19],[15,19],[16,19],[17,19],[18,19]]
positions_walls_Level2 = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],[0,10],[0,11],[0,12],[0,13],[0,14],[0,15],[0,16],[0,17],[0,18],[0,19],[19,0],[19,1],[19,2],[19,3],[19,4],[19,5],[19,6],[19,7],[19,8],[19,9],[19,10],[19,11],[19,12],[19,13],[19,14],[19,15],[19,16],[19,17],[19,18],[19,19],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0],[13,0],[14,0],[15,0],[16,0],[17,0],[18,0],[1,19],[2,19],[3,19],[4,19],[5,19],[6,19],[7,19],[8,19],[9,19],[10,19],[11,19],[12,19],[13,19],[14,19],[15,19],[16,19],[17,19],[18,19],[3,3],[3,4],[4,3],[8,3],[7,3],[12,3],[11,3],[15,3],[16,3],[16,4],[16,7],[16,8],[16,12],[16,11],[16,15],[16,16],[15,16],[12,16],[11,16],[8,16],[7,16],[4,16],[3,16],[3,15],[3,12],[3,11],[3,8],[3,7],[6,6],[6,7],[6,8],[6,9],[6,10],[6,11],[6,12],[6,13],[13,6],[13,7],[13,8],[13,9],[13,10],[13,11],[13,12],[13,13],[9,3],[10,3],[9,16],[10,16],[3,5],[3,6],[3,13],[3,14],[16,5],[16,6],[16,13],[16,14]]
positions_walls_level3 = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],[0,10],[0,11],[0,12],[0,13],[0,14],[0,15],[0,16],[0,17],[0,18],[0,19],[19,0],[19,1],[19,2],[19,3],[19,4],[19,5],[19,6],[19,7],[19,8],[19,9],[19,10],[19,11],[19,12],[19,13],[19,14],[19,15],[19,16],[19,17],[19,18],[19,19],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0],[13,0],[14,0],[15,0],[16,0],[17,0],[18,0],[1,19],[2,19],[3,19],[4,19],[5,19],[6,19],[7,19],[8,19],[9,19],[10,19],[11,19],[12,19],[13,19],[14,19],[15,19],[16,19],[17,19],[18,19],[1,9],[1,10],[2,9],[2,10],[3,9],[3,10],[4,9],[4,10],[5,9],[5,10],[6,9],[6,10],[7,9],[7,10],[9,1],[10,1],[9,2],[10,2],[9,3],[10,3],[9,4],[10,4],[9,5],[10,5],[9,6],[10,6],[9,7],[10,7],[12,9],[12,10],[13,9],[13,10],[14,9],[14,10],[15,9],[15,10],[16,9],[16,10],[17,9],[17,10],[18,9],[18,10],[9,12],[10,12],[9,13],[10,13],[9,14],[10,14],[9,15],[10,15],[9,16],[10,16],[9,17],[10,17],[9,18],[10,18]]

spieler1Img = pygame.image.load('Spieler_t.png')

enemy1Img = pygame.image.load('e1.png')

fruitImg = pygame.image.load('Peach.png')

wallImg = pygame.image.load('iceblock.png')

groundImg = pygame.image.load('snow_ground.png')

def GUI_start(Status):
    FPS = 20
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption('Bad Ice Cream')

    font = pygame.font.SysFont('comicsansms', 72)
    font2 = pygame.font.SysFont('comicsansms', 36)
    text_1 = font.render('Level 1', True, black)
    text_2 = font.render('Level 2', True, black)
    text_3 = font.render('Level 3', True, black)

    text_Quit = font2.render('PRESS ESC TO QUIT', True, black)
    text_Restart = font2.render('PRESS R TO RESTART', True, black)
    text_rect_Quit = text_Quit.get_rect()
    text_rect_Restart = text_Restart.get_rect()
    text_rect_1 = text_1.get_rect()
    text_rect_2 = text_2.get_rect()
    text_rect_3 = text_3.get_rect()

    text_rect_1.center = (300, 150)
    text_rect_2.center = (300, 450)
    text_rect_3.center = (300, 750)
    text_rect_Restart.center = (200, 950)
    text_rect_Quit.center = (700, 950)

    while True:
        DISPLAYSURF.fill(white)
        DISPLAYSURF.fill(green, text_rect_Quit)
        DISPLAYSURF.fill(green, text_rect_Restart)
        DISPLAYSURF.fill(green, text_rect_1)
        DISPLAYSURF.fill(green, text_rect_2)
        DISPLAYSURF.fill(green, text_rect_3)
        DISPLAYSURF.blit(text_1, text_rect_1)
        DISPLAYSURF.blit(text_2, text_rect_2)
        DISPLAYSURF.blit(text_3, text_rect_3)
        DISPLAYSURF.blit(text_Quit, text_rect_Quit)
        DISPLAYSURF.blit(text_Restart, text_rect_Restart)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN :
                x, y = event.pos
                if x > 200 and x < 400 and y < 175  and y > 125:
                    pygame.quit()
                    return (1)
                elif x > 200 and x < 400 and y < 475  and y > 425:
                    pygame.quit()
                    return (2)
                elif x > 200 and x < 400 and y < 775  and y > 725:
                    pygame.quit()
                    return (3)
                elif x > 180 and x < 300 and y < 960  and y > 940:
                    pygame.quit()
                    return (10)
                elif x > 570 and x < 830 and y < 960  and y > 940:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def GUI_spiel(Level, positions_fruits):
    FPS = 60
    anzahlzellenx = 20
    anzahlzelleny = anzahlzellenx
    zellgroesse = 40
    breite = anzahlzellenx * zellgroesse
    hoehe = anzahlzelleny * zellgroesse

    my_feld = Board(anzahlzellenx)

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((breite, hoehe))
    pygame.display.set_caption('Bad Ice Cream')

# Geschwindigkeit Spieler:
    pygame.key.set_repeat(1 ,200)

# Text:
    font = pygame.font.SysFont('comicsansms', 72)
    font2 = pygame.font.SysFont('comicsansms', 36)
    text = font.render('GAME OVER!', True, black)
    text2 = font2.render('PRESS ESC TO QUIT', True, black)
    text3 = font.render('LEVEL COMPLETED!', True, black)
    text4 = font2.render('PRESS R TO RESTART', True, black)
    textRect = text.get_rect()
    textRect2 = text2.get_rect()
    textRect3 = text3.get_rect()
    textRect4 = text4.get_rect()
    textRect.center = (breite / 2, hoehe / 2 - 20)
    textRect2.center = (breite / 2, hoehe / 2 + 40)
    textRect3.center = (breite / 2, hoehe / 2 - 20)
    textRect4.center = (breite / 2, hoehe / 2 + 75)

# Variabeln:
    d = 0
    eaten_fruit = 0
    x = 0
    positions_walls = [0, 0]

    if Level == 1:
        positions_walls = positions_walls_Level1
    elif Level == 2:
        positions_walls = positions_walls_Level2
    elif Level == 3:
        positions_walls = positions_walls_level3

    while True:
        DISPLAYSURF.fill(white)

# Gehen Spieler:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_DOWN and check_walls(positions_walls, my_feld, 'down') != 0:
                         my_feld.spieler1[1] += 1

                elif event.key == K_UP and check_walls(positions_walls, my_feld, 'up') != 0:
                    my_feld.spieler1[1] -= 1

                elif event.key == K_LEFT and check_walls(positions_walls, my_feld, 'left') != 0:
                    my_feld.spieler1[0] -= 1

                elif event.key == K_RIGHT and check_walls(positions_walls, my_feld, 'right') != 0:
                    my_feld.spieler1[0] += 1


# Fruchte:

            check_fruits(positions_fruits, my_feld)

            eaten_fruit = 0
            for i in range (len(positions_fruits)):
                if positions_fruits[i][0] == 30 and positions_fruits[i][1] == 30:
                    eaten_fruit += 1

            if eaten_fruit == len(positions_fruits):
                DISPLAYSURF.fill(green)
                DISPLAYSURF.blit(text3, textRect3)
                DISPLAYSURF.blit(text2, textRect2)
                pygame.display.update()
                while (True):
                    for event in pygame.event.get():
                        if event.type == MOUSEBUTTONDOWN:
                                pygame.quit()
                                return (1)




# Raster:
        for x in range(0, breite, zellgroesse):
            pygame.draw.line(DISPLAYSURF, grey, (x, 0), (x,breite))

        for y in range(0, hoehe, zellgroesse):
            pygame.draw.line(DISPLAYSURF, grey, (0, y), (hoehe,y))

        draw_ground(groundImg, zellgroesse, DISPLAYSURF)

# Wande:
        draw_walls(positions_walls, wallImg, zellgroesse, DISPLAYSURF)

# Spieler und Fruchte zeichnen:
        draw_fruits(positions_fruits, fruitImg, zellgroesse, DISPLAYSURF)
        DISPLAYSURF.blit(spieler1Img, b_to_p(my_feld.spieler1[0], my_feld.spieler1[1], zellgroesse))
        DISPLAYSURF.blit(enemy1Img, b_to_p(my_feld.enemy1[0], my_feld.enemy1[1], zellgroesse))
        DISPLAYSURF.blit(enemy1Img, b_to_p(my_feld.enemy2[0], my_feld.enemy2[1], zellgroesse))
        DISPLAYSURF.blit(enemy1Img, b_to_p(my_feld.enemy3[0], my_feld.enemy3[1], zellgroesse))
        DISPLAYSURF.blit(enemy1Img, b_to_p(my_feld.enemy4[0], my_feld.enemy4[1], zellgroesse))

# Feindbewegung:
        d += 1
        # if d == 101:
        #     d = 0
        # if d % 20 == 0:

        if d == 15:
            d = 0

            move_enemy2(my_feld.enemy1, my_feld.spieler1, anzahlzellenx)
            move_enemy2(my_feld.enemy2, my_feld.spieler1, anzahlzellenx)
            move_enemy2(my_feld.enemy3, my_feld.spieler1, anzahlzellenx)
            move_enemy2(my_feld.enemy4, my_feld.spieler1, anzahlzellenx)
            if (my_feld.spieler1[0] == my_feld.enemy1[0] and my_feld.spieler1[1] == my_feld.enemy1[1])\
                    or (my_feld.spieler1[0] == my_feld.enemy2[0] and my_feld.spieler1[1] == my_feld.enemy2[1])\
                    or (my_feld.spieler1[0] == my_feld.enemy3[0] and my_feld.spieler1[1] == my_feld.enemy3[1])\
                    or (my_feld.spieler1[0] == my_feld.enemy4[0] and my_feld.spieler1[1] == my_feld.enemy4[1]):

                DISPLAYSURF.fill(red)
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
                                GUI_spiel(Level, positions_fruits)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def b_to_p(x, y, breite):
    return x * breite, y * breite

def p_to_b(x, y, breite):
    return x//breite, y//breite

# Boden
def draw_ground(picture, zellgroesse, DISPLAYSURF):
    DISPLAYSURF.blit(picture, b_to_p(0, 0, zellgroesse))

# Wande:
def draw_walls(positions, picture, zellgroesse, DISPLAYSURF):
    for i in range (0,(len(positions))):
        DISPLAYSURF.blit(picture, b_to_p(positions[i][0], positions[i][1], zellgroesse))

def check_walls(positions, my_feld, direction):
        if direction == 'right':
            for i in range (len(positions)):
                if (my_feld.spieler1[0]+1) == positions[i][0] and my_feld.spieler1[1] == positions[i][1]:
                    return(0)
        if direction == 'left':
            for i in range (len(positions)):
                if (my_feld.spieler1[0]-1) == positions[i][0] and my_feld.spieler1[1] == positions[i][1]:
                    return(0)
        if direction == 'up':
            for i in range (len(positions)):
                if (my_feld.spieler1[0]) == positions[i][0] and (my_feld.spieler1[1]-1) == positions[i][1]:
                    return(0)
        if direction == 'down':
            for i in range (len(positions)):
                if (my_feld.spieler1[0]) == positions[i][0] and (my_feld.spieler1[1]+1) == positions[i][1]:
                    return(0)

#Fruchte:
def check_fruits(positions, my_feld):
    for i in range (len(positions)):
        e = 0
        if my_feld.spieler1[0] == positions[i][0] and my_feld.spieler1[1] == positions[i][1]:
            positions[i][0] = 30
            positions[i][1] = 30
            e = 1

def draw_fruits(positions, picture, zellgroesse, DISPLAYSURF):
    for i in range (0,(len(positions))):
        DISPLAYSURF.blit(picture, b_to_p(positions[i][0], positions[i][1], zellgroesse))

#Feindbewegung
def move_enemy2(enemy, spieler, anzahlzellenx):

    x = random.randint(0,1)
    if x == 0:
        if spieler[0] > enemy[0]:
            enemy[0] += 1
        elif enemy[0] > spieler[0]:
            enemy[0] -= 1
        else:
            if spieler[1] > enemy[1]:
                enemy[1] += 1
            elif enemy[1] > spieler[1]:
                enemy[1] -= 1
            else:
                pass
    elif x == 1:
        if spieler[1] > enemy[1]:
            enemy[1] += 1
        elif enemy[1] > spieler[1]:
            enemy[1] -= 1
        else:
            if spieler[0] > enemy[0]:
                enemy[0] += 1
            elif enemy[0] > spieler[0]:
                enemy[0] -= 1
            else:
                pass

if __name__ == '__main__':
        v = True
        while (v == 1):
            positions_fruits = [[17, 5], [2, 5], [17, 14], [2, 14], [7, 4], [12, 4], [7, 15], [12, 15]]
            Level = GUI_start(1)
            v = GUI_spiel(Level, positions_fruits)



# Blocke fuer Rahmen: [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],[0,10],[0,11],[0,12],[0,13],[0,14],[0,15],[0,16],[0,17],[0,18],[0,19],[19,0],[19,1],[19,2],[19,3],[19,4],[19,5],[19,6],[19,7],[19,8],[19,9],[19,10],[19,11],[19,12],[19,13],[19,14],[19,15],[19,16],[19,17],[19,18],[19,19],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0],[13,0],[14,0],[15,0],[16,0],[17,0],[18,0],[1,19],[2,19],[3,19],[4,19],[5,19],[6,19],[7,19],[8,19],[9,19],[10,19],[11,19],[12,19],[13,19],[14,19],[15,19],[16,19],[17,19],[18,19]]