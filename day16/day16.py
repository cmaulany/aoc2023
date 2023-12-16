from operator import itemgetter

UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)


def parse_input(f):
    return [line.strip() for line in f.readlines()]


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def energize(grid, initial=((0, 0), RIGHT)):
    width = len(grid[0])
    height = len(grid)

    visited = set()
    open = [initial]
    while open:
        current = open.pop()
        pos, dir = current
        px, py = pos
        if px < 0 or py < 0 or px >= width or py >= height or current in visited:
            continue

        visited.add(current)
        tile = grid[py][px]
        if tile == "|" and dir in [LEFT, RIGHT]:
            open.append((add(pos, UP), UP))
            open.append((add(pos, DOWN), DOWN))
        elif tile == "-" and dir in [UP, DOWN]:
            open.append((add(pos, LEFT), LEFT))
            open.append((add(pos, RIGHT), RIGHT))
        elif tile == "/":
            new_dir = {UP: RIGHT, RIGHT: UP, DOWN: LEFT, LEFT: DOWN}[dir]
            open.append((add(pos, new_dir), new_dir))
        elif tile == "\\":
            new_dir = {UP: LEFT, RIGHT: DOWN, DOWN: RIGHT, LEFT: UP}[dir]
            open.append((add(pos, new_dir), new_dir))
        else:
            open.append((add(pos, dir), dir))
    energized = set(map(itemgetter(0), visited))
    return energized


def find_optimal_configuration(grid):
    width = len(grid[0])
    height = len(grid)
    configs = (
        [((x, 0), DOWN) for x in range(width)]
        + [((x, height - 1), UP) for x in range(width)]
        + [((0, y), RIGHT) for y in range(height)]
        + [((width - 1, y), LEFT) for y in range(height)]
    )
    energized_tiles = [energize(grid, config) for config in configs]
    return max(map(len, energized_tiles))


def solve_part1(input):
    return len(energize(input))


def solve_part2(input):
    return find_optimal_configuration(input)
