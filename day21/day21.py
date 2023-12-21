from itertools import permutations


def parse_input(f):
    return [line.strip() for line in f.readlines()]


def get_start(input):
    return next(
        (x, y) for y, line in enumerate(input) for x, c in enumerate(line) if c == "S"
    )


def get_neighbors(grid, position):
    x, y = position
    width = len(grid[0])
    height = len(grid)
    deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    neighbors = [(x + dx, y + dy) for dx, dy in deltas]
    r = [
        (nx, ny)
        for nx, ny in neighbors
        if nx >= 0 and nx < width and ny >= 0 and ny < height
        if grid[ny][nx] != "#"
    ]
    return r


def find_edges(map, start):
    width = len(map[0])
    height = len(map)

    is_border = {
        "top": lambda pos: pos[1] == 0,
        "left": lambda pos: pos[0] == 0,
        "right": lambda pos: pos[0] == width - 1,
        "bottom": lambda pos: pos[1] == height - 1,
    }

    borders = {
        "top": None,
        "left": None,
        "right": None,
        "bottom": None,
    }

    open = set([start])
    visited = set()
    distance = 0
    while True:
        for name, value in borders.items():
            for pos in open:
                if value == None and is_border[name](pos):
                    borders[name] = (distance, pos)

        if all(value != None for value in borders.values()):
            return borders

        next_open = []
        for current in open:
            visited.add(current)
            for neighbor in get_neighbors(map, current):
                if neighbor not in visited:
                    next_open.append(neighbor)
        open = set(next_open)
        distance += 1


def flood_fill(map, size, starts):
    open = set(starts)
    visited = set()
    for _ in range(size):
        next_open = []
        for current in open:
            visited.add(current)
            for neighbor in get_neighbors(map, current):
                if neighbor not in visited:
                    next_open.append(neighbor)
        open = set(next_open)
    return visited


def get_edge_neighbor(input, name, position):
    x, y = position
    width = len(input[0])
    height = len(input)

    return {
        "top": (x, (y - 1) % height),
        "bottom": (x, (y + 1) % height),
        "left": ((x - 1) % width, y),
        "right": ((x + 1) % width, y),
    }[name]


def inner_surface(l):
    s = 1
    for i in range(l + 1):
        s += i * 4
    return s


def get_steps_for_tick(positions, tick):
    offset = tick % 2
    # offset = 0
    return len([(x, y) for x, y in positions if x % 2 == (y + offset) % 2])


def solve_part1(input):
    start = get_start(input)
    surface = flood_fill(input, 64, [start])
    positions = get_steps_for_tick(surface, 64)
    return positions


def solve_part2(input):
    ticks = 26501365
    size = len(input[0])
    rem = (size - 1) // 2

    start = get_start(input)

    edges = find_edges(input, start)
    edge_points = [pos for _, pos in edges.values()]

    repeats = (ticks - rem) // size

    trbl_positions = 0
    for pos in edge_points:
        surface = flood_fill(input, rem, [pos])
        trbl_positions += get_steps_for_tick(surface, ticks)

    full_positions = flood_fill(input, size, [start])
    inner_positions = get_steps_for_tick(full_positions, ticks) * inner_surface(repeats)

    diagonal_positions = 0
    diagonal_edges_perms = list(permutations(edge_points, 2))
    for diagonal_edges in diagonal_edges_perms:
        surface = flood_fill(input, rem - 1, diagonal_edges)
        positions = get_steps_for_tick(surface, ticks)
        diagonal_positions += positions * repeats

    total_positions = inner_positions + trbl_positions + diagonal_positions
    return total_positions
