from day11 import parse_input, solve_part1, solve_part2

with open("input.txt") as stream:
    input = parse_input(stream)

solution_part1 = solve_part1(input)
print(f"Part 1: {solution_part1}")

solution_part2 = solve_part2(input)
print(f"Part 2: {solution_part2}")
