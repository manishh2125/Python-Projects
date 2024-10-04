from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple","brown","black"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():

    def __init__(self):
        self.cars=[]
        self.carspeed=STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance= random.randint(1,6)
        if random_chance==1:
            new_car=Turtle("square")
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y=random.randint(-250,250)
            new_car.goto(300,random_y)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:

            car.backward(self.carspeed)

    def level_up(self):
        self.carspeed+=MOVE_INCREMENT





