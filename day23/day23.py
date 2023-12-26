UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)


def parse_input(f):
    return [line.strip() for line in f.readlines()]


def get_neighbors(grid, pos):
    x, y = pos

    c = grid[y][x]
    if c == "^":
        deltas = [UP]
    elif c == ">":
        deltas = [RIGHT]
    elif c == "v":
        deltas = [DOWN]
    elif c == "<":
        deltas = [LEFT]
    else:
        deltas = [UP, RIGHT, DOWN, LEFT]

    width = len(grid[0])
    height = len(grid)
    return [
        (nx, ny)
        for nx, ny in [(x + dx, y + dy) for dx, dy in deltas]
        if 0 <= nx < width and 0 <= ny < height
        if grid[ny][nx] != "#"
    ]


def find_next_crossing(grid, current, parent=None):
    visited = set([parent] if parent else [])
    neighbors = [current]
    i = 0
    while len(neighbors) == 1:
        visited.add(current)
        current = neighbors[0]
        neighbors = [n for n in get_neighbors(grid, current) if n not in visited]
        i += 1
    return (i, current)


def to_graph(grid):
    return {
        (x, y): [
            find_next_crossing(grid, neighbor, (x, y))
            for neighbor in get_neighbors(grid, (x, y))
        ]
        for y, line in enumerate(grid)
        for x, c in enumerate(line)
        if c != "#" and len(get_neighbors(grid, (x, y))) != 2
    }


def get_all_paths(grid, start, end):
    paths = []
    open = [(start, [start])]
    while open:
        pos, path = open.pop()
        for neighbor in get_neighbors(grid, pos):
            if neighbor == end:
                paths.append(path + [neighbor])
            elif neighbor not in path:
                open.append((neighbor, path + [neighbor]))
    return paths


def get_all_paths(graph, start, end):
    paths = []
    open = [(start, [start], 0)]
    while open:
        node, path, cost = open.pop()
        for ncost, neighbor in graph[node]:
            if neighbor == end:
                paths.append((path + [neighbor], cost + ncost))
            elif neighbor not in path:
                open.append((neighbor, path + [neighbor], cost + ncost))
    return paths


def solve(grid):
    graph = to_graph(grid)
    start = (1, 0)
    end = (len(grid[0]) - 2, len(grid) - 1)
    paths = get_all_paths(graph, start, end)
    _, weight = max(paths, key=lambda x: x[1])
    return weight


def solve_part1(input):
    return solve(input)


def solve_part2(input):
    grid = ["".join("." if c in "^>v<" else c for c in line) for line in input]
    return solve(grid)
