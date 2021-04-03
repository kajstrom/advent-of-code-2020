import copy
from utils import time_fn

def read_input():
    file = open("inputs/day08.txt", "r")
    lines = file.read().splitlines()
    file.close()

    instructions = []
    for line in lines:
        op, val = line.split(" ")
        instructions.append({"op": op, "val": int(val)})

    return instructions

def run_instructions(instructions):
    accumulator = 0
    pointer = 0
    visited = []
    instructions_len = len(instructions)
    completed = False

    while True:
        if pointer >= instructions_len or pointer < 0:
            completed = True
            break

        if pointer not in visited:
            instruction = instructions[pointer]
            visited.append(pointer)
            op = instruction["op"]
            val = instruction["val"]

            if op == "acc":
                accumulator += val
                pointer += 1
            elif op == "jmp":
                pointer += val
            else:
                # Nop
                pointer += 1
        else:
            completed = False
            break

    return accumulator, completed

def part1():
    instructions = read_input()
    accumulator, completed = run_instructions(instructions)

    print(f"Day 8, part 1: {accumulator}")

def part2():
    instructions = read_input()

    for i in range(len(instructions)):
        altered_instructions = copy.deepcopy(instructions)
        instruction = altered_instructions[i]
        altered = False

        if instruction["op"] == "jmp":
            instruction["op"] = "nop"
            altered = True
        elif instruction["op"] == "nop":
            instruction["op"] = "jmp"
            altered = True

        if altered:
            accumulator, completed = run_instructions(altered_instructions)

            if completed:
                print(f"Day 8, part 2: {accumulator}")
                break


time_fn(part1)
time_fn(part2)