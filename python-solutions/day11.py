from utils import time_fn, count
import copy
import numpy as np


def read_input():
    file = open("inputs/day11.txt", "r")
    lines = file.read().splitlines()
    file.close()

    grid = []
    for line in lines:
        grid.append(list(line))

    return grid

def get_from(grid, x, y, oob = None):
    max_y = len(grid)
    max_x = len(grid[0])

    if x < 0 or x >= max_x:
        return oob
    elif y < 0 or y >= max_y:
        return oob
    else:
        return grid[y][x]

def get_adjacent(grid, x, y):
    adjacent = []

    adjacent.append(get_from(grid, x - 1, y - 1))
    adjacent.append(get_from(grid, x, y - 1))
    adjacent.append(get_from(grid, x + 1, y - 1))
    adjacent.append(get_from(grid, x - 1, y))
    adjacent.append(get_from(grid, x + 1, y))
    adjacent.append(get_from(grid, x - 1, y + 1))
    adjacent.append(get_from(grid, x, y + 1))
    adjacent.append(get_from(grid, x + 1, y + 1))

    return adjacent


def play_round(grid):
    next_grid = copy.deepcopy(grid)
    changes = 0

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            position = grid[y][x]

            # L = empty
            # # = occupied
            # . = floor

            if position == "L":
                adjacent = get_adjacent(grid, x, y)
                occupied_adjacent = count("#", adjacent)

                if occupied_adjacent == 0:
                    next_grid[y][x] = "#"
                    changes += 1
            elif position == "#":
                adjacent = get_adjacent(grid, x, y)
                occupied_adjacent = count("#", adjacent)

                if occupied_adjacent >= 4:
                    next_grid[y][x] = "L"
                    changes += 1

    return next_grid, changes


def part1():
    grid = read_input()
    changes = 1
    rounds = 0

    while changes != 0:
        grid, changes = play_round(grid)
        rounds += 1
        #print(rounds, changes)

    flat_grid = list(np.concatenate(grid).flat)
    occupied_cnt = count("#", flat_grid)

    print(f"Day 11, part 1: {occupied_cnt}")

time_fn(part1)