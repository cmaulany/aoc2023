from itertools import chain


def parse_input(stream):
    return [line.strip() for line in stream.readlines()]


def get_neighbors(x, y, length, input):
    left = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1)]
    middle = chain(*([(x + i, y - 1), (x + i, y + 1)] for i in range(length)))
    right = [(x + length, y - 1), (x + length, y), (x + length, y + 1)]

    positions = chain(left, middle, right)
    return [
        (x, y, input[y][x])
        for x, y in positions
        if x >= 0
        and x < len(input[0])
        and y >= 0
        and y < len(input)
        and input[y][x] != "."
    ]


def has_neighbor_symbol(x, y, length, input):
    return len(get_neighbors(x, y, length, input)) > 0


# print(input)
def solve_part1(input):
    numbers = []
    for y, line in enumerate(input):
        digits = ""
        for x in range(len(line) + 1):
            c = line[x] if x < len(line) else "."
            if c.isdigit():
                digits += c
            elif len(digits) > 0:
                neighbors = get_neighbors(x - len(digits), y, len(digits), input)
                if len(neighbors) > 0:
                    numbers.append(int(digits))
                digits = ""
    return sum(numbers)


def solve_part2(input):
    pass
