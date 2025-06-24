from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270
MOVE_DISTANCE = 20

move_complete = False
# x = 0
# y = 0

class Snake:
    def __init__(self):
        self.score = 0
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        global move_complete #, x, y
        # x = self.segments[len(self.segments) - 1].xcor()
        # y = self.segments[len(self.segments) - 1].ycor()
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        move_complete = True

    def move_north(self):
        global move_complete
        if move_complete and self.head.heading() != SOUTH:
            self.head.setheading(NORTH)
            move_complete = False

    def move_south(self):
        global move_complete
        if move_complete and self.head.heading() != NORTH:
            self.head.setheading(SOUTH)
            move_complete = False

    def move_west(self):
        global move_complete
        if move_complete and self.head.heading() != EAST:
            self.head.setheading(WEST)
            move_complete = False

    def move_east(self):
        global move_complete
        if move_complete and self.head.heading() != WEST:
            self.head.setheading(EAST)
            move_complete = False