def parse_input(f):
    return [plane.split() for plane in f.read().split("\n\n")]


def find_refelctions(plane):
    width = len(plane[0])
    height = len(plane)

    reflections = []
    for x in range(1, width):
        w = min(x, width - x)
        if all(line[x - w : x] == "".join(reversed(line[x : x + w])) for line in plane):
            reflections.append(("x", x))
    for y in range(1, height):
        h = min(y, height - y)
        if plane[y - h : y] == list(reversed(plane[y : y + h])):
            reflections.append(("y", y))
    return reflections


def find_reflection(plane):
    return find_refelctions(plane)[0]


def find_smudge_reflection(plane):
    reflection = find_reflection(plane)
    for y, line in enumerate(plane):
        for x, c in enumerate(line):
            new_c = "#" if c == "." else "."
            new_line = line[:x] + new_c + line[x + 1 :]
            new_plane = plane[:y] + [new_line] + plane[y + 1 :]

            new_reflection = next(
                (
                    new_reflection
                    for new_reflection in find_refelctions(new_plane)
                    if new_reflection != reflection
                ),
                None,
            )
            if new_reflection:
                return new_reflection


def get_value(reflection):
    axis, i = reflection
    return i if axis == "x" else i * 100


def solve_part1(input):
    reflections = map(find_reflection, input)
    values = map(get_value, reflections)
    return sum(values)


def solve_part2(input):
    reflections = map(find_smudge_reflection, input)
    values = map(get_value, reflections)
    return sum(values)
