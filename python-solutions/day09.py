from utils import time_fn
import numpy as np

preamble_len = 25

def read_input():
    file = open("inputs/day09.txt", "r")
    lines = file.read().splitlines()
    file.close()

    numbers = []
    for line in lines:
        numbers.append(int(line))

    return numbers

def is_sum_of(numbers, number):
    for i in range(len(numbers)):
        first = numbers[i]

        for j in range(len(numbers)):
            if i == j:
                continue
            second = numbers[j]
            sum = first + second
            #print(f"{first} + {second} = {sum}")

            if sum == number:
                return True

    return False

def part1():
    numbers = read_input()
    pointer = preamble_len

    numbers_to_test = numbers[preamble_len:]

    for number in numbers_to_test:
        start = pointer - preamble_len
        end = pointer

        previous = numbers[start:end]

        if not is_sum_of(previous, number):
            print(f"Day 9, part 1: {number}")
            return number

        pointer += 1

def contiguous_set_sums_up_to(numbers, to):
    contiguous_set = []

    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[j] == to:
                continue

            contiguous_set.append(numbers[j])
            sum = np.sum(contiguous_set)
            #print(sum)

            if sum == to:
                return contiguous_set
            elif sum > to:
                #print(f"Sum {sum} exceeded")
                contiguous_set = []
                break




def part2():
    numbers = read_input()
    invalid_number = part1()
    contiguous_set = contiguous_set_sums_up_to(numbers, invalid_number)

    smallest = min(contiguous_set)
    largest = max(contiguous_set)

    encryption_weakness = smallest + largest
    print(f"Day 9, part 2: {encryption_weakness}")


time_fn(part2)
