from collections import Counter


def parse_input(f):
    lines = f.readlines()
    pairs = []
    for line in lines:
        hand, bid = line.split(" ")
        pairs.append((hand, int(bid)))
    return pairs


def score_hand(hand, wildcards=False):
    if wildcards:
        hand_without_wildcards = "".join(c for c in hand if c != "J")
        jacks = hand.count("J")
        card_order = "AKQT98765432J"
    else:
        hand_without_wildcards = hand
        jacks = 0
        card_order = "AKQJT98765432"

    counts = Counter(hand_without_wildcards)
    values = sorted(counts.values(), reverse=True)

    if hand == "JJJJJ" or values[0] + jacks >= 5:
        # five of a kind
        combination_value = 6
    elif values[0] + jacks >= 4:
        # four of a kind
        combination_value = 5
    elif (values[0] + jacks >= 3 and values[1] >= 2) or (
        values[0] == 3 and values[1] + jacks >= 2
    ):
        # full house
        combination_value = 4
    elif values[0] + jacks >= 3:
        # three of a kind
        combination_value = 3
    elif values.count(2) == 2:
        # two pair
        combination_value = 2
    elif values[0] == 2 or jacks == 1:
        # one pair
        combination_value = 1
    else:
        # high card
        combination_value = 0

    hand_value = tuple(len(card_order) - card_order.index(card) for card in hand)
    return (combination_value, hand_value)


def solve(input, wildcards):
    sorted_input = sorted(input, key=lambda x: score_hand(x[0], wildcards=wildcards))
    total_winnings = sum((i + 1) * bid for i, (_, bid) in enumerate(sorted_input))
    return total_winnings


def solve_part1(input):
    return solve(input, wildcards=False)


def solve_part2(input):
    return solve(input, wildcards=True)
