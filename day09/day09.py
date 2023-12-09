from itertools import tee
from functools import reduce


def parse_input(f):
    return [list(map(int, line.split(" "))) for line in f.readlines()]


def pairwise(l):
    a, b = tee(l)
    next(b, None)
    return zip(a, b)


def get_history_steps(history):
    steps = [history]
    while any(n != 0 for n in steps[-1]):
        step = [b - a for a, b in pairwise(steps[-1])]
        steps.append(step)

    return list(reversed(steps))


def extrapolate_right(steps):
    return reduce(lambda n, steps: steps[-1] + n, steps, 0)


def extrapolate_left(steps):
    return reduce(lambda n, step: step[0] - n, steps, 0)


def solve_part1(input):
    steps = [get_history_steps(history) for history in input]
    right_values = map(extrapolate_right, steps)
    return sum(right_values)


def solve_part2(input):
    steps = [get_history_steps(history) for history in input]
    left_values = map(extrapolate_left, steps)
    return sum(left_values)
