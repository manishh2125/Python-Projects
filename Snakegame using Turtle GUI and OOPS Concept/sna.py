from turtle import Turtle
POSITIONS=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]


    def create_snake(self):
        for pose in POSITIONS:
            self.add_segments(pose)

    def add_segments(self,pose):
        tom = Turtle("square")
        tom.color("white")
        tom.penup()
        tom.goto(pose)
        self.segments.append(tom)

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(20)


    def up(self):
        if self.head.heading()!=DOWN:
           self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
           self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!=RIGHT:
           self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!=LEFT:
           self.head.setheading(RIGHT)
