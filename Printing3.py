import multiprocessing
import sys
import os

class Printing():
    def __init__(self, width, height, ball_q, printing_q, collision_q, gui_q):
        """

        """
        self.ball_q = ball_q
        self.printing_q = printing_q
        self.collision_q = collision_q
        self.gui_q = gui_q




    def input_num_of_balls(self):
        """

        :return:
        """
        num_balls = input("enter num balls: ")

        while (not num_balls.isdigit() or int(num_balls) <= 0):
            print("not legall input, try again")
            num_balls = input("enter num balls: ")
        return int(num_balls)


    def ball_added(self, num_ball, count):
        """

        :param num_ball:
        :return:
        """
        print(f"ball number {num_ball} add")
        print("num balls on screen: " + str(count))



    def ball_deleted(self, num_ball, count):
        """

        :param num_ball:
        :return:
        """
        print(f"ball number {num_ball} deleted")
        print("num balls on screen: " + str(count))

    def main_loop(self, stdin_fd):
        print("Printing process started")

        #open key board so we can enter input
        sys.stdin = os.fdopen(stdin_fd)

        print("Printing process started")
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