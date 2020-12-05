file = open("inputs/day01.txt", "r")
lines = file.read().splitlines()
file.close()

def part_1(lines):
    for current_line_n in range(len(lines)):
        for next_line_n in range(current_line_n + 1, len(lines)):
            number1 = int(lines[current_line_n])
            number2 = int(lines[next_line_n])

            summed = number1 + number2

            if summed == 2020:
                print("Day 1, part 1: " + str(number1 * number2))


def part_2(lines):
    for first_line_n in range(len(lines)):
        number1 = int(lines[first_line_n])
        for second_line_n in range(first_line_n + 1, len(lines)):
            number2 = int(lines[second_line_n])
            for third_line_n in range(second_line_n + 2, len(lines)):
                number3 = int(lines[third_line_n])

                summed = number1 + number2 + number3

                if summed == 2020:
                    print("Day 1, part 2: " + str(number1 * number2 * number3))



part_1(lines)
part_2(lines)