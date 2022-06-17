from turtle import Turtle, Screen
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

food = Food()

display = Turtle()
display.hideturtle()
display.penup()
display.color("white")
display.speed(0)
display.goto(0, 270)

display.write("Test", align="center", font=("Arial", 10))


screen.exitonclick()
