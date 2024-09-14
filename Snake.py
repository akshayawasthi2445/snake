from turtle import Turtle

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20


UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.snake_len = 3
        self.last = self.segments[self.snake_len-1]


    def create_snake(self):
        for coordinate in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(coordinate)
            self.segments.append(new_segment)

    def change_coordinates(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)

    def increase_length(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup() # when moving the turtle object, it will not draw the line
        self.segments.append(new_segment)

        # getting the last coordinate
        x_last = self.last.xcor()
        y_last = self.last.ycor()

        if self.last.heading() == DOWN:
            new_segment.goto(x_last,y_last+1)
        elif self.last.heading() == UP:
            new_segment.goto(x_last,y_last-1)
        elif self.last.heading() == LEFT:
            new_segment.goto(x_last+1,y_last)
        elif self.last.heading() == RIGHT:
            new_segment.goto(x_last-1,y_last)

    def move(self):
        self.change_coordinates()
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        #self.change_coordinates()
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        #self.change_coordinates()
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

