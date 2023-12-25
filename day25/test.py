import unittest
from day25 import parse_input, solve_part1


class TestDay25(unittest.TestCase):
    def test_example_input_part1(self):
        with open("example_input.txt") as f:
            input = parse_input(f)

        solution = solve_part1(input)
        self.assertEqual(solution, 54)


if __name__ == "__main__":
    unittest.main()
