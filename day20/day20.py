from math import lcm


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
            if conn in modules and modules[conn][0] == "&":
                memory[conn][name] = "low"
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
    history = []
    memory = None
    for _ in range(1000):
        memory, sub_history = simulate_pulses(input, memory)
        history += sub_history
    lows = [val for _, _, val in history if val == "low"]
    highs = [val for _, _, val in history if val == "high"]
    return len(lows) * len(highs)


def find_low_pulse(modules, name):
    i = 0
    memory = init_memory(modules)
    while True:
        memory, history = simulate_pulses(modules, memory)
        i += 1

        pulsed = any(to == name and val == "low" for _, to, val in history)
        if pulsed:
            return i


def solve_part2(input):
    pre_rx = next(
        name
        for name, (type, conns) in input.items()
        for conn in conns
        if type == "&" and conn == "rx"
    )
    pre_rx_sources = [
        name
        for name, (type, conns) in input.items()
        for conn in conns
        if type == "&" and conn == pre_rx
    ]
    cycles = [find_low_pulse(input, name) for name in pre_rx_sources]
    return lcm(*cycles)
