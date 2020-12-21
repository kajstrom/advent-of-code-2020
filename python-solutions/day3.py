import operator
from functools import reduce


def read_input():
    file = open("inputs/day03.txt", "r")
    lines = file.read().splitlines()
    file.close()

    return lines

def lines_to_arrays(lines):
    arr_lines = []

    for line in lines:
        arr_lines.append(list(line))

    return arr_lines

def count_trees(arr_lines, slope):
    rows = len(arr_lines) - 1
    columns = len(arr_lines[0])
    down = slope["down"]
    right = slope["right"]

    curr_row = 0
    curr_col = 0
    trees = 0
    while curr_row != rows:
        curr_row = curr_row + down
        curr_col = (curr_col + right) % columns

        if arr_lines[curr_row][curr_col] == '#':
            trees = trees + 1


    return trees


def part1():
    lines = lines_to_arrays(read_input())

    trees_encountered = count_trees(lines, {"down": 1, "right": 3})

    print("Day 3, part 1: ", trees_encountered)

def part2():
    lines = lines_to_arrays(read_input())
    slopes = [
        {"down": 1, "right": 1},
        {"down": 1, "right": 3},
        {"down": 1, "right": 5},
        {"down": 1, "right": 7},
        {"down": 2, "right": 1},
    ]

    trees_encountered = []

    for slope in slopes:
        trees_encountered.append(count_trees(lines, slope))

    print(trees_encountered)
    print("Day 3, part 2: ", reduce(operator.mul, trees_encountered, 1))


part1()
part2()
