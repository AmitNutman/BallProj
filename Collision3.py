#https://github.com/AmitNutman/BallProj
#עמית נוטמן ואורי פרסמן


import math
import random


class Collision():

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
        self.balls = {}  # dict of all balls to be drawn on screen
        self.ball_q = ball_q
        self.printing_q = printing_q
        self.collision_q = collision_q
        self.gui_q = gui_q
        self.width = width  # screen width
        self.height = height  # screen height



    def ball_added(self, num_ball, color, pos):
        """
        a new ball was added - checks if collide - if collide random new place
        :param num_ball: the number of the ball added
        :param color: the color of the ball added
        :param pos: the position of the ball added
        :return: None
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
        a ball was deleted - removes from dict
        :param num_ball: the number of the ball that was deleted
        :return: None
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
        """
        see what it needs to do based on the q
        :return: None
        """
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






