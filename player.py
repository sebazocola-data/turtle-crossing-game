from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(0, -250)
        self.setheading(90)


    def move(self):
        self.forward(20)

    def level_up(self):
        self.goto(0, -250)
