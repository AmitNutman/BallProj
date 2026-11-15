#https://github.com/AmitNutman/BallProj
#עמית נוטמן ואורי פרסמן

import pygame



class Gui():

    def __init__(self, width, height, ball_q, printing_q, collision_q, gui_q):
        """
        constructor
        :param width: the screens width
        :param height: the screens height
        :param ball_q: the q for the ball process
        :param printing_q: the q fot the printing process
        :param collision_q: the q for the collision process
        :param gui_q: the q for the drawing process
        """
        self.width = width  # screen width
        self.height = height  # screen height
        self.screen = pygame.display.set_mode((self.width, self.height)) #the screen
        self.ball_q = ball_q
        self.printing_q = printing_q
        self.collision_q = collision_q
        self.gui_q = gui_q
        self.balls = {}


    def draw_ball(self, ball_processes):
        """
        draws all balls dict on screen
        :param ball_processes: all processes of all balls
        :return: None
        """
        self.printing_q.put("GUI process started")
        running = True
        while running:
            while not self.gui_q.empty():
                self.balls = self.gui_q.get()

            self.screen.fill((0, 0, 0))
            #value = (color, pos, radius)
            for ball in self.balls.values():
                pygame.draw.circle(self.screen, ball[0], ball[1], ball[2])

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            #checks if all ball processes finished
            not_one_process_working = True
            for p in ball_processes:
                if p.is_alive():
                    not_one_process_working = False
            if(not_one_process_working):
                running = False

        self.printing_q.put("GUI process ended")
        pygame.quit()