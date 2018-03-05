from src.position import Position


class Ride:
    current_index = 0

    def __init__(self, ride):
        self.index = Ride.current_index
        Ride.current_index += 1
        self.start_position = Position(ride[0], ride[1])
        self.end_position = Position(ride[2], ride[3])
        self.start_time = int(ride[4])
        self.end_time = int(ride[5])

    def __repr__(self):
        # return "{} {} {} {}".format(self.start_position, self.end_position, self.start_time, self.end_time)
        return "{}: {}".format(self.index, self.end_time)

    def duration(self):
        return self.start_position.distance_between_positions(self.end_position)

    def latest_possible_pickup(self):
        return (self.end_time - 1) - self.duration()

    def calculate_time_delta(self):
        return self.end_time - self.start_time
