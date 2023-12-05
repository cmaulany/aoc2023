from functools import reduce
from itertools import chain


def parse_input(stream):
    seeds_input, *maps_input = stream.read().split("\n\n")
    seeds = list(map(int, seeds_input.split(":")[1].strip().split(" ")))

    cats = []
    for map_input in maps_input:
        _, *lines = map_input.split("\n")
        cat = [list(map(int, line.split(" "))) for line in lines]
        cat.sort(key=lambda x: x[1])
        cats.append(cat)

    return seeds, cats


def map_one(n, maps):
    for dst_start, src_start, l in maps:
        if n >= src_start and n < src_start + l:
            return n + dst_start - src_start
    return n


def merge_ranges(ranges):
    merged = []
    for range in sorted(ranges):
        if merged and merged[-1][1] >= range[0]:
            merged[-1] = (merged[-1][0], max(range[1], merged[-1][1]))
        else:
            merged.append(range)
    return merged


def map_range(range, maps):
    next_ranges = []
    start, end = range

    n = start
    for dst_start, src_start, l in maps:
        if n < src_start:
            next_n = min(end, src_start)
            next_ranges.append((n, next_n))
            n = next_n

        if n > src_start + l:
            continue

        next_start = n + dst_start - src_start
        next_end = min(src_start + l, end) + dst_start - src_start
        next_range = (next_start, next_end)
        if next_end > next_start:
            next_ranges.append(next_range)
        n = min(n + l, src_start + l)

    if n < end:
        next_ranges.append((n, end))

    return merge_ranges(next_ranges)


def map_ranges(ranges, maps):
    next_ranges = merge_ranges(
        next_range for range in ranges for next_range in map_range(range, maps)
    )
    return next_ranges


def solve_part1(input):
    initial_seeds, cats = input

    final_seeds = [reduce(map_one, cats, seed) for seed in initial_seeds]

    return min(final_seeds)


def solve_part2(input):
    ranges_cfg, cats = input

    initial_ranges = [
        (ranges_cfg[i], ranges_cfg[i] + ranges_cfg[i + 1])
        for i in range(0, len(ranges_cfg), 2)
    ]
    final_ranges = reduce(map_ranges, cats, initial_ranges)

    return min(final_ranges)[0]
