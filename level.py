from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 20, "normal")


class LevelUp(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-230, 230)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game over", align=ALIGNMENT, font=FONT)