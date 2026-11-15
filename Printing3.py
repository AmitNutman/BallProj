#https://github.com/AmitNutman/BallProj
#עמית נוטמן ואורי פרסמן

import sys
import os

class Printing():
    def __init__(self, ball_q, printing_q, collision_q, gui_q):
        """
        constructor
        :param ball_q: the q for the ball process
        :param printing_q: the q fot the printing process
        :param collision_q: the q for the collision process
        :param gui_q: the q for the drawing process
        """
        self.ball_q = ball_q
        self.printing_q = printing_q
        self.collision_q = collision_q
        self.gui_q = gui_q




    def input_num_of_balls(self):
        """
        asks user to enter num balls
        :return: num balls
        """
        num_balls = input("enter num balls: ")

        while (not num_balls.isdigit() or int(num_balls) <= 0):
            print("not legall input, try again")
            num_balls = input("enter num balls: ")
        return int(num_balls)


    def ball_added(self, num_ball, count):
        """
        prints a new ball was added
        :param num_ball: the number of the ball added
        :param count: the number of all balls on screen
        :return: None
        """
        print(f"ball number {num_ball} add")
        print("num balls on screen: " + str(count))



    def ball_deleted(self, num_ball, count):
        """
        prints a ball was deleted
        :param num_ball: the number of the ball deleted
        :param count: the number of all balls on screen
        :return: None
        """
        print(f"ball number {num_ball} deleted")
        print("num balls on screen: " + str(count))

    def main_loop(self, stdin_fd):
        """
        does what it needs to do based on q
        :param stdin_fd: so the user can enter input
        :return: None
        """
        print("Printing process started")

        #open key board so we can enter input
        sys.stdin = os.fdopen(stdin_fd)

        num_balls = self.input_num_of_balls()
        self.ball_q.put(num_balls)

        while True:
            data = self.printing_q.get()
            #if finished all balls
            if data == "STOP":
                print("Printing process ended")
                break
            elif isinstance(data, tuple):
                opcode = data[0]
                if opcode == "ball_added":
                    # data = ("ball_added", num_ball, count)
                    self.ball_added(data[1], data[2])
                elif opcode == "ball_deleted":
                    # data = ("ball_deleted", num_ball, count)
                    self.ball_deleted(data[1], data[2])
                elif opcode == "input_num_balls":
                    #data = ("input_num_balls")
                    self.input_num_of_balls()
            else:
                print(data)