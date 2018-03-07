import sys

from src.car import Car
from src.ride import Ride

simulation_data = {
    'ROWS': 0,
    'COLUMNS': 0,
    'FLEET': 0,
    'RIDE_COUNT': 0,
    'BONUS': 0,
    'TIME': 0
}

remaining_rides = []
cars = []


def get_input(filename):
    lines = []
    with open(filename) as f:
        read_data = f.readlines()

    for r in read_data:
        lines.append(r)

    extract_lines(lines)


def write_result_to_file(filename):
    with open(filename, 'w') as f:
        for car in cars:
            f.write(str(car) + '\n')


def extract_lines(lines):
    populate_simulation_data([int(x) for x in lines[0].split()])
    for line in lines[1:]:
        remaining_rides.append(Ride(line.split()))


def populate_simulation_data(meta):
    simulation_data['ROWS'] = meta[0]
    simulation_data['COLUMNS'] = meta[1]
    simulation_data['FLEET'] = meta[2]
    simulation_data['RIDE_COUNT'] = meta[3]
    simulation_data['BONUS'] = meta[4]
    simulation_data['TIME'] = meta[5]


def create_cars():
    for i in range(simulation_data['FLEET']):
        cars.append(Car())


def simulate_scenario():
    sort_rides_by_end_time()
    # for i in range(simulation_data['TIME']):
    #     print(i)
    #     simulate_step(i)
    for car in cars:
        print(car.number)
        simulate_car_route(car, simulation_data['TIME'])


def simulate_car_route(car, max_time):
    while max_time > car.busy_until:
        print(car.busy_until)
        car.filter_possible_rides(remaining_rides, car.busy_until)
        if len(car.possible_rides) > 0:
            car.take_ride(car.possible_rides[0], car.busy_until)
            remaining_rides.remove(car.possible_rides[0])
        else:
            break


def simulate_step(time_now):
    for car in cars:
        if car.busy_until < time_now:
            pick_best_ride(car, time_now)


def pick_best_ride(car, time_now):
    car.filter_possible_rides(remaining_rides, time_now)
    if len(car.possible_rides) > 0:
        car.take_ride(car.possible_rides[0], time_now)
        remaining_rides.remove(car.possible_rides[0])


def sort_rides_by_end_time():
    remaining_rides.sort(key=lambda r: r.end_time)


def main():
    get_input('data_sets/b_should_be_easy.in')
    create_cars()
    simulate_scenario()
    write_result_to_file('results/result_b.txt')


if __name__ == '__main__':
    main()