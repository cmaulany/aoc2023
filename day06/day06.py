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
        winning_press_times = [
            press_time
            for press_time in range(time)
            if (time - press_time) * press_time > distance
        ]
        win_counts.append(len(winning_press_times))
    return prod(win_counts)


def solve_part1(input):
    return solve(input)


def solve_part2(input):
    times = [int("".join(map(str, input[0])))]
    distances = [int("".join(map(str, input[1])))]
    return solve((times, distances))
