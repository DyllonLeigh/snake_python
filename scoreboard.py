from turtle import Turtle

ALIGNMENT = "center"
FONT = ("arial", 16, "bold")
FONT2 = ("courier", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = -1
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,15)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=FONT2)
        self.goto(0,-15)
        self.color("white")
        self.write(f"Final Score: {self.score}", align=ALIGNMENT, font=FONT)