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
        card_order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    else:
        hand_without_wildcards = hand
        jacks = 0
        card_order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

    counts = Counter(hand_without_wildcards)
    values = sorted(counts.values(), reverse=True)

    score = pow(13, 14)
    if hand == "JJJJJ" or values[0] + jacks >= 5:
        # "five of a kind"
        score *= 6
    elif values[0] + jacks >= 4:
        # "four of a kind"
        score *= 5
    elif (values[0] + jacks >= 3 and values[1] >= 2) or (
        values[0] == 3 and values[1] + jacks >= 2
    ):
        # "full house"
        score *= 4
    elif values[0] + jacks >= 3:
        # "three of a kind"
        score *= 3
    elif values.count(2) == 2:
        # "two pair"
        score *= 2
    elif values[0] == 2 or jacks == 1:
        # "one pair"
        score *= 1
    else:
        # "high card"
        score *= 0

    tie_breaker_score = sum(
        (12 - card_order.index(c)) * pow(13, (13 - i)) for i, c in enumerate(hand)
    )
    score += tie_breaker_score
    return score


def solve(input, wildcards):
    scores = [(score_hand(hand, wildcards=wildcards), bid) for hand, bid in input]
    scores.sort()

    total_winnings = sum((i + 1) * bid for i, (_, bid) in enumerate(scores))
    return total_winnings


def solve_part1(input):
    return solve(input, wildcards=False)


def solve_part2(input):
    return solve(input, wildcards=True)
