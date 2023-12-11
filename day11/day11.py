from itertools import combinations


def parse_input(f):
    return [line.strip() for line in f.readlines()]


def get_expansion_zones(universe):
    width = len(universe[0])
    xzones = [x for x in range(width) if all(line[x] == "." for line in universe)]
    yzones = [y for y, line in enumerate(universe) if all(c == "." for c in line)]
    return xzones, yzones


def get_positions(universe):
    return [
        (x, y)
        for y, line in enumerate(universe)
        for x, c in enumerate(line)
        if c == "#"
    ]


def dis(a, b, expansion_zones, scale=1):
    ax, ay = a
    bx, by = b
    xzones, yzones = expansion_zones
    xzone_count = len([x for x in xzones if x >= min(ax, bx) and x < max(ax, bx)])
    yzone_count = len([y for y in yzones if y >= min(ay, by) and y < max(ay, by)])
    return (
        abs(ax - bx) + abs(ay - by) + (xzone_count + yzone_count) * (scale - 1)
    )


def solve(input, scale):
    expansion_zones = get_expansion_zones(input)
    positions = get_positions(input)
    distances = [
        dis(a, b, expansion_zones, scale) for a, b in combinations(positions, 2)
    ]
    return sum(distances)


def solve_part1(input):
    return solve(input, 2)


def solve_part2(input, scale=1000000):
    return solve(input, scale)
