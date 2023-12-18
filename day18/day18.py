def parse_input(f):
    input = []
    for line in f.readlines():
        dir, l, c = line.strip().split(" ")
        input.append((dir, int(l), c[1:-1]))
    return input


def pairwise(list):
    return ((list[i], list[i + 1]) for i in range(len(list) - 1))


def get_edges(commands, start=(0, 0)):
    edges = []
    end = start
    for command in commands:
        dir, l = command
        d = {
            "U": (0, -1),
            "R": (1, 0),
            "D": (0, 1),
            "L": (-1, 0),
        }[dir]
        start = end
        end = (start[0] + d[0] * l, start[1] + d[1] * l)
        edges.append((start, end))
    return edges


def get_surface(edges):
    h_edges = [(start, end) for start, end in edges if start[1] == end[1]]
    v_edges = [(start, end) for start, end in edges if start[0] == end[0]]
    ys = list(sorted(set(start[1] for start, _ in h_edges)))

    # calculate surface area
    a = 0
    for y0, y1 in pairwise(ys):
        xs = (
            sx
            for (sx, sy), (_, ey) in v_edges
            if y0 >= min(sy, ey) and y0 < max(sy, ey)
        )
        xs = list(sorted(set(xs)))
        for x in range(0, len(xs), 2):
            x0 = xs[x]
            x1 = xs[x + 1]
            a += (y1 - y0) * (x1 - x0)

    # expand by 0.5 tile
    a += 1
    a += sum(abs(ex - sx) / 2 for (sx, _), (ex, _) in h_edges)
    a += sum(abs(ey - sy) / 2 for (_, sy), (_, ey) in v_edges)
    return int(a)


def color_to_commands(colors):
    commands = []
    for color in colors:
        dir = {"0": "R", "1": "D", "2": "L", "3": "U"}[color[6]]
        l = int(color[1:6], 16)
        commands.append((dir, l))
    return commands


def solve_part1(input):
    commands = [row[:2] for row in input]
    edges = get_edges(commands)
    return get_surface(edges)


def solve_part2(input):
    commands = color_to_commands(row[2] for row in input)
    edges = get_edges(commands)
    return get_surface(edges)
