from itertools import combinations
import sympy as sym


def parse_input(f):
    return [
        (
            tuple(map(int, (p for p in line.split("@")[0].strip().split(",")))),
            tuple(map(int, (p for p in line.split("@")[1].strip().split(",")))),
        )
        for line in f.readlines()
    ]


def find_intersection(a, b):
    (pax, pay, _), (vax, vay, _) = a
    (pbx, pby, _), (vbx, vby, _) = b

    div = (vay * vbx) - (vax * vby)
    if div == 0:
        return None

    t = (vax * (pby - pay) - vay * (pbx - pax)) / div
    return (pbx + vbx * t, pby + vby * t)


def solve_part1(input, min_bound, max_bound):
    c = 0
    for a, b in combinations(input, 2):
        intersection = find_intersection(b, a)
        if intersection == None:
            continue
        x, y = intersection
        (ax, ay, _), (vax, vay, _) = a
        (bx, by, _), (vbx, vby, _) = b
        if (
            min_bound <= x <= max_bound
            and min_bound <= y <= max_bound
            and (x - ax) / vax > 0
            and (y - ay) / vay > 0
            and (x - bx) / vbx > 0
            and (y - by) / vby > 0
        ):
            c += 1
    return c


def solve_part2(input):
    a, b, c, *_ = input
    (ax, ay, az), (vax, vay, vaz) = a
    (bx, by, bz), (vbx, vby, vbz) = b
    (cx, cy, cz), (vcx, vcy, vcz) = c

    rx, ry, rz = sym.symbols("pmx, pmy, pmz")
    vrx, vry, vrz = sym.symbols("vmx, vmy, vmz")
    t, u, v = sym.symbols("t, u, v")

    solution = sym.solve(
        (
            rx + vrx * t - ax - vax * t,
            ry + vry * t - ay - vay * t,
            rz + vrz * t - az - vaz * t,
            rx + vrx * u - bx - vbx * u,
            ry + vry * u - by - vby * u,
            rz + vrz * u - bz - vbz * u,
            rx + vrx * v - cx - vcx * v,
            ry + vry * v - cy - vcy * v,
            rz + vrz * v - cz - vcz * v,
        )
    )[0]
    return solution[rx] + solution[ry] + solution[rz]
