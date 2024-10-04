import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(player.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    for kar in car_manager.cars:
         if kar.distance(player)<20:
            game_is_on=False
            scoreboard.game_over()

    #succesful crossing..............................................
    if player.is_at_finishline():
        player.goto_start()
        car_manager.level_up()
        scoreboard.update_score()






screen.exitonclick()