digit_values = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}

word_values = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

values_part1 = digit_values
values_part2 = {**digit_values, **word_values}


def parse_input(stream):
    return stream.readlines()


def solve(input, values):
    numbers = []
    for line in input:
        first_pairs = [
            (line.find(key), digit) for key, digit in values.items() if key in line
        ]
        min_pair = min(first_pairs, key=lambda pair: pair[0])
        first_digit = min_pair[1]

        last_pairs = [(line.rfind(key), value) for key, value in values.items()]
        max_pair = max(last_pairs, key=lambda pair: pair[0])
        last_digit = max_pair[1]

        number = int(first_digit + last_digit)
        numbers.append(number)

    calibration_value = sum(numbers)
    return calibration_value


def solve_part1(input):
    return solve(input, values_part1)


def solve_part2(input):
    return solve(input, values_part2)
