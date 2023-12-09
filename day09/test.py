import unittest
from day09 import parse_input, solve_part1, solve_part2


class TestDay09(unittest.TestCase):
    def test_example_input_part1(self):
        with open("example_input.txt") as stream:
            input = parse_input(stream)

        solution = solve_part1(input)
        self.assertEqual(solution, 114)

    def test_example_input_part2(self):
        with open("example_input.txt") as stream:
            input = parse_input(stream)

        solution = solve_part2(input)
        self.assertEqual(solution, 2)


if __name__ == "__main__":
    unittest.main()
