import unittest
from day10 import parse_input, solve_part1, solve_part2


class TestDay10(unittest.TestCase):
    def test_example_input_part1_1(self):
        with open("example_input_part1_1.txt") as f:
            input = parse_input(f)

        solution = solve_part1(input)
        self.assertEqual(solution, 4)

    def test_example_input_part1_2(self):
        with open("example_input_part1_2.txt") as f:
            input = parse_input(f)

        solution = solve_part1(input)
        self.assertEqual(solution, 8)

    def test_example_input_part2_1(self):
        with open("example_input_part2_1.txt") as f:
            input = parse_input(f)

        solution = solve_part2(input)
        self.assertEqual(solution, 4)

    def test_example_input_part2_2(self):
        with open("example_input_part2_2.txt") as f:
            input = parse_input(f)

        solution = solve_part2(input)
        self.assertEqual(solution, 8)

    def test_example_input_part2_3(self):
        with open("example_input_part2_3.txt") as f:
            input = parse_input(f)

        solution = solve_part2(input)
        self.assertEqual(solution, 10)


if __name__ == "__main__":
    unittest.main()
