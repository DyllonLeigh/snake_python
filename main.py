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

screen.listen()
screen.onkeypress(snake.move_north,"w")
screen.onkeypress(snake.move_south,"s")
screen.onkeypress(snake.move_west,"a")
screen.onkeypress(snake.move_east,"d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect Collision with Food:
    if snake.head.distance(food) < 1:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    # Detect Collision with Boundary:
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280
            or snake.head.ycor() > 280 or snake.head.ycor() < -280):
        scoreboard.game_over()
        game_is_on = False

    # Detect Collision with Body:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()