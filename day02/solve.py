from itertools import groupby
from math import prod


def parse_input():
    with open("input.txt") as stream:
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


def solve(input):
    valid_game_ids = []
    powers = []
    for game in input:
        id, reveals = game

        pairs = sorted(
            [comb for reveal in reveals for comb in reveal], key=lambda x: x[1]
        )
        bycolor = groupby(pairs, key=lambda x: x[1])

        required_cubes = {}
        for color, pairs in bycolor:
            n = max(n for n, _ in pairs)
            required_cubes[color] = n

        game_is_valid = all(n <= available_cubes[color] for color, n in required_cubes.items())

        if game_is_valid:
            valid_game_ids.append(id)

        power = prod(required_cubes.values())
        powers.append(power)

    power_sum = sum(powers)
    valid_game_sum = sum(valid_game_ids)
    print(power_sum)
    print(valid_game_sum)


input = parse_input()
solve(input)
