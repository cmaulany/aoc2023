from itertools import groupby
from math import prod


def parse_input(stream):
    lines = stream.readlines()
    games = []
    for line in lines:
        id_input, reveals_input = line.split(":")
        id = int(id_input.split(" ")[1])

        reveals = []
        for reveal_input in reveals_input.split(";"):
            reveal = []
            for pair_input in reveal_input.strip().split(","):
                n, color = pair_input.strip().split(" ")
                reveal.append((int(n), color))
            reveals.append(reveal)

        games.append((id, reveals))
    return games


available_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def solve(input, score_game):
    scores = []
    for id, reveals in input:
        pairs = sorted(
            [pair for reveal in reveals for pair in reveal], key=lambda x: x[1]
        )
        bycolor = groupby(pairs, key=lambda x: x[1])
        required_cubes = {color: max(n for n, _ in pairs) for color, pairs in bycolor}

        scores.append(score_game(id, required_cubes))

    return sum(scores)


def score_game_part1(id, required_cubes):
    game_is_valid = all(
        n <= available_cubes[color] for color, n in required_cubes.items()
    )
    return id if game_is_valid else 0


def score_game_part2(_, required_cubes):
    return prod(required_cubes.values())


def solve_part1(input):
    return solve(input, score_game_part1)


def solve_part2(input):
    return solve(input, score_game_part2)
