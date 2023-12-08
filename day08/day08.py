from itertools import cycle
from math import prod


def parse_input(f):
    input = f.read()
    seq_input, nodes_input = input.split("\n\n")

    nodes = {line[0:3]: (line[7:10], line[12:15]) for line in nodes_input.split("\n")}
    return (seq_input.strip(), nodes)


def steps_to_node(seq, nodes, start_node_name, stop_condition):
    node_name = start_node_name
    for i, ins in enumerate(cycle(seq)):
        index = 0 if ins == "L" else 1
        node_name = nodes[node_name][index]
        if stop_condition(i + 1, node_name):
            return i + 1


def solve_part1(input):
    seq, nodes = input

    def stop_condition(_, node_name):
        return node_name == "ZZZ"

    return steps_to_node(seq, nodes, "AAA", stop_condition)


def solve_part2(input):
    """
    After analyzing the input we learned that we always find a "..Z" 
    node after an amount of steps that is a multiple of the sequence length.

    Afterwards we enter a cycle where we end up at the same (end) node
    after exactly the same amount of steps. 

    When expressing these periods as the amount of full sequence cycles,
    we find that these periods are all prime.

    Therefore, we can find when the cycles align by multiplying these periods
    together, followed by multiplying by the sequence length to get the total
    amount of steps.
    """
    seq, nodes = input
    start_node_names = [name for name in nodes.keys() if name[2] == "A"]

    def stop_condition(i, node_name):
        return i % len(seq) == 0 and node_name[2] == "Z"

    periods = [
        steps_to_node(seq, nodes, name, stop_condition) / len(seq)
        for name in start_node_names
    ]

    steps = prod(periods) * len(seq)
    return steps
