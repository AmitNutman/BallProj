import multiprocessing

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


    def ball_added(self, num_ball):
        """

        :param num_ball:
        :return:
        """
        print(f"ball number {num_ball} add")
        print("num balls on screen: " + str(len(self.balls)))



    def ball_deleted(self, num_ball):
        """

        :param num_ball:
        :return:
        """
        print(f"ball number {num_ball} deleted")
        print("num balls on screen: " + str(len(self.balls)))