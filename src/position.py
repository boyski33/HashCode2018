

class Position:

    def __init__(self, x, y):
        self.row = int(x)
        self.col = int(y)

    def __repr__(self):
        return "{}, {}".format(self.row, self.col)

    def distance_between_positions(self, other):
        return abs(self.row - other.row) + abs(self.col - other.col)

