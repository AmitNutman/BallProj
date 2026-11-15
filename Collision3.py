import math
import multiprocessing
import random


class Collision():

    def __init__(self, width, height, ball_q, printing_q, collision_q, gui_q):
        """

        """
        self.balls = {}  # dict of all balls to be drawn on screen
        self.ball_q = ball_q
        self.printing_q = printing_q
        self.collision_q = collision_q
        self.gui_q = gui_q
        self.width = width  # screen width
        self.height = height  # screen height



    def ball_added(self, num_ball, color, pos):
        """

        :param num_ball:
        :param color:
        :param pos:
        :return:
        """
        while self.check_if_collision(pos):
            #if collision random another place
            ball_x = random.randint(1 + 25, self.width - 25)
            ball_y = random.randint(1 + 25, self.height - 25)
            pos = (ball_x, ball_y)
        self.balls[num_ball] = (color, pos, 25)
        self.gui_q.put(self.balls)
        self.printing_q.put(("ball_added", num_ball, len(self.balls)))


    def ball_deleted(self, num_ball):
        """

        :param num_ball:
        :return:
        """
        # delete the ball so it will disapear
        if num_ball in self.balls:
            del self.balls[num_ball]
            self.gui_q.put(self.balls)
            self.printing_q.put(("ball_deleted", num_ball, len(self.balls)))


    def check_if_collision(self, pos):
       """
       checks if the ball that just added is not collision
       :param pos: the pos of the ball just added
       :return: true if collision, false if not collision
       """
       collision = False
       for ball in self.balls.values():
           if not collision:
                x = ball[1][0]
                y = ball[1][1]

                # checks if the distance is below 50 - 2 radius
                distance = math.hypot((x - pos[0]), (y - pos[1]))

                #if distance <= 2 radius
                if distance <= 50:
                    collision = True
       return collision

    def main_loop(self):
        self.printing_q.put("Collision process started")
        while True:
            data = self.collision_q.get()
            if data == "STOP":
                self.printing_q.put("Collision process ended")
                self.gui_q.put("STOP")
                break
            opcode, args = data
            if opcode == "ball_added":
                num_ball, color, pos = args
                self.ball_added(num_ball, color, pos)
            elif opcode == "ball_deleted":
                num_ball = args
                self.ball_deleted(num_ball)






