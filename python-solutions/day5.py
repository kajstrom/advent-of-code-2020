import math

def read_input():
    file = open("inputs/day05.txt", "r")
    lines = file.read().splitlines()
    file.close()

    return lines

def calculate_row(row_steps):
    range_start = 0
    range_end = 127

    for step in row_steps:
        range = range_end - range_start

        middle = range / 2

        if step == "F":
            range_end = range_start + math.floor(middle)
        else:
            range_start = range_start + math.ceil(middle)

    if row_steps[-1] == "F":
        return range_start
    else:
        return range_end

def calculate_column(column_steps):
    range_start = 0
    range_end = 7

    for step in column_steps:
        range = range_end - range_start
        middle = range / 2

        if step == "L":
            range_end = range_start + math.floor(middle)
        else:
            range_start = range_start + math.ceil(middle)

    if column_steps[-1] == "L":
        return range_start
    else:
        return range_end

def calculate_seat_id(boarding_pass):
    row = calculate_row(boarding_pass[0:7])
    colum = calculate_column(boarding_pass[7:10])

    return row * 8 + colum


def part1():
    boarding_passes = read_input()
    seat_ids = []

    for boarding_pass in boarding_passes:
        seat_ids.append(calculate_seat_id(boarding_pass))

    print("Day 5, part 1: ", max(seat_ids))



#print(calculate_seat_id("FBFBBFFRLR"))
#print(calculate_seat_id("BFFFBBFRRR"))
#print(calculate_seat_id("FFFBBBFRRR"))
#print(calculate_seat_id("BBFFBBFRLL"))

part1()