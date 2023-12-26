import unittest
from day23 import parse_input, solve_part1, solve_part2


class TestDay23(unittest.TestCase):
    def test_example_input_part1(self):
        with open("example_input.txt") as f:
            input = parse_input(f)

        solution = solve_part1(input)
        self.assertEqual(solution, 94)

    def test_example_input_part2(self):
        with open("example_input.txt") as f:
            input = parse_input(f)

        solution = solve_part2(input)
        self.assertEqual(solution, 154)


if __name__ == "__main__":
    unittest.main()
