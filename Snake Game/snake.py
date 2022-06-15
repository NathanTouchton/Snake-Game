from turtle import Turtle

START_X_COORDINATES = [0, -20, -40]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_squares = []
        self.create_snake()
        self.head = self.snake_squares[0]

    def create_snake(self):
        for new_square in range(3):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(x=START_X_COORDINATES[new_square], y=0)
            self.snake_squares.append(snake)

    def move(self):
        for square in range(len(self.snake_squares) - 1, 0, -1):
            new_x = self.snake_squares[square - 1].xcor()
            new_y = self.snake_squares[square - 1].ycor()
            self.snake_squares[square].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
            