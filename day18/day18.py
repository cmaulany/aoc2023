from functools import reduce

with open("example_input.txt") as f:
    input = []
    for line in f.readlines():
        dir, l, c = line.strip().split(" ")
        input.append((dir, int(l), c[1:-1]))


def dig(grid, position, command):
    dir, l, c = command
    d = {
        "U": (0, -1),
        "R": (1, 0),
        "D": (0, 1),
        "L": (-1, 0),
    }[dir]
    for _ in range(l):
        position = (position[0] + d[0], position[1] + d[1])
        grid[position] = c
    return grid, position


def do_all(grid, position, commands):
    return reduce(
        lambda acc, command: dig(acc[0], acc[1], command), commands, (grid, position)
    )


new_input = []
for _, _, c in input:
    print(c)
    i = int(c[1:6], 16)
    d = {"0": "R", "1": "D", "2": "L", "3": "U"}[c[6]]
    new_input.append((d, i, ""))
grid, position = do_all({}, (0, 0), new_input)


def get_inner(grid):
    xs = list(map(lambda x: x[0], grid.keys()))
    ys = list(map(lambda x: x[1], grid.keys()))
    min_x = min(xs) - 1
    min_y = min(ys) - 1
    max_x = max(xs) + 2
    max_y = max(ys) + 2

    filled = set()
    open = [(min_x, min_y)]
    while open:
        current = open.pop()
        neighbors = [
            (current[0] + d[0], current[1] + d[1])
            for d in [(0, -1), (1, 0), (0, 1), (-1, 0)]
        ]
        valid_neighbors = [
            neighbor
            for neighbor in neighbors
            if neighbor not in grid
            and neighbor not in filled
            and neighbor[0] >= min_x
            and neighbor[0] < max_x
            and neighbor[1] >= min_y
            and neighbor[1] < max_y
        ]
        for neighbor in valid_neighbors:
            filled.add(neighbor)
            open.append(neighbor)

    return set(
        [
            (x, y)
            for x in range(min_x, max_x)
            for y in range(min_y, max_y)
            if (x, y) not in filled and (x, y) not in grid
        ]
    )


def draw(grid):
    xs = list(map(lambda x: x[0], grid))
    ys = list(map(lambda x: x[1], grid))
    min_x = min(xs)
    min_y = min(ys)
    max_x = max(xs)
    max_y = max(ys)
    for y in range(min_y, max_y + 1):
        print("".join("#" if (x, y) in grid else "." for x in range(min_x, max_x + 1)))


print(len(grid))

inner = get_inner(grid)
print(len(inner))

print(len(inner) + len(grid))