#https://github.com/AmitNutman/BallProj
#עמית נוטמן ואורי פרסמן


import random
import time
import multiprocessing
from Gui3 import Gui
from Printing3 import Printing
from Collision3 import Collision
import sys


class BallClass():
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
        self.ball_q = ball_q
        self.printing_q = printing_q
        self.collision_q = collision_q
        self.gui_q = gui_q
        self.width = width
        self.height = height

    def main_loop(self, num_ball):
        """
        random another ball and updates collision
        :param num_ball: the number of the ball created
        :return: None
        """
        self.printing_q.put(f"Ball process {num_ball} started")
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        num_of_shows = random.randint(1, 10)

        for i in range(num_of_shows):
            ball_x = random.randint(1 + 25, self.width - 25)
            ball_y = random.randint(1 + 25, self.height - 25)
            pos = (ball_x, ball_y)

            self.collision_q.put(("ball_added", (num_ball, color, pos)))
            #show on screen for 2 seconds
            time.sleep(2)

            self.collision_q.put(("ball_deleted", num_ball))
            #delete from screen for 0.5 seconds
            time.sleep(0.5)

        self.printing_q.put(f"Ball process {num_ball} ended")

if __name__ == "__main__":

    width, height = 700, 500

    ball_q = multiprocessing.Queue()
    printing_q = multiprocessing.Queue()
    collision_q = multiprocessing.Queue()
    gui_q = multiprocessing.Queue()

   #printing process so it will ask for num balls
    printer = Printing(ball_q, printing_q, collision_q, gui_q)
    printer_process = multiprocessing.Process(target=printer.main_loop, args=(sys.stdin.fileno(),))
    printer_process.start()

    num_balls = ball_q.get()


    collision = Collision(width, height, ball_q, printing_q, collision_q, gui_q)
    collision_process = multiprocessing.Process(target=collision.main_loop)
    collision_process.start()

    #create process for every ball
    ball_processes = []
    for i in range(1, num_balls + 1):
        ball = BallClass(width, height, ball_q, printing_q, collision_q, gui_q)
        p = multiprocessing.Process(target=ball.main_loop, args=(i,))
        ball_processes.append(p)
        p.start()

    #after there is process for every ball - process to draw them
    gui = Gui(width, height, ball_q, printing_q, collision_q, gui_q)
    gui.draw_ball(ball_processes)



    collision_q.put("STOP")
    collision_process.join()

    printing_q.put("STOP")
    printer_process.join()


