def parse_input(f):
    bricks = []
    for line in f.readlines():
        s, e = line.strip().split("~")
        bricks.append(
            (
                tuple(map(int, s.split(","))),
                tuple(map(int, e.split(","))),
            )
        )
    return bricks


def is_supporting(low, high):
    lsx, lsy, _ = low[0]
    lex, ley, lez = low[1]
    hsx, hsy, hsz = high[0]
    hex, hey, _ = high[1]

    return (
        lez + 1 == hsz
        and (
            lsx <= hsx <= lex
            or lsx <= hex <= lex
            or hsx <= lsx <= hex
            or hsx <= lex <= hex
        )
        and (
            lsy <= hsy <= ley
            or lsy <= hey <= ley
            or hsy <= lsy <= hey
            or hsy <= ley <= hey
        )
    )


def find_above(bricks, brick):
    _, e = brick
    _, _, ez = e

    above = [b for b in bricks if b[0][2] == ez + 1]
    return [other for other in above if is_supporting(brick, other)]


def find_below(bricks, brick):
    s, _ = brick
    _, _, sz = s

    below = [b for b in bricks if b[1][2] == sz - 1]
    return [other for other in below if is_supporting(other, brick)]


def settle(bricks):
    next_bricks = []
    for brick in sorted(bricks, key=lambda x: x[0][2]):
        s, e = brick
        sx, sy, sz = s
        ex, ey, ez = e

        nsz = next(
            (
                a[1][2] + 1
                for a in next_bricks
                if find_below(
                    next_bricks,
                    ((sx, sy, a[1][2] + 1), (ex, ey, a[1][2] + 1 + ez - sz)),
                )
            ),
            1,
        )
        nez = nsz + ez - sz
        next_bricks.append(((sx, sy, nsz), (ex, ey, nez)))
        next_bricks.sort(key=lambda x: x[1][2], reverse=True)

    return next_bricks


def find_free_bricks(bricks):
    free_bricks = []
    for i, brick in enumerate(bricks):
        rest = bricks[:i] + bricks[i + 1 :]
        if all(find_below(rest, supporting) for supporting in find_above(rest, brick)):
            free_bricks.append(brick)
    return free_bricks


def find_falling_bricks(bricks, dis_brick):
    bricks = set(bricks)
    removed = []
    open = [dis_brick]
    while open:
        current = open.pop()
        if current not in bricks:
            continue
        bricks.remove(current)
        removed.append(current)

        supporting = [
            a for a in find_above(bricks, current) if not find_below(bricks, a)
        ]
        for sup in supporting:
            open.append(sup)
    return removed


def solve_part1(input):
    settled = settle(input)
    free_bricks = find_free_bricks(settled)
    return len(free_bricks)


def solve_part2(input):
    settled = settle(input)
    free_bricks = find_free_bricks(settled)
    sup_bricks = set(settled) - set(free_bricks)
    chain_reactions = [
        find_falling_bricks(settled, sup_brick) for sup_brick in sup_bricks
    ]
    return sum(len(chain_reaction) - 1 for chain_reaction in chain_reactions)
