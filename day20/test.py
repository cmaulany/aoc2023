import unittest
from day20 import parse_input, solve_part1, solve_part2, simulate_pulses, format_history


class TestDay20(unittest.TestCase):
    def test_example_input_part1_2(self):
        with open("example_input2.txt") as f:
            input = parse_input(f)

        memory, history = simulate_pulses(input)
        self.assertEqual(
            format_history(history),
            """button -low-> broadcaster
broadcaster -low-> a
a -high-> inv
a -high-> con
inv -low-> b
con -high-> output
b -high-> con
con -low-> output""",
        )

        _, history = simulate_pulses(input, memory)

        self.assertEqual(
            format_history(history),
            """button -low-> broadcaster
broadcaster -low-> a
a -low-> inv
a -low-> con
inv -high-> b
con -high-> output""",
        )

    def test_example_input_part1_1(self):
        with open("example_input1.txt") as f:
            input = parse_input(f)

        solution = solve_part1(input)
        self.assertEqual(solution, 32000000)

    def test_example_input_part1_2(self):
        with open("example_input2.txt") as f:
            input = parse_input(f)

        solution = solve_part1(input)
        self.assertEqual(solution, 11687500)


if __name__ == "__main__":
    unittest.main()
