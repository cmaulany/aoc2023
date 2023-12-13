number_digits = {
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

word_digits = {
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

valid_digits_part1 = number_digits
valid_digits_part2 = {**number_digits, **word_digits}


def parse_input(f):
    return f.readlines()


def find_calibration_value(line, valid_digits):
    first_pairs = [
        (line.find(key), digit) for key, digit in valid_digits.items() if key in line
    ]
    min_pair = min(first_pairs, key=lambda pair: pair[0])
    first_digit = min_pair[1]

    last_pairs = [
        (line.rfind(key), digit) for key, digit in valid_digits.items() if key in line
    ]
    max_pair = max(last_pairs, key=lambda pair: pair[0])
    last_digit = max_pair[1]

    return int(first_digit + last_digit)


def solve(input, valid_digits):
    calibration_values = [find_calibration_value(line, valid_digits) for line in input]
    total = sum(calibration_values)
    return total


def solve_part1(input):
    return solve(input, valid_digits_part1)


def solve_part2(input):
    return solve(input, valid_digits_part2)
