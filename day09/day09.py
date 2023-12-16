from functools import reduce


def parse_input(f):
    return [list(map(int, line.split(" "))) for line in f.readlines()]


def pairwise(list):
    return ((list[i], list[i + 1]) for i in range(len(list) - 1))


def get_history_steps(history):
    steps = [history]
    while any(n != 0 for n in steps[0]):
        step = [b - a for a, b in pairwise(steps[0])]
        steps.insert(0, step)

    return steps


def extrapolate_right(steps):
    return reduce(lambda n, step: step[-1] + n, steps, 0)


def extrapolate_left(steps):
    return reduce(lambda n, step: step[0] - n, steps, 0)


def solve_part1(input):
    histories_steps = map(get_history_steps, input)
    right_values = map(extrapolate_right, histories_steps)
    return sum(right_values)


def solve_part2(input):
    histories_steps = map(get_history_steps, input)
    left_values = map(extrapolate_left, histories_steps)
    return sum(left_values)
