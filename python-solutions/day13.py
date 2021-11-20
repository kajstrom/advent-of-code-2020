import sys
from utils import time_fn

def read_input():
    file = open("inputs/day13.txt", "r")
    lines = file.read().splitlines()
    file.close()

    buses = []
    for bus in lines[1].split(","):
        if bus != 'x':
            buses.append(int(bus))

    return {
        "earliest": int(lines[0]),
        "buses": buses

    }

input = read_input()

def part1():
    best_bus = None
    best_time = sys.maxsize

    earliest = input["earliest"]
    for bus in input["buses"]:
        mod = earliest % bus
        first_possible_depart = earliest + (bus - mod)

        if best_time > first_possible_depart:
            best_bus = bus
            best_time = first_possible_depart

    print(f"Best bus {best_bus} Best time {best_time}")

    diff = best_time - earliest
    result = diff * best_bus

    print(f"Day 13, part 1: {result}")


if __name__ == '__main__':
    time_fn(part1)