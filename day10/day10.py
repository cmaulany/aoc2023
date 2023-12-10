NORTH = (0, -1)
EAST = (1, 0)
SOUTH = (0, 1)
WEST = (-1, 0)


def get_start(map):
    position = next((line.index("S"), y) for y, line in enumerate(map) if "S" in line)
    x, y = position

    n = map[y - 1][x] in "|7F"
    e = map[y][x + 1] in "-J7"
    s = map[y + 1][x] in "|LJ"
    w = map[y][x - 1] in "-LF"
    if n and s:
        type = "|"
    if e and w:
        type = "-"
    if n and e:
        type = "L"
    if n and w:
        type = "J"
    if s and w:
        type = "7"
    if e and s:
        type = "F"

    return position, type


def parse_input(f):
    map = [line.strip() for line in f.readlines()]

    start_position, start_type = get_start(map)
    sx, sy = start_position

    map[sy] = map[sy][:sx] + start_type + map[sy][sx + 1 :]
    return map, start_position


def get_neighbors(map, position):
    px, py = position
    width = len(map[0])
    height = len(map)

    type = map[py][px]
    deltas = {
        "|": [NORTH, SOUTH],
        "-": [EAST, WEST],
        "L": [NORTH, EAST],
        "J": [WEST, NORTH],
        "7": [WEST, SOUTH],
        "F": [EAST, SOUTH],
    }[type]

    neighbors = [(px + dx, py + dy) for dx, dy in deltas]

    return [
        (px, py)
        for px, py in neighbors
        if px >= 0 and px < width and py >= 0 and py < height
    ]


def find_path(map, start):
    open = [start]
    visited = set()
    prevs = {}
    while open:
        current = open.pop()
        if visited and current == start:
            break

        visited.add(current)
        for neighbor in get_neighbors(map, current):
            if neighbor != "." and (neighbor == start or neighbor not in visited):
                open.append(neighbor)
                prevs[neighbor] = current

    path = []
    current = start
    while current != start or not path:
        path.append(current)
        current = prevs[current]
    return path


def get_sub_neighbors(map, start_position):
    """
    We divide each tile into for subtiles:
    A | B
    - + -
    C | D
    """
    x, y = start_position
    type = map[int(y / 2)][int(x / 2)]

    sub_position = (x % 2, y % 2)
    sub_type = {
        (0, 0): "A",
        (1, 0): "B",
        (0, 1): "C",
        (1, 1): "D",
    }[sub_position]

    deltas = {
        ".": {
            "A": [NORTH, EAST, SOUTH, WEST],
            "B": [NORTH, EAST, SOUTH, WEST],
            "C": [NORTH, EAST, SOUTH, WEST],
            "D": [NORTH, EAST, SOUTH, WEST],
        },
        "|": {
            "A": [NORTH, SOUTH, WEST],
            "B": [NORTH, EAST, SOUTH],
            "C": [NORTH, SOUTH, WEST],
            "D": [NORTH, EAST, SOUTH],
        },
        "-": {
            "A": [NORTH, EAST, WEST],
            "B": [NORTH, EAST, WEST],
            "C": [EAST, SOUTH, WEST],
            "D": [EAST, SOUTH, WEST],
        },
        "L": {
            "A": [NORTH, SOUTH, WEST],
            "B": [NORTH, EAST],
            "C": [NORTH, EAST, SOUTH, WEST],
            "D": [EAST, SOUTH, WEST],
        },
        "J": {
            "A": [NORTH, WEST],
            "B": [NORTH, EAST, SOUTH],
            "C": [EAST, SOUTH, WEST],
            "D": [NORTH, EAST, SOUTH, WEST],
        },
        "7": {
            "A": [NORTH, EAST, WEST],
            "B": [NORTH, EAST, SOUTH, WEST],
            "C": [SOUTH, WEST],
            "D": [NORTH, EAST, SOUTH],
        },
        "F": {
            "A": [NORTH, EAST, SOUTH, WEST],
            "B": [NORTH, EAST, WEST],
            "C": [NORTH, SOUTH, WEST],
            "D": [SOUTH, EAST],
        },
    }[type][sub_type]

    neighbors = [(x + dx, y + dy) for dx, dy in deltas]

    width = len(map[0]) * 2
    height = len(map) * 2
    return [
        (x, y) for x, y in neighbors if x >= 0 and x < width and y >= 0 and y < height
    ]


def flood_fill(map, position=(0, 0)):
    open = [position]
    visited = set()
    while open:
        current = open.pop()

        visited.add(current)
        for neighbor in get_sub_neighbors(map, current):
            if neighbor not in visited:
                open.append(neighbor)

    width = range(len(map[0]))
    height = range(len(map))
    return {
        (x, y)
        for x in width
        for y in height
        if (x * 2, y * 2) in visited
        and (x * 2 + 1, y * 2) in visited
        and (x * 2, y * 2 + 1) in visited
        and (x * 2 + 1, y * 2 + 1) in visited
    }


def solve_part1(input):
    map, start_position = input
    path = find_path(map, start_position)
    return len(path) // 2


def solve_part2(input):
    map, start_position = input

    loop = set(find_path(map, start_position))
    loop_map = [
        "".join(type if (x, y) in loop else "." for x, type in enumerate(line))
        for y, line in enumerate(map)
    ]
    outer_positions = flood_fill(loop_map)

    width = range(len(map[0]))
    height = range(len(map))
    enclosed_positions = [
        (x, y)
        for x in width
        for y in height
        if (x, y) not in loop and (x, y) not in outer_positions
    ]
    return len(enclosed_positions)
