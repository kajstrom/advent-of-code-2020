def read_input(file):
    with open(file) as f:
        return f.read().splitlines()


def parse_values(line):
    parsed_line = []
    while len(line) > 0:
        value = line[0]
        line = line[1:]

        if value == '+':
            parsed_line.append(value)
        elif value == '*':
            parsed_line.append(value)
        elif value == '(':
            sub_list, line = parse_values(line)
            parsed_line.append(sub_list)
        elif value == ')':
            return parsed_line, line
        elif value != ' ':
            parsed_line.append(int(value))

    return parsed_line, line


def do_math(operations):
    value = operations[0]
    operations = operations[1:]

    if type(value) is list:
        value = do_math(value)

    while len(operations) > 0:
        operator = operations[0]
        value_2 = operations[1]

        if type(value_2) is list:
            value_2 = do_math(value_2)

        operations = operations[2:]

        if operator == '+':
            value = value + value_2
        else:
            value = value * value_2

    return value


if __name__ == '__main__':
    lines = read_input('inputs/day18.txt')
    sum = 0
    for line in lines:
        parsed_line = parse_values(line)[0]
        print(parsed_line)
        sum += do_math(parsed_line)

    print(f"Day 18, part 1: {sum}")