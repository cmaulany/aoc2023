import unittest
from day19 import parse_input, solve_part1, solve_part2


class TestDay19(unittest.TestCase):
    def test_example_input_part1(self):
        with open("example_input.txt") as f:
            input = parse_input(f)

        solution = solve_part1(input)
        self.assertEqual(solution, 19114)
    
    def test_example_input_part2(self):
        with open("example_input.txt") as f:
            input = parse_input(f)

        solution = solve_part2(input)
        self.assertEqual(solution, 167409079868000)


if __name__ == "__main__":
    unittest.main()
