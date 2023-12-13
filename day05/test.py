import unittest
from day05 import (
    map_one,
    map_ranges,
    map_range,
    merge_ranges,
    parse_input,
    solve_part1,
    solve_part2,
)


class TestDay05(unittest.TestCase):
    def test_map_one(self):
        ranges = [
            (10, 20, 5),
            (30, 40, 10),
        ]
        self.assertEqual(map_one(10, ranges), 10)
        self.assertEqual(map_one(20, ranges), 10)
        self.assertEqual(map_one(24, ranges), 14)
        self.assertEqual(map_one(28, ranges), 28)
        self.assertEqual(map_one(30, ranges), 30)
        self.assertEqual(map_one(45, ranges), 35)

    def test_map_range_a(self):
        self.assertEqual(
            map_range((0, 100), [(150, 50, 25)]), [(0, 50), (75, 100), (150, 175)]
        )

    def test_map_range_b(self):
        self.assertEqual(
            map_range(
                (0, 100),
                [
                    (150, 50, 25),
                    (20, 90, 5),
                ],
            ),
            [(0, 50), (75, 90), (95, 100), (150, 175)],
        )

    def test_map_range_c(self):
        self.assertEqual(map_range((0, 10), [(0, 50, 25)]), [(0, 10)])

    def test_map_range_d(self):
        self.assertEqual(
            map_range((50, 100), [(0, 60, 10)]), [(0, 10), (50, 60), (70, 100)]
        )

    def test_map_range_e(self):
        self.assertEqual(map_range((50, 70), [(0, 60, 40)]), [(0, 10), (50, 60)])

    def test_map_ranges(self):
        self.assertEqual(
            map_ranges([(0, 10), (40, 60)], [(0, 50, 25)]),
            [(0, 10), (40, 50)],
        )

        self.assertEqual(map_ranges([(60, 70)], [(10, 50, 30)]), [(20, 30)])

        self.assertEqual(map_ranges([(60, 100)], [(10, 50, 30)]), [(20, 40), (80, 100)])

        self.assertEqual(
            map_ranges(
                [(79, 93)],
                [
                    (52, 50, 48),
                    (50, 98, 2),
                ],
            ),
            [(81, 95)],
        )

    def test_merge_ranges(self):
        self.assertEqual(
            merge_ranges([(0, 10), (40, 50), (0, 10)]), [(0, 10), (40, 50)]
        )
        self.assertEqual(
            merge_ranges([(0, 10), (10, 20), (30, 40), (35, 50), (60, 70)]),
            [(0, 20), (30, 50), (60, 70)],
        )

    def test_example_input_part1(self):
        with open("example_input.txt") as f:
            input = parse_input(f)

        solution = solve_part1(input)
        self.assertEqual(solution, 35)

    def test_example_input_part2(self):
        with open("example_input.txt") as f:
            input = parse_input(f)

        solution = solve_part2(input)
        self.assertEqual(solution, 46)


if __name__ == "__main__":
    unittest.main()
