from math import gcd


def part1():
    input_file = open("input.txt", "r")

    instructions = []
    network = {}
    for idx, line in enumerate(input_file):
        line = line.replace("\n", " ")
        if idx == 0:
            line = line.replace(" ", "")
            for instruction in line:
                instructions.append(0 if instruction == "L" else 1)
        elif idx >= 2:
            src_dest = line.replace(" ", "").replace("(", "").replace(")", "").split("=")
            network[src_dest[0]] = src_dest[1].split(",")

    instr_idx = 0
    steps = 0
    node = "AAA"
    while node != "ZZZ":
        node = network[node][instructions[instr_idx]]
        instr_idx += 1
        steps += 1
        if instr_idx >= len(instructions):
            instr_idx = 0

    print(steps)


def part2():
    input_file = open("input.txt", "r")

    instructions = []
    network = {}
    nodes = []
    for idx, line in enumerate(input_file):
        line = line.replace("\n", " ")
        if idx == 0:
            line = line.replace(" ", "")
            for instruction in line:
                instructions.append(0 if instruction == "L" else 1)
        elif idx >= 2:
            src_dest = line.replace(" ", "").replace("(", "").replace(")", "").split("=")
            network[src_dest[0]] = src_dest[1].split(",")
            if src_dest[0][-1] == "A":
                nodes.append(src_dest[0])

    steps = []
    for i in range(len(nodes)):
        instr_idx = 0
        step = 0
        while True:
            nodes[i] = network[nodes[i]][instructions[instr_idx]]
            step += 1
            instr_idx += 1
            if instr_idx >= len(instructions):
                instr_idx = 0
            if nodes[i][-1] == "Z":
                steps.append(step)
                break
    lcm = 1
    for step in steps:
        lcm = lcm * step // gcd(lcm, step)
    print(lcm)


if __name__ == "__main__":
    part2()
