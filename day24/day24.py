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


def find_intersection_time(a, b):
    pa, va = a
    pax, pay, _ = pa
    vax, vay, _ = va
    pb, vb = b
    pbx, pby, _ = pb
    vbx, vby, _ = vb

    div = (vay * vbx) - (vax * vby)
    if div == 0:
        return None
    return (vax * (pby - pay) - vay * (pbx - pax)) / div


def find_intersection(a, b):
    pb, vb = b
    pbx, pby, _ = pb
    vbx, vby, _ = vb
    u = find_intersection_time(a, b)
    if u == None or u <= 0:
        return None
    pos = (pbx + vbx * u, pby + vby * u)
    return pos


def solve_part1(input, min_bound, max_bound):
    c = 0
    for a, b in combinations(input, 2):
        inter_a = find_intersection(b, a)
        inter_b = find_intersection(a, b)
        if (
            inter_a != None
            and inter_b != None
            and inter_a[0] >= min_bound
            and inter_a[0] <= max_bound
            and inter_b[1] >= min_bound
            and inter_b[1] <= max_bound
        ):
            c += 1
    return c


def solve_part2(input):
    a, b, c, *_ = input
    (pax, pay, paz), (vax, vay, vaz) = a
    (pbx, pby, pbz), (vbx, vby, vbz) = b
    (pcx, pcy, pcz), (vcx, vcy, vcz) = c

    pmx = sym.Symbol("pmx")
    pmy = sym.Symbol("pmy")
    pmz = sym.Symbol("pmz")
    vmx = sym.Symbol("vmx")
    vmy = sym.Symbol("vmy")
    vmz = sym.Symbol("vmz")
    t = sym.Symbol("t")
    u = sym.Symbol("u")
    v = sym.Symbol("v")

    solution = sym.solve(
        (
            pmx + vmx * t - pax - vax * t,
            pmy + vmy * t - pay - vay * t,
            pmz + vmz * t - paz - vaz * t,
            pmx + vmx * u - pbx - vbx * u,
            pmy + vmy * u - pby - vby * u,
            pmz + vmz * u - pbz - vbz * u,
            pmx + vmx * v - pcx - vcx * v,
            pmy + vmy * v - pcy - vcy * v,
            pmz + vmz * v - pcz - vcz * v,
        )
    )[0]
    return solution[pmx] + solution[pmy] + solution[pmz]
