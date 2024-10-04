from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(0,275)
        self.write(f"level: {self.level}","False","center",("Arial",11,"normal"))

    def update_score(self):
        self.level+=1
        self.clear()
        self.goto(0,275)
        self.write(f"level: {self.level}","False","center",("Arial",11,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER","False","center",("Aria",25,"normal"))


