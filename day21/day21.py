def parse_input(f):
    return [line.strip() for line in f.readlines()]


def get_start(input):
    return next(
        (x, y) for y, line in enumerate(input) for x, c in enumerate(line) if c == "S"
    )


def get_neighbors(grid, position, wrap=False):
    x, y = position
    width = len(grid[0])
    height = len(grid)
    deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    neighbors = [(x + dx, y + dy) for dx, dy in deltas]
    return [
        (nx, ny)
        for nx, ny in neighbors
        if wrap or (nx >= 0 and nx < width and ny >= 0 and ny < height)
        if grid[ny % height][nx % width] != "#"
    ]


def flood_fill(map, steps, start, wrap=False):
    open = set([start])
    visited = set()
    for _ in range(steps + 1):
        next_open = []
        for current in open:
            visited.add(current)
            for neighbor in get_neighbors(map, current, wrap):
                if neighbor not in visited:
                    next_open.append(neighbor)
        open = set(next_open)
    return visited


def count_positions_for_step(surface, step):
    offset = step % 2
    return len([(x, y) for x, y in surface if x % 2 == (y + offset) % 2])


def solve_part1(input, steps=64):
    start = get_start(input)
    positions = flood_fill(input, steps, start, True)
    return count_positions_for_step(positions, steps)


def solve_part2(input, steps=26501365):
    width = len(input[0])
    half_width = (width - 1) // 2
    l = (steps - half_width) // width

    start = get_start(input)

    full_tile_positions = flood_fill(input, width * 2, start)
    full_tile_count_a = count_positions_for_step(full_tile_positions, steps)
    full_tile_count_b = count_positions_for_step(full_tile_positions, steps + 1)

    inner_count = full_tile_count_a
    for i in range(1, l):
        count = full_tile_count_a if i % 2 == 0 else full_tile_count_b
        inner_count += count * i * 4

    tip_count = 0
    edge_centers = [
        (0, half_width),
        (width - 1, half_width),
        (half_width, 0),
        (half_width, width - 1),
    ]
    for pos in edge_centers:
        positions = flood_fill(input, width, pos)
        tip_count += count_positions_for_step(positions, steps)

    diagonal_positions = 0
    corners = [
        (0, 0),
        (width - 1, 0),
        (0, width - 1),
        (width - 1, width - 1),
    ]
    for pos in corners:
        positions = flood_fill(input, half_width - 1, pos)
        diagonal_positions += count_positions_for_step(positions, steps + 1) * l

        positions = flood_fill(input, width + half_width - 1, pos)
        positions = count_positions_for_step(positions, steps + 0)
        diagonal_positions += positions * (l - 1)

    return inner_count + tip_count + diagonal_positions
