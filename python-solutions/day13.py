import sys
import bisect
from operator import itemgetter

from utils import time_fn
import numpy as np

def read_input():
    file = open("inputs/day13.txt", "r")
    lines = file.read().splitlines()
    file.close()

    buses = []
    i = 0
    for bus in lines[1].split(","):
        if bus != 'x':
            buses.append({
                "number": int(bus),
                "index": i
            })
        i += 1

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
        bus = bus["number"]
        mod = earliest % bus
        first_possible_depart = earliest + (bus - mod)

        if best_time > first_possible_depart:
            best_bus = bus
            best_time = first_possible_depart

    print(f"Best bus {best_bus} Best time {best_time}")

    diff = best_time - earliest
    result = diff * best_bus

    print(f"Day 13, part 1: {result}")



def create_bus_ranges(buses):
    first_bus_number = buses[0]["number"]

    bus_ranges = []
    bus_range = range(0, sys.maxsize, first_bus_number)
    bus_ranges.append(bus_range)
    for bus in buses[1:]:
        number = bus["number"]
        offset = bus["index"] % first_bus_number

        bus_range = range(0, sys.maxsize, number)
        bus_ranges.append(bus_range)

    return bus_ranges

def part2():
    buses = input["buses"]

    bus_n = 1
    for bus in buses:
        bus_n = bus_n * bus["number"]

    result = 0
    #Chinese remainder theorem
    for bus in buses:
        bi = bus["number"] - bus["index"]
        mod = bus["number"]

        Ni = int(bus_n / mod)

        xi = pow(Ni, mod - 2, mod)

        temp_res = bi * Ni * xi

        result += temp_res

    result = result % bus_n
    print(f"Day 13, part 2: {result}")


if __name__ == '__main__':
    time_fn(part1)
    time_fn(part2)