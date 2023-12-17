def parse_input(f):
    return [list(map(int, line.strip())) for line in f.readlines()]


def get_neighbors(map, node, crucible_behavior):
    pos, dir, l = node

    min_move, max_move = crucible_behavior
    deltas = []
    if l < max_move:
        deltas.append((dir, l + 1))
    for d in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        if l < min_move or d == dir or d == (-dir[0], -dir[1]):
            continue
        deltas.append((d, 1))

    width = len(map[0])
    height = len(map)
    neighbors = [
        ((pos[0] + delta_dir[0], pos[1] + delta_dir[1]), delta_dir, delta_l)
        for delta_dir, delta_l in deltas
    ]
    return [
        (pos, dir, l)
        for pos, dir, l in neighbors
        if pos[0] >= 0 and pos[1] >= 0 and pos[0] < width and pos[1] < height
    ]


def find_path(map, crucible_behavior):
    start = ((0, 0), (1, 0), 0)
    open = [start]
    prev = {}
    val = {start: 0}
    while open:
        current = open.pop(0)
        for neighbor in get_neighbors(map, current, crucible_behavior):
            new_val = val[current] + map[neighbor[0][1]][neighbor[0][0]]
            if neighbor not in val or new_val < val[neighbor]:
                prev[neighbor] = current
                val[neighbor] = new_val
                open.append(neighbor)

    width = len(map[0])
    height = len(map)
    min_move = crucible_behavior[0]
    current = min(
        (
            (pos, dir, l)
            for pos, dir, l in val.keys()
            if pos == (width - 1, height - 1) and l >= min_move
        ),
        key=lambda node: val[node],
    )
    print(
        "MATCHES",
        [
            (pos, dir, l)
            for pos, dir, l in val.keys()
            if pos == (width - 1, height - 1) and l >= min_move
        ],
    )

    path = []
    while current != start:
        path.append(current)
        current = prev[current]

    return [p[0] for p in path]


def solve_part1(input):
    path = find_path(input, (1, 3))
    return sum(input[y][x] for x, y in path)


def solve_part2(input):
    path = find_path(input, (4, 10))
    return sum(input[y][x] for x, y in path)


# print(get_neighbors(input, ((0, 0), (1, 0), 0)))
# path = find_path(input)
# print("PATH", path)
# values = [input[y][x] for x, y in path]
# print(sum(values))

# for y in range(len(input)):
#     print("".join("#" if (x, y) in path else str(c) for x, c in enumerate(input[y])))

# TOo high 810
# too low
