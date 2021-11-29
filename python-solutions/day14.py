from enum import Enum
from itertools import combinations, combinations

from utils import time_fn

class Instuction(Enum):
    MASK = "mask"
    MEM = "mem"

def read_input():
    file = open("inputs/day14.txt", "r")
    lines = file.read().splitlines()
    file.close()

    instructions = []
    for line in lines:
        if line.__contains__("mask"):
            instructions.append({
                "type": Instuction.MASK,
                "value": list(line[7:])
            })
        elif line.__contains__(Instuction.MEM.value):
            address_start = line.index("[") + 1
            address_end = line.index("]")
            value_start = line.index("=") + 1
            instructions.append({
                "type": Instuction.MEM,
                "value": int(line[value_start:]),
                "address": int(line[address_start:address_end])
            })

    return instructions

instructions = read_input()

def store_value(memory, mask, address, value):
    bin_value = list(f'{value:b}'.zfill(36))

    final_value = ""
    for mask_value, value in zip(mask, bin_value):
        if mask_value == 'X':
            final_value += value
        elif mask_value == '1':
            final_value += '1'
        elif mask_value == '0':
            final_value += '0'

    memory[address] = final_value

def part1():
    memory = {}
    mask = None

    for instruction in instructions:
        if instruction["type"] == Instuction.MASK:
            mask = instruction["value"]
        else:
            store_value(memory, mask, instruction["address"], instruction["value"])

    result = 0
    for mem_loc in memory.values():
        result += int(mem_loc, base=2)

    print(f"Day 14, part 1: {result}")

def gen_floating_bit_combinations(floating_count):
    i = 0
    address_bits = []
    while i < floating_count:
        address_bits.append(0)
        address_bits.append(1)

        i += 1

    address_bit_combinations = []
    for combination in combinations(address_bits, floating_count):
        address_bit_combinations.append(combination)

    return list(set(address_bit_combinations))

def store_value2(memory, mask, address, value):
    bin_address = list(f'{address:b}'.zfill(36))

    # generate addresses
    floating_count = mask.count('X')

    address_bit_combinations = gen_floating_bit_combinations(floating_count)

    addresses = []
    for floating_combinations in address_bit_combinations:
        address_str = ""
        for mask_value, address_value in zip(mask, bin_address):
            if mask_value == 'X':
                address_str += str(floating_combinations[0])
                floating_combinations = floating_combinations[1:]
            elif mask_value == '1':
                address_str += '1'
            elif mask_value == '0':
                address_str += address_value

        addresses.append(int(address_str, base=2))

    for address in addresses:
        memory[address] = f'{value:b}'.zfill(36)


def part2():
    memory = {}
    mask = None

    for instruction in instructions:
        if instruction["type"] == Instuction.MASK:
            mask = instruction["value"]
        else:
            store_value2(memory, mask, instruction["address"], instruction["value"])

    result = 0
    for mem_loc in memory.values():
        result += int(mem_loc, base=2)

    print(f"Day 14, part 2: {result}")



if __name__ == '__main__':
    time_fn(part1)
    time_fn(part2)