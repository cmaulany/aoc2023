def parse_input(f):
    return [line.strip() for line in f.readlines()]

s_shadow = "7"


def get_neighbors(map, position):
    px, py = position
    width = len(map[0])
    height = len(map)

    c = map[py][px]

    if c == "S":
        deltas = [(0, 1)]
    elif c == "|":
        deltas = [(0, -1), (0, 1)]
    elif c == "-":
        deltas = [(-1, 0), (1, 0)]
    elif c == "L":
        deltas = [(0, -1), (1, 0)]
    elif c == "J":
        deltas = [(-1, 0), (0, -1)]
    elif c == "7":
        deltas = [(-1, 0), (0, 1)]
    elif c == "F":
        deltas = [(1, 0), (0, 1)]

    neighbors = [(px + dx, py + dy) for dx, dy in deltas]

    return [
        (px, py)
        for px, py in neighbors
        if px >= 0 and px < width and py >= 0 and py < height and map[py][px] != "."
    ]


def get_tiny_neighbors(map, position):
    px, py = position
    width = len(map[0])
    height = len(map)

    c = map[int(py / 2)][int(px / 2)]
    if px % 2 == 0 and py % 2 == 0:
        d = "A"
    elif py % 2 == 0:
        d = "B"
    elif px % 2 == 0:
        d = "C"
    else:
        d = "D"

    if c == "S":
        c = s_shadow

    if c == ".":
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    elif c == "|":
        if d == "A" or d == "C":
            deltas = [(0, -1), (0, 1), (-1, 0)]
        else:
            deltas = [(0, -1), (0, 1), (1, 0)]
    elif c == "-":
        if d == "A" or d == "B":
            deltas = [(-1, 0), (1, 0), (0, -1)]
        else:
            deltas = [(-1, 0), (1, 0), (0, 1)]
    elif c == "L":
        if d == "A":
            deltas = [(-1, 0), (0, -1), (0, 1)]
        elif d == "B":
            deltas = [(0, -1), (1, 0)]
        elif d == "C":
            deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        else:
            deltas = [(-1, 0), (1, 0), (0, 1)]
    elif c == "J":
        if d == "A":
            deltas = [(-1, 0), (0, -1)]
        elif d == "B":
            deltas = [(0, -1), (1, 0), (0, 1)]
        elif d == "C":
            deltas = [(-1, 0), (1, 0), (0, 1)]
        else:
            deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    elif c == "7":
        if d == "A":
            deltas = [(-1, 0), (1, 0), (0, -1)]
        elif d == "B":
            deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        elif d == "C":
            deltas = [(-1, 0), (0, 1)]
        else:
            deltas = [(0, -1), (1, 0), (0, 1)]
    elif c == "F":
        if d == "A":
            deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        elif d == "B":
            deltas = [(-1, 0), (1, 0), (0, -1)]
        elif d == "C":
            deltas = [(-1, 0), (0, -1), (0, 1)]
        else:
            deltas = [(1, 0), (0, 1)]

    neighbors = [(px + dx, py + dy) for dx, dy in deltas]

    return [
        (px, py)
        for px, py in neighbors
        if px >= 0 and px < width * 2 and py >= 0 and py < height * 2
    ]


# A | B
# - + -
# C | D


def flood_fill(map):
    open = [(0, 0)]
    visited = set()
    while open:
        current = open.pop()
        visited.add(current)
        neighbors = get_tiny_neighbors(map, current)
        new_neighbors = [
            neighbor
            for neighbor in neighbors
            if neighbor not in visited
        ]
        for neighbor in new_neighbors:
            open.append(neighbor)

    lines = []
    for y in range(len(map)):
        line = []
        for x in range(len(map[0])):
            coords = [
                (x * 2, y * 2),
                (x * 2 + 1, y * 2),
                (x * 2, y * 2 + 1),
                (x * 2 + 1, y * 2 + 1)
            ]
            if all(coord in visited for coord in coords):
                line.append("O")
            else:
                line.append("I")
        lines.append("".join(line))
        
    return lines



def find_path(map, start):
    open = [start]
    visited = set()
    prevs = {}
    while open:
        current = open.pop()
        if visited and current == start:
            break

        neighbors = get_neighbors(map, current)
        new_neighbors = [
            neighbor
            for neighbor in neighbors
            if neighbor == start or neighbor not in visited
        ]
        for neighbor in new_neighbors:
            open.append(neighbor)
            if not neighbor in current:
                # print("A", neighbor, current)
                prevs[neighbor] = current

        visited.add(current)

    path = []
    current = start
    while not path or current != start:
        path.append(current)
        current = prevs[current]

    return path


def solve_part1(input):
    start = next((line.index("S"), y) for y, line in enumerate(input) if "S" in line)
    path = find_path(input, start)
    return len(path) // 2


def solve_part2(input):
    start = next((line.index("S"), y) for y, line in enumerate(input) if "S" in line)
    path = set(find_path(input, start))
    map = [
        "".join(c if (x, y) in path else "." for x, c in enumerate(line))
        for y, line in enumerate(input)
    ]
    ff = flood_fill(map)
    resmap = [
        "".join("O" if (x, y) in path else c for x, c in enumerate(line))
        for y, line in enumerate(ff)
    ]
    r = "\n".join(resmap).count("I")
    return r

# solve_part1(input)
# solve_part2(input)
