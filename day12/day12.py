import re
from itertools import combinations

"""
for each track combination track:
    combination
    touch-left
    touch-right

Then we should be able to combine these combinations into new sequences
    
"""

with open("input.txt") as f:
    rows = []
    for line in f.readlines():
        springs, groups_input = line.strip().split(" ")
        groups = list(map(int, groups_input.split(",")))
        rows.append((springs, groups))


def get_combinations(row):
    springs, groups = row
    spring_count = sum(groups)
    known_count = springs.count("#")
    unknowns = [i for i, g in enumerate(springs) if g == "?"]
    # print(known_count, unknowns)
    # print(list(combinations(unknowns, spring_count - known_count)))
    combs = [
        "".join(("#" if i in comb or c == "#" else ".") for i, c in enumerate(springs))
        for comb in combinations(unknowns, spring_count - known_count)
    ]
    # print(combs)
    combs_groups = [
        list(map(len, re.split("\.+", comb[comb.find("#") : comb.rfind("#") + 1])))
        for comb in combs
    ]
    valid_combs = [comb for comb in combs_groups if comb == groups]
    # print("A", valid_combs)
    res = len(valid_combs)
    print(res)
    return res
    # make string
    # see if it matches by splitting

rows = [
    (springs + "?" + springs + "?" + springs + "?" + springs + "?" + springs, groups + groups + groups + groups + groups)
    for springs, groups in rows
]
# print(rows)

# print(get_combinations(rows[1]))

valids = map(get_combinations, rows)
print(sum(valids))
