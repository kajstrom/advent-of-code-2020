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

    print(last_number_spoken)



if __name__ == '__main__':
    time_fn(part1)