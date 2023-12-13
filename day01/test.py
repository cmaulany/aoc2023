import unittest
from day01 import parse_input, solve_part1, solve_part2


class TestDay01(unittest.TestCase):
    def test_example_input_part1(self):
        with open("example_input_part1.txt") as f:
            input = parse_input(f)

        solution = solve_part1(input)
        self.assertEqual(solution, 142)

    def test_example_input_part2(self):
        with open("example_input_part2.txt") as f:
            input = parse_input(f)

        solution = solve_part2(input)
        self.assertEqual(solution, 281)


if __name__ == "__main__":
    unittest.main()
