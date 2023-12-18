import unittest
from day15 import hash, parse_input, solve_part1, solve_part2


class TestDay15(unittest.TestCase):
    def test_hash(self):
        self.assertEqual(hash("HASH"), 52)

    def test_example_input_part1(self):
        with open("example_input.txt") as f:
            input = parse_input(f)

        solution = solve_part1(input)
        self.assertEqual(solution, 1320)

    def test_example_input_part2(self):
        with open("example_input.txt") as f:
            input = parse_input(f)

        solution = solve_part2(input)
        self.assertEqual(solution, 145)


if __name__ == "__main__":
    unittest.main()
