def parse_input(f):
    modules = {}
    for line in f.readlines():
        left, right = line.strip().split(" -> ")
        if left[0] in "%&":
            type = left[0]
            name = left[1:]
        else:
            type = None
            name = left
        modules[name] = (type, [conn.strip() for conn in right.split(",")])
    return modules


def invert(val):
    if val == "high":
        return "low"
    return "high"


def init_memory(modules):
    memory = {}
    for name, module in modules.items():
        type, _ = module
        if type == "%":
            memory[name] = "off"
        elif type == "&":
            memory[name] = {}

    for name, module in modules.items():
        type, conns = module
        for conn in conns:
            if conn != "output" and conn in modules and modules[conn][0] == "&":
                memory[conn][name] = "off"
    return memory


def simulate_pulses(modules, memory=None):
    if memory == None:
        memory = init_memory(modules)

    pulses = [("button", "broadcaster", "low")]
    history = []
    while pulses:
        frm, to, val = pulses.pop(0)
        history.append((frm, to, val))
        if to not in modules:
            continue
        to_type, to_conns = modules[to]
        if to == "broadcaster":
            for to_conn in to_conns:
                pulses.append((to, to_conn, val))
            continue
        if to_type == "%" and val == "low":
            state = memory[to]
            memory[to] = "on" if state == "off" else "off"
            for to_conn in to_conns:
                pulses.append((to, to_conn, "high" if state == "off" else "low"))

        elif to_type == "&":
            memory[to][frm] = val
            pulse_type = (
                "low" if all(v == "high" for v in memory[to].values()) else "high"
            )
            for to_conn in to_conns:
                pulses.append((to, to_conn, pulse_type))

    return memory, history


def format_history(history):
    return "\n".join([f"{frm} -{val}-> {to}" for frm, to, val in history])


def solve_part1(input):
    total_history = []
    memory = None
    for _ in range(1000):
        memory, history = simulate_pulses(input, memory)
        total_history += history
    lows = [val for _, _, val in total_history if val == "low"]
    highs = [val for _, _, val in total_history if val == "high"]
    print(len(lows), len(highs))

    return len(lows) * len(highs)


def solve_part2(input):
    memory = None
    i = 0
    while True:
        memory, history = simulate_pulses(input, memory)
        if any(to == "rx" and val == "low" for _, to, val in history):
            break
        i += 1
    return i
