from collections import defaultdict, Counter


def parse_input(f):
    graph = defaultdict(lambda: set())
    for line in f.readlines():
        name, conns = line.strip().split(": ")
        for conn in conns.split(" "):
            graph[name].add(conn)
            graph[conn].add(name)
    return graph


def find_cut(graph, size):
    for start in graph.keys():
        group = set()
        group_edges = [(start, b) for b in graph[start]]
        while len(group_edges) > size:
            new_node = Counter(b for _, b in group_edges).most_common(1)[0][0]
            group.add(new_node)
            group_edges = [
                (a, b)
                for a in graph.keys()
                for b in graph[a]
                if a in group and b not in group
            ]
        if len(group_edges) == size:
            return group, group_edges


def solve_part1(input):
    group, _ = find_cut(input, 3)
    size_a = len(group)
    size_b = len(input) - size_a
    return size_a * size_b
