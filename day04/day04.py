import re
from functools import cache


def parse_input(stream):
    input = []
    for line in stream.readlines():
        card, rest = line.split(":")
        card_id = int(re.split(r" +", card)[1])
        winners_input, mine_input = rest.split("|")
        winners = map(lambda x: int(x.strip()), re.split(r" +", winners_input.strip()))
        mine = map(lambda x: int(x.strip()), re.split(r" +", mine_input.strip()))
        input.append((card_id, list(winners), list(mine)))
    return input


def scratch(input, card_id):
    _, winning_ns, ns = input[card_id - 1]
    correct_ns = [n for n in ns if n in winning_ns]
    wins = len(correct_ns)
    return wins


def solve_part1(input):
    card_ids = [card[0] for card in input]
    results = map(lambda card_id: scratch(input, card_id), card_ids)
    score = sum(2 ** (wins - 1) for wins in results if wins > 0)
    return score


def solve_part2(input):
    @cache
    def cached_scratch(id):
        return scratch(input, id)

    unscratched_card_ids = [card[0] for card in input]
    scratched_card_ids = []
    while unscratched_card_ids:
        card_id = unscratched_card_ids.pop()
        wins = cached_scratch(card_id)
        for n in range(wins):
            unscratched_card_ids.append(card_id + n + 1)
        scratched_card_ids.append(card_id)
    return len(scratched_card_ids)
