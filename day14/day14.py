from itertools import cycle


def parse_input(f):
    return [line.strip() for line in f.readlines()]


NORTH = (0, -1)
WEST = (-1, 0)
SOUTH = (0, 1)
EAST = (1, -0)

with open("input.txt") as f:
    input = parse_input(f)

print(input)

round_rocks = tuple(
    (x, y) for y, line in enumerate(input) for x, c in enumerate(line) if c == "O"
)
cube_rocks = tuple(
    (x, y) for y, line in enumerate(input) for x, c in enumerate(line) if c == "#"
)

width = len(input[0])
height = len(input)


def slide_one(blocked, position, dir):
    next_position = (position[0] + dir[0], position[1] + dir[1])
    while (
        next_position not in blocked
        and next_position[0] >= 0
        and next_position[1] >= 0
        and next_position[0] < width
        and next_position[1] < height
    ):
        position = next_position
        next_position = (position[0] + dir[0], position[1] + dir[1])
    return position


def slide(world, dir):
    round_rocks, cube_rocks = world
    round_rocks = tuple(
        sorted(round_rocks, key=lambda rock: rock[0] * -dir[0] + rock[1] * -dir[1])
    )
    for i in range(len(round_rocks)):
        rock = round_rocks[i]
        rest = round_rocks[:i] + round_rocks[i + 1 :]
        new_pos = slide_one(set(cube_rocks + rest), rock, dir)
        round_rocks = round_rocks[:i] + (new_pos,) + round_rocks[i + 1 :]

    return round_rocks, cube_rocks


print("ROUND", round_rocks)
print("CUBE", cube_rocks)
world = round_rocks, cube_rocks
# print(new[0])


# ----- | -- | -- | -- | -

known = {}
i = 0
target = 1000000000
target = 1
# i = 12
found_cycle = False
for dir in cycle([NORTH, WEST, SOUTH, EAST]):
    # print(world, dir)
    if i % 1 == 0:
        print(i, dir)
    if i == target:
        break

    if not found_cycle and (world, dir) in known:
        size = i - known[(world[0], dir)]
        print("CYCLE!", i, "to", known[(world, dir)], "size", size)
        while i + size < target:
            i += size
        found_cycle = True
    else:
        known[(world[0], dir)] = i

    world = slide(world, dir)
    i += 1


for y in range(height):
    print(
        "".join(
            "O" if (x, y) in world[0] else ("#" if (x, y) in world[1] else ".")
            for x in range(width)
        )
    )

weights = [height - y for _, y in world[0]]
print(sum(weights))
