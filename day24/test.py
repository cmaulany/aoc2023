import unittest
from day24 import parse_input, solve_part1, solve_part2


class TestDay24(unittest.TestCase):
    def test_example_input_part1(self):
        with open("example_input.txt") as f:
            input = parse_input(f)

        solution = solve_part1(input, 7, 27)
        self.assertEqual(solution, 2)

    def test_example_input_part2(self):
        with open("example_input.txt") as f:
            input = parse_input(f)

        solution = solve_part2(input)
        self.assertEqual(solution, 47)


if __name__ == "__main__":
    unittest.main()
