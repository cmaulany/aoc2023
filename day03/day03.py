from itertools import chain, groupby
from math import prod


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


def get_parts(input):
    parts = []
    for y, line in enumerate(input):
        digits = ""
        for x, c in enumerate(line + "."):
            if c.isdigit():
                digits += c
            elif len(digits) > 0:
                neighbors = get_neighbors(x - len(digits), y, len(digits), input)
                if len(neighbors) > 0:
                    parts.append((int(digits), neighbors))
                digits = ""
    return parts


def solve_part1(input):
    parts = get_parts(input)
    return sum(number for number, _ in parts)


def solve_part2(input):
    parts = get_parts(input)
    gear_parts = [
        (digit, neighbor)
        for digit, neighbors in parts
        for neighbor in neighbors
        if neighbor[2] == "*"
    ]
    grouped = groupby(sorted(gear_parts, key=lambda x: x[1]), key=lambda x: x[1])

    ratios = []
    for _, group_iterator in grouped:
        group = list(group_iterator)
        if len(group) == 2:
            ratio = prod(map(lambda x: x[0], group))
            ratios.append(ratio)
    return sum(ratios)
