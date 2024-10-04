from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scorekeeper import Scoreboard

screen=Screen()
screen.setup(1000,700)
screen.bgcolor("black")
screen.title("PING PONG")
screen.tracer(0)

r_paddle=Paddle((470,0))
l_paddle=Paddle((-480,0))
ball=Ball()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

game_is_on=True

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    #collision with the wall...................................
    if ball.ycor()>330 or ball.ycor()<-330:
        ball.bounce_y()

    #collision with the side wall.............................................................
    if ball.xcor()>440 and ball.distance(r_paddle)<50:
        ball.bounce_x()
        #ball.mspeed*=0.9

    if ball.xcor()<-445 and ball.distance(l_paddle)<50:
        ball.bounce_x()
        #ball.mspeed*=0.9


    #if missed the right paddle...................................
    if ball.xcor()>480:
        ball.refresh()
        scoreboard.lpoint()

    #if missed the left paddle..................................
    if ball.xcor()<-480:
        ball.refresh()
        scoreboard.rpoint()


screen.exitonclick()
