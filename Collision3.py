import math
import multiprocessing


class Collision():

    def __init__(self, width, height, ball_q, printing_q, collision_q, gui_q):
        """

        """
        self.balls = {}  # dict of all balls to be drawn on screen
        self.ball_q = ball_q
        self.printing_q = printing_q
        self.collision_q = collision_q
        self.gui_q = gui_q



    def ball_added(self, num_ball, color, pos):
        """

        :param num_ball:
        :param color:
        :param pos:
        :return:
        """
        while not self.check_if_collision(pos):
            pass
            #pos = call the roll_new_pos in ballclass
        self.balls[num_ball] = (color, pos, 25)


    def ball_deleted(self, num_ball):
        """

        :param num_ball:
        :return:
        """
        # delete the ball so it will disapear
        if num_ball in self.balls:
            del self.balls[num_ball]


    def check_if_collision(self, pos):
       """
       checks if the ball that just added is not collision
       :param pos: the pos of the ball just added
       :return: true if collision, false if not collision
       """
       collision = False
       for ball in self.balls:
           if not collision:
                x = ball[1][0]
                y = ball[1][1]

                # checks if the distance is below 25
                distance = math.hypot((x - pos[0]), (y - pos[1]))

                #if distance <= radius
                if distance <= 25:
                    collision = True
       return collision






