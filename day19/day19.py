from math import prod


def parse_input(f):
    workflows_input, parts_input = f.read().split("\n\n")
    lines = workflows_input.split("\n")
    workflows = {}
    for line in lines:
        name, action = line.split("{")
        *items, tail = action[:-1].split(",")
        steps = [
            (
                item[0],
                item[1],
                int(item[2 : item.index(":")]),
                item[item.index(":") + 1 :],
            )
            for item in items
        ]
        workflows[name] = (steps, tail)

    parts = []
    for part_input in parts_input.split("\n"):
        part_input = {
            val.split("=")[0]: int(val.split("=")[1])
            for val in part_input[1:-1].split(",")
        }
        parts.append(part_input)
    return workflows, parts


def run_workflow(workflows, name, part):
    steps, fallback = workflows[name]
    for step in steps:
        cat, op, n, next = step
        if part[cat] > n if op == ">" else part[cat] < n:
            if next in "AR":
                return next
            return run_workflow(workflows, next, part)
    return fallback if fallback in "AR" else run_workflow(workflows, fallback, part)


def run_ranges(workflows, name, step_i, ranges):
    if name == "R" or any(end - start <= 0 for start, end in ranges.values()):
        return 0

    if name == "A":
        return prod((end - start + 1) for start, end in ranges.values())

    steps, fallback = workflows[name]
    if step_i >= len(steps):
        return run_ranges(workflows, fallback, 0, ranges)

    step = steps[step_i]
    cat, op, n, next = step
    start, end = ranges[cat]

    valid_count = 0
    if op == ">":
        valid_count += run_ranges(
            workflows,
            name,
            step_i + 1,
            {
                **ranges,
                cat: (start, min(end, n)),
            },
        )
        valid_count += run_ranges(
            workflows,
            next,
            0,
            {**ranges, cat: (max(start, n + 1), end)},
        )
    if op == "<":
        valid_count += run_ranges(
            workflows,
            next,
            0,
            {**ranges, cat: (start, min(end, n - 1))},
        )
        valid_count += run_ranges(
            workflows,
            name,
            step_i + 1,
            {**ranges, cat: (max(start, n), end)},
        )
    return valid_count


def solve_part1(input):
    workflows, parts = input
    res = [
        sum(part.values()) if run_workflow(workflows, "in", part) == "A" else 0
        for part in parts
    ]
    return sum(res)


def solve_part2(input):
    workflows, parts = input
    return run_ranges(
        workflows,
        "in",
        0,
        {
            "x": (1, 4000),
            "m": (1, 4000),
            "a": (1, 4000),
            "s": (1, 4000),
        },
    )
