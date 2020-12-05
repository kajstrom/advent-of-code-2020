
file = open("inputs/day01.txt", "r")
lines = file.read().splitlines()
file.close()

for current_line_n in range(len(lines)):
    for next_line_n in range(current_line_n + 1, len(lines)):
        number1 = int(lines[current_line_n])
        number2 = int(lines[next_line_n])

        summed = number1 + number2

        if summed == 2020:
            print("Day 1, part 1: " + str(number1 * number2))
