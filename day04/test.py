import unittest
from day04 import parse_input, solve_part1, solve_part2


class TestDay04(unittest.TestCase):
    def test_example_input_part1(self):
        with open("example_input.txt") as stream:
            input = parse_input(stream)

        solution = solve_part1(input)
        self.assertEqual(solution, 13)

    def test_example_input_part2(self):
        with open("example_input.txt") as stream:
            input = parse_input(stream)

        solution = solve_part2(input)
        self.assertEqual(solution, 30)


if __name__ == "__main__":
    unittest.main()
