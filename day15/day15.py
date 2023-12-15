import re


def parse_input(f):
    return f.read().split(",")


def hash(string):
    value = 0
    for c in string:
        value += ord(c)
        value *= 17
        value %= 256
    return value


def do_step(boxes, step):
    label, focal_length = re.split(r"[=-]", step)
    box = boxes[hash(label)]
    existing_i = next((i for i, lens in enumerate(box) if lens.startswith(label)), -1)
    if "=" in step:
        name = f"{label} {focal_length}"
        if existing_i >= 0:
            box[existing_i] = name
        else:
            box.append(name)
    elif existing_i >= 0:
        box.pop(existing_i)


def solve_part1(input):
    return sum(map(hash, input))


def solve_part2(input):
    boxes = {i: [] for i in range(256)}
    for step in input:
        do_step(boxes, step)

    fpowers = [
        (box_i + 1) * (lens_i + 1) * int(lens.split(" ")[1])
        for box_i, box in boxes.items()
        for lens_i, lens in enumerate(box)
    ]
    return sum(fpowers)
