def parse_input(stream):
    return stream.readline()


def solve(input):
    return input == "hello"


if __name__ == "__main__":
    stream = open("input.txt")
    input = parse_input(stream)
    solution = solve(input)
    
    print(f"Solution: {solution}")
