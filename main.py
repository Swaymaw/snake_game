from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snakes')
screen.tracer(0)
top_margin = Turtle()
top_margin.hideturtle()
top_margin.penup()
top_margin.color('white')
top_margin.goto(-300, 260)
top_margin.pendown()
top_margin.goto(300, 260)


snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
# move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        for turtle in snake.turtles:
            while turtle.distance == 0:
                food.refresh()
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall̦
    if abs(snake.head.xcor()) > 290 or snake.head.ycor() > 255 or snake.head.ycor() < -290:
        scoreboard.reset_scoreboard()
        snake.reset_snake()

    # Detect collision with tail
    for segment in snake.turtles[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_scoreboard()
            snake.reset_snake()


screen.exitonclick()
