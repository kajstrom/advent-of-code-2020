file = open("inputs/day02.txt", "r")
lines = file.read().splitlines()
file.close()

def parse_password_and_policy(line):
    policy_str, password = line.split(": ")

    times, character = policy_str.split(" ")
    min, max = times.split("-")
    min = int(min)
    max = int(max)

    return {
        "min": min,
        "max": max,
        "character": character,
        "password": password
    }

def is_valid(password_and_policy):
    char_count = password_and_policy["password"].count(password_and_policy["character"])
    min = password_and_policy["min"]
    max = password_and_policy["max"]

    return char_count >= min and char_count <= max


def part_1(lines):
    valid_cnt = 0
    for line in lines:
        policy = parse_password_and_policy(line)

        if is_valid(policy):
            valid_cnt = valid_cnt + 1

    print("Day 2, part 1: " + str(valid_cnt))

def is_valid_part2(password_and_policy):
    password = password_and_policy["password"]
    character = password_and_policy["character"]
    pos1 = password_and_policy["min"] - 1
    pos2 = password_and_policy["max"] - 1

    pos1_has_char = password[pos1] == character
    pos2_has_char = password[pos2] == character

    if pos1_has_char and pos2_has_char:
        return False
    elif pos1_has_char and not pos2_has_char:
        return True
    elif not pos1_has_char and pos2_has_char:
        return True
    else:
        return False


def part_2(lines):
    valid_cnt = 0
    for line in lines:
        policy = parse_password_and_policy(line)

        if is_valid_part2(policy):
            valid_cnt = valid_cnt + 1

    print("Day 2, part 2: " + str(valid_cnt))


part_1(lines)
part_2(lines)
