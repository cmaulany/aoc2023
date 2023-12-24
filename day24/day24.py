from itertools import combinations, permutations


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


def pos_at_t(a, t):
    pa, va = a
    pax, pay, paz = pa
    vax, vay, vaz = va
    return (pax + vax * t, pay + vay * t, paz + vaz * t)


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


def destroys_all_stones(stones, throw):
    for stone in stones:
        t = find_intersection_time(stone, throw)
        if t == None or t <= 0 or pos_at_t(stone, t) != pos_at_t(throw, t):
            return False
    return True


def create_vector(a, b, m, n):
    pos_at_1 = pos_at_t(a, m)
    pos_at_2 = pos_at_t(b, n)
    dx = (pos_at_2[0] - pos_at_1[0]) / (n - m)
    dy = (pos_at_2[1] - pos_at_1[1]) / (n - m)
    dz = (pos_at_2[2] - pos_at_1[2]) / (n - m)

    sx = pos_at_1[0] - dx * m
    sy = pos_at_1[1] - dy * m
    sz = pos_at_1[2] - dz * m
    return (sx, sy, sz), (dx, dy, dz)


def solve_part2(input):
    for i in range(1, 1000):
        print(i)
        # if i % 100 == 0 and j == i + 1:
        #     print(i, j)
        for j in range(i + 1, i + 10):
            for a, b in permutations(input, 2):
                throw = create_vector(a, b, i, j)
                if destroys_all_stones(input, throw):
                    return throw
    return None


# with open("example_input.txt") as f:
#     input = parse_input(f)

# r = create_vector(((20, 19, 15), (1, -5, -3)), ((18, 19, 22), (-1, -1, -2)), 1, 3)
# print("VEC", r)
# print("VECRES", try_throw(input, r))
