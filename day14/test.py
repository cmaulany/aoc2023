import unittest
from day14 import parse_input, solve_part1, solve_part2


class TestDay14(unittest.TestCase):
    def test_example_input_part1(self):
        with open("example_input.txt") as f:
            input = parse_input(f)

        solution = solve_part1(input)
        self.assertEqual(solution, 136)

    def test_example_input_part1(self):
        with open("example_input.txt") as f:
            input = parse_input(f)

        solution = solve_part2(input)
        self.assertEqual(solution, 64)


if __name__ == "__main__":
    unittest.main()
