from turtle import Turtle

START_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        super().__init__()
        self.snake_squares = []
        self.create_snake()
        self.head = self.snake_squares[0]

    def create_snake(self):
        for position in START_COORDINATES:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snake_squares.append(snake)

    def extend(self):
        self.add_segment(self.snake_squares[-1].position())

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
