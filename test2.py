import pygame, sys
from pygame.locals import *

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

class My_app():
    def __init__(self):

        pygame.init()

        # set up the window
        self.D_WIDHT = 600
        self.D_HEIGHT = 300

        self.DISPLAYSURF = pygame.display.set_mode((self.D_WIDHT, self.D_HEIGHT), 0, 32)
        pygame.display.set_caption('Drawing')


        self.die_koordinaten = {'x': 300, 'y': 200}
        self.die_radius = 5

        FPS = 50
        FPSCLOCK = pygame.time.Clock()

        while True:
            self.DISPLAYSURF.fill(WHITE)
            for event in pygame.event.get():
                self.check_exit_event(event)
                self.check_mouse_event(event)

            self.the_background()

            pygame.draw.circle(self.DISPLAYSURF, BLACK, (self.die_koordinaten['x'], self.die_koordinaten['y']), self.die_radius, 0)

            #print(pygame.mouse.get_pos())
            pygame.display.update()
            FPSCLOCK.tick(FPS)


    def check_exit_event(self, event):
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    def check_mouse_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            #print(event.pos)
            if event.button == 1:
                neu_koordinaten = pygame.mouse.get_pos()
                self.die_koordinaten['x'] = neu_koordinaten[0]
                self.die_koordinaten['y'] = neu_koordinaten[1]
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                self.die_radius += 1
            elif event.button == 5:
                self.die_radius = max(1, self.die_radius -1)


    def the_background(self):
        # draw on the surface object
        self.DISPLAYSURF.fill(WHITE)
        pygame.draw.polygon(self.DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
        pygame.draw.line(self.DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
        pygame.draw.line(self.DISPLAYSURF, BLUE, (120, 60), (60, 120))
        pygame.draw.line(self.DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
        pygame.draw.circle(self.DISPLAYSURF, BLUE, (300, 50), 20, 0)
        pygame.draw.ellipse(self.DISPLAYSURF, RED, (300, 200, 40, 80), 1)
        the_rect = pygame.Rect(300, 200, 40, 80)
        pygame.draw.rect(self.DISPLAYSURF, BLACK, the_rect, 1)
        pygame.draw.rect(self.DISPLAYSURF, RED, (200, 150, 100, 50))

# run the game loop
if __name__ == "__main__":
    ausfuehren = My_app()