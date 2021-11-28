from enum import Enum

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
    print(bin_value)

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





part1()