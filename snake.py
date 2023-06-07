from turtle import Turtle
move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = Turtle('square')
        new_turtle.color('white')
        new_turtle.penup()
        new_turtle.goto(position)
        self.turtles.append(new_turtle)

    def extend(self):
        self.add_segment(self.turtles[-1].position())

    def move(self):
        # this links all the snake segments together to move synchronously.
        for seg in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[seg - 1].xcor()
            new_y = self.turtles[seg - 1].ycor()
            self.turtles[seg].goto(new_x, new_y)
        self.turtles[0].forward(move_distance)

    def reset_snake(self):
        for seg in self.turtles:
            seg.goto(1000, 1000)

        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
