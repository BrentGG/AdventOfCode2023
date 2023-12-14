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


if __name__ == "__main__":
    part1()
