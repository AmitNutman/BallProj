#שני צוקרמן ועמית נוטמן
#https://github.com/AmitNutman/BallProj

import pygame
import sys
import threading
import random
import time
import requests


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
        self.num_collisions = 0


    def add_ball(self, num_ball):
        """
        adds new ball to list
        :param num_ball: the number of the ball
        :return: None
        """
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        num_of_shows = random.randint(1, 10)
        for i in range(num_of_shows):
            ball_x = random.randint(1 + 50, 700 - 50)
            ball_y = random.randint(1 + 50, 500 - 50)
            pos = (ball_x, ball_y)

            # create a list for all balls location accept from the currnt ball
            positions = []
            for ballColor, ballPos, ballRadius in self.balls.values():
                positions.append(ballPos)


            self.balls[num_ball] = (color, pos, 50)


            prompt = (
                f"Current Game State:\n"
                f"- Ball position (X, Y): {pos}\n"
                f"- other balls positions in a list (X, Y): {positions}\n"
                f"- radius : {50}\n"
                f"return True if collide else return False"
            )


            #start ai only if there are other balls
            if positions:
                threading.Thread(target=self.check_ai_result, args=(prompt,), daemon = True).start()

            print(f"ball number {num_ball} add")
            print("num balls on screen: " + str(len(self.balls)))

            time.sleep(5)

            #delete the ball so it will disapear
            if num_ball in self.balls:
                del self.balls[num_ball]

            print(f"ball number {num_ball} deleted")
            print("num balls on screen: " + str(len(self.balls)))

            time.sleep(2.0)

    def check_ai_result(self, prompt):
        """
        checks if ai returned that the balls collide or not
        :param prompt: the prompt to send to ai
        :return: None
        """
        result = self.query_local_ai(prompt).strip().lower()
        if result == "true":
            self.num_collisions += 1


    def draw_circle(self):
        """
        draws the ball on screen
        :return: None
        """
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

            for t in ball_threads:
                if not t.is_alive():
                    ball_threads.remove(t)

            if ball_threads == []:
                print("collision count = ", self.num_collisions)
                pygame.quit()
                sys.exit()



    def query_local_ai(self, prompt):
        """
        ai agent checks if balls collided based on the instructions
        :param prompt: the prompt to ai
        :return: str - true / false/ do nothing
        """

        OLLAMA_API_URL = "http://localhost:11434/api/chat"
        OLLAMA_MODEL = "gemma2"

        system_instructions = "You are an AI agent that checks if ball collide others ballas  - you will get ball position is (x,y) other balls position in list [(x1,y1), (x2,y2)...] all balls's radius is 50, please check if first ball collide with one or more of the others balls in the list, answer only in one words: true if collide else false"

        payload = {"model": OLLAMA_MODEL, "messages": [{"role": "system", "content": system_instructions}, {"role": "system", "content": prompt}], "stream": False}

        try:
            print("sending the game state to the local AI to analyze")
            response = requests.post(OLLAMA_API_URL, json=payload, timeout=30)

            if response.status_code == 200:
                result = response.json()
                action = result.get('message', {}).get('content', '').strip()
                return action
            else:
                print(f"error:{response.status_code}")
                return "DO_NOTHING"
        except requests.exceptions.RequestException as e:
            print(f"error:{e}")
            return "DO_NOTHING"

if __name__ == "__main__":



    num_balls = input("enter num balls: ")

    while (not num_balls.isdigit() or int(num_balls) <= 0):
        print("not legall input, try again")
        num_balls = input("enter num balls: ")

    gui = GameGUI(700, 500)

    ball_threads = []
    for i in range(int(num_balls)):
        t = threading.Thread(target=gui.add_ball, args=(i,))
        ball_threads.append(t)
        t.start()
        time.sleep(5)

    gui.draw_circle()











