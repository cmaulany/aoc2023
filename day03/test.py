import unittest
from day03 import get_neighbors, parse_input, solve_part1, solve_part2


class TestDay03(unittest.TestCase):
    def test_get_neighbors(self):
        with open("example_input.txt") as stream:
            input = parse_input(stream)
        neighbors = get_neighbors(0, 0, 3, input)
        self.assertEqual(len(neighbors), 1)
        self.assertEqual(neighbors[0], (3, 1, "*"))

    def test_get_neighbors_multiple(self):
        raw = """ABCD
        E12F
        GHIJ"""

        input = [line.strip() for line in raw.splitlines()]

        neighbors = get_neighbors(1, 1, 2, input)
        self.assertEqual(len(neighbors), 10)

        chars = [c for _, _, c in neighbors]
        for c in "ABCDEFGHIJ":
            self.assertIn(c, chars)

    def test_get_neighbors_on_edge(self):
        raw = """ABC
        E12
        GHI"""

        input = [line.strip() for line in raw.splitlines()]

        neighbors = get_neighbors(1, 1, 2, input)
        self.assertEqual(len(neighbors), 7)

        chars = [c for _, _, c in neighbors]
        for c in "ABCEGHI":
            self.assertIn(c, chars)

    def test_get_neighbors_individual(self):
        combinations = [
            (
                """A...
                .12.
                ....""",
                [(0, 0, "A")],
            ),
            (
                """.A..
                .12.
                ....""",
                [(1, 0, "A")],
            ),
            (
                """..A.
                .12.
                ....""",
                [(2, 0, "A")],
            ),
            (
                """...A
                .12.
                ....""",
                [(3, 0, "A")],
            ),
            (
                """....
                A12.
                ....""",
                [(0, 1, "A")],
            ),
            (
                """....
                .12A
                ....""",
                [(3, 1, "A")],
            ),
            (
                """....
                .12.
                A...""",
                [(0, 2, "A")],
            ),
            (
                """....
                .12.
                .A..""",
                [(1, 2, "A")],
            ),
            (
                """....
                .12.
                ..A.""",
                [(2, 2, "A")],
            ),
            (
                """....
                .12.
                ...A""",
                [(3, 2, "A")],
            ),
        ]

        for raw, expected in combinations:
            input = [line.strip() for line in raw.splitlines()]

            neighbors = get_neighbors(1, 1, 2, input)
            self.assertEqual(neighbors, expected)

    def test_example_input_part1(self):
        with open("example_input.txt") as stream:
            input = parse_input(stream)

        solution = solve_part1(input)
        self.assertEqual(solution, 4361)

    def test_example_input_part2(self):
        with open("example_input.txt") as stream:
            input = parse_input(stream)

        solution = solve_part2(input)
        self.assertEqual(solution, 467835)


if __name__ == "__main__":
    unittest.main()
