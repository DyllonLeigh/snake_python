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
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Your score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt",mode="w") as file:
                file.write(str(self.high_score))
        self.score = -1
        self.update_score()

    # def game_over(self):
    #     self.clear()
    #     self.goto(0,15)
    #     self.color("red")
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT2)
    #     self.goto(0,-15)
    #     self.color("white")
    #     self.write(f"Final Score: {self.score}", align=ALIGNMENT, font=FONT)