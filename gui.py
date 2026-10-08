import pygame
import sys
import threading
import random
import time


class GameGUI():

    def __init__(self, width, height):
        """
        constructor
        :param width: the screens width
        :param height: the screens height
        """
        self.width = width  # screen width
        self.height = height  # screen height
        self.screen = pygame.display.set_mode((self.width, self.height)) #the screen
        self.balls = {} #dict of all balls to be drawn on screen


    def add_ball(self, num_ball):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        num_of_shows = random.randint(1, 10)
        for i in range(num_of_shows):
            ball_x = random.randint(1 + 50, 700 - 50)
            ball_y = random.randint(1 + 50, 500 - 50)
            pos = (ball_x, ball_y)
            self.balls[num_ball] = (color, pos, 50)

            print(f"ball number {num_ball} add")
            print("num balls on screen: " + str(len(self.balls)))

            time.sleep(2)

            #delete the ball so it will disapear
            if num_ball in self.balls:
                del self.balls[num_ball]

            print(f"ball number {num_ball} deleted")
            print("num balls on screen: " + str(len(self.balls)))

            time.sleep(0.5)



    def draw_circle(self):
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



if __name__ == "__main__":


    num_balls = input("enter num balls: ")

    while (not num_balls.isdigit() or int(num_balls) <= 0):
        print("not legall input, try again")
        num_balls = input("enter num balls: ")

    gui = GameGUI(700, 500)

    for i in range(int(num_balls)):
        threading.Thread(target=gui.add_ball, args=(i,)).start()
        time.sleep(0.5)

    gui.draw_circle()











