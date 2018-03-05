from src.position import Position


class Car:
    current_number = 1

    def __init__(self):
        self.number = Car.current_number
        Car.current_number += 1
        self.position = Position(0, 0)
        self.taken_rides_indexes = []
        self.possible_rides = []
        self.busy_until = 0

    def __str__(self):
        return "{} {}".format(len(self.taken_rides_indexes), ' '.join(self.taken_rides_indexes))

    def __repr__(self):
        return self.__str__()

    def filter_possible_rides(self, rides, time_now):
        self.possible_rides = []
        for r in rides:
            if time_now + self.distance_to_ride(r) < r.latest_possible_pickup():
                self.possible_rides.append(r)

    def distance_to_ride(self, ride):
        return self.position.distance_between_positions(ride.start_position)

    def take_ride(self, ride, time_now):
        self.taken_rides_indexes.append(str(ride.index))
        self.busy_until = time_now + self.distance_to_ride(ride) + ride.duration()
        self.position = ride.end_position
