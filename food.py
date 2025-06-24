from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("darkgreen")
        self.penup()
        self.shapesize(0.75, 0.75)
        self.refresh()

    def refresh(self):
        x_pos = float(randint(-13, 13) * 20)
        y_pos = float(randint(-13, 13) * 20)
        self.goto(x_pos, y_pos)