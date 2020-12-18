#! /bin/python3

import time
from turtle import Screen
import turtle
from player import Player
from car_manager import CarManager, Car
from scoreboard import Scoreboard
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()


screen.listen()

screen.onkey(player.turtle_up, "Up")
screen.onkey(player.turtle_down, "Down")
screen.onkey(player.turtle_left,"Left")
screen.onkey(player.turtle_right, "Right")

game_is_on = True
player_win = False
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move_all()
    if randint(1,100) < 5:
        cars.create_car()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    if player.ycor() == 290:
        player_win = True
        game_is_on = False