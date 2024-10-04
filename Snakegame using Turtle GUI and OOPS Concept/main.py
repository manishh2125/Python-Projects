from turtle import Screen
import time
from sna import Snake
from foo import Food
from scrb import Scoreboard

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("MySnakeGame")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    for seg in snake.segments:
         if snake.head.distance(food)<15:
             food.refresh()
             snake.extend()
             scoreboard.inc_score()

    if snake.head.xcor() >290 or snake.head.xcor() <-290 or snake.head.ycor() >290 or snake.head.ycor() <-290:
        game_is_on=False
        scoreboard.game_over()

    for segm in snake.segments:
        if segm==snake.head:
            pass
        elif snake.head.distance(segm)<10:
            game_is_on=False
            scoreboard.game_over()

























screen.exitonclick()