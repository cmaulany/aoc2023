from functools import cache


def parse_input(f):
    rows = []
    for line in f.readlines():
        springs, groups_input = line.strip().split(" ")
        groups = tuple(map(int, groups_input.split(",")))
        rows.append((springs, groups))
    return rows


@cache
def count_solutions(springs, groups):
    if len(groups) == 0:
        return "#" not in springs

    first = groups[0]
    if first > len(springs):
        return 0

    count = 0
    if all(springs[i] in "#?" for i in range(first)) and (
        first == len(springs) or springs[first] != "#"
    ):
        count += count_solutions(springs[first + 1 :], groups[1:])

    if springs[0] == "." or springs[0] == "?":
        count += count_solutions(springs[1:], groups)

    return count


def solve_part1(input):
    return sum(count_solutions(*row) for row in input)


def solve_part2(input):
    rows = [(springs + ("?" + springs) * 4, groups * 5) for springs, groups in input]
    return sum(count_solutions(*row) for row in rows)
