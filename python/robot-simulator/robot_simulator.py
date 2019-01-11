# Globals for the bearings
# Change the values as you see fit
EAST = (1,0)
WEST = (-1,0)
NORTH = (0,1)
SOUTH = (0,-1)


class Robot(object):

    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.coordinates = (x, y)

    def advance(self):
        x, y = self.coordinates
        moviment_x, moviment_y = self.bearing
        x += moviment_x
        y += moviment_y
        self.coordinates = (x, y)

    def turn_right(self):
        parameter = {NORTH:EAST, EAST:SOUTH, SOUTH:WEST, WEST:NORTH}
        self.bearing = parameter[self.bearing]

    def turn_left(self):
        parameter = {NORTH:WEST, EAST:NORTH, SOUTH:EAST, WEST:SOUTH}
        self.bearing = parameter[self.bearing]

    def simulate(self, orders):
        for order in orders:
            if order == 'R':
                self.turn_right()
            elif order == 'L':
                self.turn_left()
            elif order == 'A':
                self.advance()