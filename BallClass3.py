import random
import time
from gui import GameGUI
import threading
import multiprocessing



class BallClass():
    def __init__(self, ball_q, printing_q, collision_q, gui_q):
        """
        constructor
        """
        self.ball_q = ball_q
        self.printing_q = printing_q
        self.collision_q = collision_q
        self.gui_q = gui_q




    def create_ball(self, num_ball):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        num_of_shows = random.randint(1, 10)
        for i in range(num_of_shows):
            ball_x = random.randint(1 + 25, 700 - 25)
            ball_y = random.randint(1 + 25, 500 - 25)
            pos = (ball_x, ball_y)

            self.collision_q.put(("ball_added", (num_ball, color, pos)))
            # self.balls[num_ball] = (color, pos, 25)


            # print(f"ball number {num_ball} add")
            # print("num balls on screen: " + str(len(self.balls)))

            time.sleep(2)

            """
            #delete the ball so it will disapear
            if num_ball in self.balls:
                del self.balls[num_ball]
            """

            """
            print(f"ball number {num_ball} deleted")
            print("num balls on screen: " + str(len(self.balls)))
            """

            time.sleep(0.5)


    def roll_new_pos(self):
        """

        :return:
        """
        ball_x = random.randint(1 + 25, 700 - 25)
        ball_y = random.randint(1 + 25, 500 - 25)
        pos = (ball_x, ball_y)
        return pos



    def main_loop(self):
        while True:
            if not self.ball_q.isEmpty():
                data = self.ball_q.get()
                if not data is None:
                    if data[0] == "roll_new_pos":
                        self.roll_new_pos()
                    elif data[0] == "create_ball":
                        self.create_ball(data[1][0])


if __name__ == "__main__":

    ball_q = multiprocessing.Queue
    printing_q = multiprocessing.Queue
    collision_q = multiprocessing.Queue
    gui_q = multiprocessing.Queue

    ball_class = BallClass(ball_q, printing_q, collision_q, gui_q)


    printer_process = multiprocessing.Process(target=main_loop, args=(print_queue,))
    printer_process.start()


