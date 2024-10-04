from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0

    def update_score(self):
        self.clear()
        self.goto(-300, 300)
        self.write(self.l_score, "False", "center", ("Arial", 21, "normal"))
        self.goto(300, 300)
        self.write(self.r_score, "False", "center", ("Arial", 21, "normal"))

    def lpoint(self):
        self.l_score+=1
        self.update_score()

    def rpoint(self):
        self.r_score+=1
        self.update_score()