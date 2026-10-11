import pygame
import sys
import multiprocessing



class Gui():

    def __init__(self, width, height, ball_q, printing_q, collision_q, gui_q):
        """
        constructor
        :param width: the screens width
        :param height: the screens height
        """
        self.width = width  # screen width
        self.height = height  # screen height
        self.screen = pygame.display.set_mode((self.width, self.height)) #the screen
        self.ball_q = ball_q
        self.printing_q = printing_q
        self.collision_q = collision_q
        self.gui_q = gui_q




    def draw_ball(self):
        while True:

            #clean the screen before all balls in the list will be drawn again
            self.screen.fill((0,0,0))

            for ball in self.balls.values():
                #color, pos, radius
                pygame.draw.circle(self.screen, ball[0], ball[1], ball[2])

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # closes py_game window
                    pygame.quit()
                    # closes the program
                    sys.exit()

            #how many active threads are in the system - main thread is always active
            if threading.active_count() < 2:
                # closes py_game window
                pygame.quit()
                # closes the program
                sys.exit()