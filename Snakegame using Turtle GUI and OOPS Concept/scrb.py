from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.score=0
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.write(f"Score {self.score}","False","center",("Arial",21,"normal"))

    def inc_score(self):

        self.score+=1
        self.clear()
        self.goto(0,265)
        self.write(f"Score {self.score}","False","center",("Arial",21,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER","False","center",("Arial",25,"normal"))

