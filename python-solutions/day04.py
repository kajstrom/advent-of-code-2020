import re

def read_input():
    file = open("inputs/day04.txt", "r")
    lines = file.read().splitlines()
    file.close()

    return lines

def append_passport_field(passport, row):
    attributes = row.split(" ")

    for attribute in attributes:
        key, value = attribute.split(":")
        passport[key] = value

def collect_passports(input):
    passports = []

    current_passport = {}

    for row in input:
        if row != "":
            append_passport_field(current_passport, row)
        else:
            passports.append(current_passport)
            current_passport = {}

    return passports

def has_valid_fields(passport):
    required_fields = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid'
    ]

    for field in required_fields:
        if not (field in passport):
            return False

    return True

def has_valid_values(passport):
    byr = int(passport["byr"])
    if byr < 1920 or byr > 2002:
        return False

    iyr = int(passport["iyr"])
    if iyr < 2010 or iyr > 2020:
        return False

    eyr = int(passport["eyr"])
    if eyr < 2020 or eyr > 2030:
        return False

    hgt = passport["hgt"]
    if "cm" in hgt:
        hgt_num = int(hgt.replace("cm", ""))
        if hgt_num < 150 or hgt_num > 193:
            return False
    elif "in" in hgt:
        hgt_num = int(hgt.replace("in", ""))
        if hgt_num < 59 or hgt_num > 76:
            return False
    else:
        return False

    hcl = passport["hcl"]
    hcl_p = re.compile("#[0-9|a-f]{6}")
    if not hcl_p.fullmatch(hcl):
        return False

    valid_eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    ecl = passport["ecl"]
    if not (ecl in valid_eye_colors):
        return False

    pid = passport["pid"]
    pid_p = re.compile("[0-9]{9}")
    if not pid_p.fullmatch(pid):
        return False

    return True

def valid_passports(passports):
    valid = []

    for passport in passports:
        if has_valid_fields(passport):
            valid.append(passport)

    return valid

def part1():
    input = read_input()
    passports = collect_passports(input)
    valid = valid_passports(passports)

    valid_cnt = len(valid)

    print(f"Day 4, part 1: {valid_cnt}")

def part2():
    input = read_input()
    passports = collect_passports(input)
    valid_structure = valid_passports(passports)

    valid_contents = []

    for passport in valid_structure:
        if has_valid_values(passport):
            valid_contents.append(passport)

    valid_cnt = len(valid_contents)
    print(f"Day 4, part 2: {valid_cnt}")

part1()
part2()