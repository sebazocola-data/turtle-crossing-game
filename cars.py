from turtle import Turtle
import random


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(random.randint(300, 10000), random.randint(-200, 200))

    def move_the_car(self):
        self.backward(10)




