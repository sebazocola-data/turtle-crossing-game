from turtle import Screen
from player import Player
from cars import Cars
from level import LevelUp
import time

# screen object

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("The Turtle Crossing Capstone Game")
screen.tracer(0)
screen.colormode(255)

# La tortuga que camina por la calle
player = Player()

# Los autos que pasan a distinta velocidad
list_of_cars = []
for number in range(0, 500):
    car_number = Cars()
    list_of_cars.append(car_number)

# Leyenda de level up
level = LevelUp()

# Tecla para mover la tortuga por la calle
screen.listen()
screen.onkey(player.move, "Up")

# El comienzo del juego
the_game = True
# Variable para aumentar la velocidad

time_speed = 0.1
while the_game:
    screen.setup()
    time.sleep(time_speed)


    # Lo que hace que los autos se muevan
    for move in list_of_cars:
        move.move_the_car()



    # Lo que hace que la tortuga vuelva a su posición y se suba de nivel
    if player.ycor() > 260:
        player.level_up()
        level.increase_level()
        time_speed *= 0.8

    for crush in list_of_cars:
        if player.distance(crush) < 20:
            level.game_over()
            the_game = False

screen.exitonclick()


# tengo que mejorar la distancia en el choque

#tengo que ver como hacer que los autos no vengan tán ensimados

