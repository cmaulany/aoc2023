import unittest
from day21 import parse_input, solve_part1, solve_part2


class TestDay21(unittest.TestCase):
    def test_example_input_part1(self):
        with open("example_input.txt") as f:
            input = parse_input(f)

        solution = solve_part1(input, 1)
        self.assertEqual(solution, 2)

        solution = solve_part1(input, 2)
        self.assertEqual(solution, 4)

        solution = solve_part1(input, 3)
        self.assertEqual(solution, 6)

        solution = solve_part1(input, 6)
        self.assertEqual(solution, 16)

    def test_example_input_part2(self):
        """
        We test the naive solution of part 1 with the optimizated solution
        of part 2, using a smaller stepcount than the actual puzzle.
        """
        with open("input.txt") as f:
            input = parse_input(f)

        for i in range(3):
            n = 65 + 2 * i * 131
            self.assertEqual(solve_part1(input, n), solve_part2(input, n))


if __name__ == "__main__":
    unittest.main()
