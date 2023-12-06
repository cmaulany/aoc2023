from math import prod
import re


def parse_input(f):
    times_input, distances_input = f.readlines()
    times = list(map(int, re.split(r" +", times_input)[1:]))
    distances = list(map(int, re.split(r" +", distances_input)[1:]))
    return times, distances


def solve(input):
    times, distances = input
    win_counts = []
    for time, distance in zip(times, distances):
        ds = [(time - press_time) * press_time for press_time in range(time)]
        beaters = [d for d in ds if d > distance]
        win_counts.append(len(beaters))
    return prod(win_counts)


def solve_part1(input):
    return solve(input)


def solve_part2(input):
    times = [int("".join(map(str, input[0])))]
    distances = [int("".join(map(str, input[1])))]
    return solve((times, distances))
