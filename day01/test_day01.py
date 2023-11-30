import unittest
from day01.day01 import parse_input, solve


class TestDay01(unittest.TestCase):
    def test_example_input(self):
        stream = open("example-input.txt")
        input = parse_input(stream)
        solution = solve(input)

        self.assertEqual(solution, True)


if __name__ == "__main__":
    unittest.main()
