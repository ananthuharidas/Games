from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.spawn_the_snake()
        self.head = self.segments[0]

    def spawn_the_snake(self):
        """Define the starting position of the snake at the beginning of the game."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        """Move the snake automatically once it is spawned."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        """Add a new segment to the snake."""
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setposition(position)
        self.segments.append(new_segment)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.spawn_the_snake()
        self.head = self.segments[0]

    def up(self):
        """Move the snake up."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Move the snake down."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Move the snake up."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Move the snake up."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
