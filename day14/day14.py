from itertools import cycle


NORTH = (0, -1)
WEST = (-1, 0)
SOUTH = (0, 1)
EAST = (1, -0)


def parse_input(f):
    return [line.strip() for line in f.readlines()]


def replace(grid, position, c):
    x, y = position
    line = grid[y][:x] + c + grid[y][x + 1 :]
    return grid[:y] + [line] + grid[y + 1 :]


def slide_one(grid, position, dir):
    dx, dy = dir
    x, y = position
    nx = x + dx
    ny = y + dy
    width = len(grid[0])
    height = len(grid)
    while nx >= 0 and ny >= 0 and nx < width and ny < height and grid[ny][nx] == ".":
        x, y = nx, ny
        nx = x + dx
        ny = y + dy
    grid = replace(grid, position, ".")
    grid = replace(grid, (x, y), "O")
    return grid


def slide(grid, dir):
    width = len(grid[0])
    height = len(grid)
    reverse = dir in [SOUTH, EAST]
    for y in reversed(range(height)) if reverse else range(height):
        for x in reversed(range(width)) if reverse else range(width):
            if grid[y][x] == "O":
                grid = slide_one(grid, (x, y), dir)
    return grid


def do_cycles(grid, n):
    grid_to_i = {}
    i = n * 4
    searching_cycle = True
    for dir in cycle([NORTH, WEST, SOUTH, EAST]):
        if i == 0:
            break

        key = "\n".join(grid), dir
        if searching_cycle and dir == NORTH and key in grid_to_i:
            i %= grid_to_i[key] - i
            searching_cycle = False
        elif searching_cycle:
            grid_to_i[key] = i

        grid = slide(grid, dir)
        i -= 1
    return grid


def get_load(grid):
    height = grid[0]
    return sum(len(height) - y for y, line in enumerate(grid) for c in line if c == "O")


def solve_part1(input):
    grid = slide(input, NORTH)
    return get_load(grid)


def solve_part2(input):
    grid = do_cycles(input, 1000000000)
    return get_load(grid)
