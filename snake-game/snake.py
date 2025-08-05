from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        # Initialize the snake segments and create the initial snake
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # Create the initial snake by adding segments at starting positions
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        # Add a new segment to the snake at the given position
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        # Add a segment to the end of the snake
        self.add_segment(self.segments[-1].position())

    def move(self):
        # Move each segment to the position of the segment ahead of it
        for idx in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[idx - 1].xcor()
            new_y = self.segments[idx - 1].ycor()
            self.segments[idx].goto(new_x, new_y)
        # Move the head forward
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        # Move all segments off-screen and reset the snake
        for seg in self.segments:
            seg.goto(1000, 1000)  # move off-screen before clearing
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        # Change direction to up unless currently moving down
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Change direction to down unless currently moving up
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # Change direction to left unless currently moving right
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # Change direction to right unless currently moving left
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
