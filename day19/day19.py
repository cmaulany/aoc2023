def parse_input(f):
    workflows, parts = f.read().split("\n\n")
    lines = workflows.split("\n")
    wfs = {}
    for line in lines:
        name, rest = line.split("{")
        *first, last = rest[:-1].split(",")
        steps = [
            (a[0], a[1], int(a[2 : a.index(":")]), a[a.index(":") + 1 :]) for a in first
        ]
        wfs[name] = (steps, last)

    ps = []
    for part in parts.split("\n"):
        x, m, a, s = [int(p.split("=")[1]) for p in part[1:-1].split(",")]
        ps.append({"x": x, "m": m, "a": a, "s": s})
    return wfs, ps


def run_workflow(workflows, name, part):
    steps, fallback = workflows[name]
    for step in steps:
        cat, op, n, next = step
        if part[cat] > n if op == ">" else part[cat] < n:
            if next in "AR":
                return next
            return run_workflow(workflows, next, part)
    return fallback if fallback in "AR" else run_workflow(workflows, fallback, part)


with open("input.txt") as f:
    input = parse_input(f)


workflows, parts = input
print(workflows)
print(parts)

res = [
    sum(part.values()) if run_workflow(workflows, "in", part) == "A" else 0
    for part in parts
]
print(sum(res))
