import unittest
from day08 import parse_input, solve_part1, solve_part2


class TestDay08(unittest.TestCase):
    def test_example_input_part1_1(self):
        with open("example_input_part1_1.txt") as stream:
            input = parse_input(stream)

        solution = solve_part1(input)
        self.assertEqual(solution, 2)

    def test_example_input_part1_2(self):
        with open("example_input_part1_2.txt") as stream:
            input = parse_input(stream)

        solution = solve_part1(input)
        self.assertEqual(solution, 6)

    def test_example_input_part2(self):
        with open("example_input_part2.txt") as stream:
            input = parse_input(stream)

        solution = solve_part2(input)
        self.assertEqual(solution, 6)


if __name__ == "__main__":
    unittest.main()
