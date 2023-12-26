NORTH = (0, -1)
EAST = (1, 0)
SOUTH = (0, 1)
WEST = (-1, 0)


def get_start(map):
    position = next((line.index("S"), y) for y, line in enumerate(map) if "S" in line)
    x, y = position

    width = len(map[0]) * 2
    height = len(map) * 2
    n = y > 0 and map[y - 1][x] in "|7F"
    e = x < width - 1 and map[y][x + 1] in "-J7"
    s = y < height - 1 and map[y + 1][x] in "|LJ"
    w = x > 0 and map[y][x - 1] in "-LF"
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


def get_pipe_neighbors(map, position):
    px, py = position
    width = len(map[0])
    height = len(map)

    type = map[py][px]
    deltas = {
        "|": [NORTH, SOUTH],
        "-": [EAST, WEST],
        "L": [NORTH, EAST],
        "J": [NORTH, WEST],
        "7": [SOUTH, WEST],
        "F": [EAST, SOUTH],
    }[type]

    neighbors = [(px + dx, py + dy) for dx, dy in deltas]

    return [(px, py) for px, py in neighbors if 0 <= px < width and 0 <= py < height]


def find_path(map, start):
    open = [start]
    visited = set()
    prevs = {}
    while open:
        current = open.pop()
        if visited and current == start:
            break

        visited.add(current)
        for neighbor in get_pipe_neighbors(map, current):
            if neighbor != "." and (neighbor == start or neighbor not in visited):
                open.append(neighbor)
                prevs[neighbor] = current

    path = []
    current = start
    while current != start or not path:
        path.append(current)
        current = prevs[current]
    return path


expansions = {
    ".": [
        "...",
        "...",
        "...",
    ],
    "|": [
        ".#.",
        ".#.",
        ".#.",
    ],
    "-": [
        "...",
        "###",
        "...",
    ],
    "L": [
        ".#.",
        ".##",
        "...",
    ],
    "J": [
        ".#.",
        "##.",
        "...",
    ],
    "7": [
        "...",
        "##.",
        ".#.",
    ],
    "F": [
        "...",
        ".##",
        ".#.",
    ],
}


def expand(map):
    new_map = [""] * len(map) * 3
    for y, row in enumerate(map):
        for c in row:
            tile = expansions[c]
            for dy, cs in enumerate(tile):
                new_map[y * 3 + dy] += cs
    return new_map


def get_neighbors(map, position):
    x, y = position

    neighbors = [(x + dx, y + dy) for dx, dy in [NORTH, EAST, SOUTH, WEST]]

    width = len(map[0])
    height = len(map)
    return [
        (x, y)
        for x, y in neighbors
        if 0 <= x < width and 0 <= y < height and map[y][x] != "#"
    ]


def flood_fill(map, position=(0, 0)):
    open = [position]
    visited = set()
    while open:
        current = open.pop()

        visited.add(current)
        for neighbor in get_neighbors(map, current):
            if neighbor not in visited:
                open.append(neighbor)
    return visited


def solve_part1(input):
    map, start_position = input
    path = find_path(map, start_position)
    return len(path) // 2


def solve_part2(input):
    map, start_position = input
    width = len(map[0])
    height = len(map)

    loop = set(find_path(map, start_position))
    loop_map = [
        "".join(type if (x, y) in loop else "." for x, type in enumerate(line))
        for y, line in enumerate(map)
    ]
    expanded_outer_map = flood_fill(expand(loop_map))
    enclosed_positions = set(
        (x, y)
        for x in range(width)
        for y in range(height)
        if (x * 3, y * 3) not in expanded_outer_map
        and (x * 3 + 2, y * 3) not in expanded_outer_map
        and (x * 3, y * 3 + 2) not in expanded_outer_map
        and (x * 3 + 2, y * 3 + 2) not in expanded_outer_map
    )
    return len(enclosed_positions)
