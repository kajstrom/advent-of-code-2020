from utils import time_fn

starting_numbers = [None, 0, 5, 4, 1, 10, 14, 7]

def part1():
    reverse_numbers = list(reversed(starting_numbers))
    last_number_spoken = reverse_numbers[0]

    print(reverse_numbers, last_number_spoken)

    turn = len(reverse_numbers)
    while turn <= 2020:
        if reverse_numbers.count(last_number_spoken) >= 2:
            last_turn_spoken_idx = reverse_numbers.index(last_number_spoken)
            last_turn_spoken = len(reverse_numbers) - 1 - last_turn_spoken_idx

            previous_turn_spoken_idx = len(reverse_numbers) - 1 - reverse_numbers.index(last_number_spoken, last_turn_spoken_idx + 1)
            last_number_spoken = last_turn_spoken - previous_turn_spoken_idx
        else:
            last_number_spoken = 0

        reverse_numbers.insert(0, last_number_spoken)

        turn += 1

    print(f"Day 15, part 1: {last_number_spoken}")

def part2():
    numbers = {}

    turn = 1
    for number in starting_numbers[1:]:
        numbers[number] = [turn]

        turn += 1

    last_number_spoken = number
    turn = len(starting_numbers)
    while turn <= 30000000:
        seen_number = last_number_spoken in numbers

        if seen_number and len(numbers[last_number_spoken]) >= 2:
            last_turn_spoken = numbers[last_number_spoken][-1]
            previous_turn_spoken = numbers[last_number_spoken][-2]

            last_number_spoken = last_turn_spoken - previous_turn_spoken
        else:
            last_number_spoken = 0

        if last_number_spoken in numbers:
            numbers[last_number_spoken].append(turn)
        else:
            numbers[last_number_spoken] = [turn]

        turn += 1


    print(f"Day 15, part 2: {last_number_spoken}")


if __name__ == '__main__':
    time_fn(part1)
    time_fn(part2)