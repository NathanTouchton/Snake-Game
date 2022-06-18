from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scorboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.down, key="s")
screen.onkey(fun=snake.left, key="a")
screen.onkey(fun=snake.right, key="d")

SCORE = 0

GAME_IS_ON = True
while GAME_IS_ON:
    scorboard.update_score(SCORE)
    screen.update()
    sleep(.1)
    snake.move()
    if snake.head.distance(food) < 16:
        food.refresh()
        SCORE += 1

screen.exitonclick()
