
def read_input():
    file = open("inputs/day06.txt", "r")
    lines = file.read().splitlines()
    file.close()

    return lines

def parse_groups(lines):
    groups = []

    current_group = ""
    for line in lines:
        if line != "":
            current_group = current_group + line
        else:
            groups.append(current_group)
            current_group = ""

    groups.append(current_group)

    return groups

def group_counts(groups):
    counts_per_group = []

    for group in groups:
        unique_answers = list(set(list(group)))
        counts_per_group.append(len(unique_answers))

    return counts_per_group


def part1():
    lines = read_input()
    groups = parse_groups(lines)
    counts = group_counts(groups)

    print("Day 6, part 1: ", sum(counts))

def parse_groups_per_person(lines):
    groups = []

    current_group = []
    for line in lines:
        if line != "":
            current_group.append(list(line))
        else:
            groups.append(current_group)
            current_group = []

    groups.append(current_group)

    return groups

def group_common_counts(groups):
    counts_per_group = []

    for group in groups:
        common_answers = set(group[0])
        for person in group[1:]:
            common_answers = common_answers.intersection(person)

        counts_per_group.append(len(common_answers))

    return counts_per_group

def part2():
    lines = read_input()
    groups = parse_groups_per_person(lines)
    counts = group_common_counts(groups)

    print("Day 6, part 2: ", sum(counts))

part1()
part2()
