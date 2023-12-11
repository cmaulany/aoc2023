import unittest
from day11 import parse_input, solve_part1, solve_part2


class TestDay10(unittest.TestCase):
    def test_example_input_part1(self):
        with open("example_input.txt") as f:
            input = parse_input(f)

        solution = solve_part1(input)
        self.assertEqual(solution, 4)

    def test_example_input_part1(self):
        with open("example_input.txt") as f:
            input = parse_input(f)

        solution = solve_part2(input, 10)
        self.assertEqual(solution, 1030)

        solution = solve_part2(input, 100)
        self.assertEqual(solution, 8410)


if __name__ == "__main__":
    unittest.main()
