from snake import Snake
from food import Food
from turtle import Screen
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

game_is_on = True

def end_game():
    global game_is_on
    game_is_on = False

screen.listen()
screen.onkeypress(snake.move_north,"w")
screen.onkeypress(snake.move_south,"s")
screen.onkeypress(snake.move_west,"a")
screen.onkeypress(snake.move_east,"d")
screen.onkeypress(end_game,"x")

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280:
        snake.head.goto((snake.head.xcor() * -1), snake.head.ycor())
    if snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.head.goto((snake.head.xcor(), (snake.head.ycor() * -1)))

    # Detect Collision with Food:
    if snake.head.distance(food) < 1:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    # Detect Collision with Body:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset_snake()
            break