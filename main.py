import turtle
from turtle import Turtle, Screen
import time
from turtledemo.penrose import start
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard

screen = Screen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.setup(600,600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)


# coordinates = [(0,0),(-20,0),(-40,0)]
#
# segments = []
# for coordinate in coordinates:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(coordinate)
#     segments.append(new_segment)
game_is_on = True

screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.increase_length()

    # detect collision with a wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with self
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

# screen.listen()


# turtle.pendown()
print(f"pen up {turtle.penup()}")

screen.exitonclick()