def get_next_pos(pos, prev, scan):
    temp = [pos[0], pos[1]]
    char = scan[pos[0]][pos[1]]
    if char == "|":
        pos[0] += 1 if pos[0] + 1 != prev[0] else -1
    elif char == "-":
        pos[1] += 1 if pos[1] + 1 != prev[1] else -1
    elif char == "L":
        if pos[0] - 1 == prev[0]:
            pos[1] += 1
        else:
            pos[0] -= 1
    elif char == "7":
        if pos[0] + 1 == prev[0]:
            pos[1] -= 1
        else:
            pos[0] += 1
    elif char == "J":
        if pos[0] - 1 == prev[0]:
            pos[1] -= 1
        else:
            pos[0] -= 1
    elif char == "F":
        if pos[0] + 1 == prev[0]:
            pos[1] += 1
        else:
            pos[0] += 1
    return pos, temp


def part1():
    input_file = open("input.txt", "r")

    scan = []
    start = [0, 0]
    for row, line in enumerate(input_file):
        line = line.replace("\n", "")
        vals = []
        for col, char in enumerate(line):
            vals.append(char)
            if char == "S":
                start = [row, col]
        scan.append(vals)

    distance = 1
    pos1_prev = start
    pos2_prev = start
    positions = []
    if start[0] - 1 >= 0 and (scan[start[0] - 1][start[1]] == "|" or scan[start[0] - 1][start[1]] == "7" or scan[start[0] - 1][start[1]] == "F"):
        positions.append([start[0] - 1, start[1]])
    if start[0] + 1 < len(scan) and (scan[start[0] + 1][start[1]] == "|" or scan[start[0] + 1][start[1]] == "J" or scan[start[0] + 1][start[1]] == "J"):
        positions.append([start[0] + 1, start[1]])
    if start[1] - 1 >= 0 and (scan[start[0]][start[1] - 1] == "-" or scan[start[0]][start[1] - 1] == "L" or scan[start[0]][start[1] - 1] == "F"):
        positions.append([start[0], start[1] - 1])
    if start[1] + 1 < len(scan[0]) and (scan[start[0]][start[1] + 1] == "-" or scan[start[0]][start[1] + 1] == "J" or scan[start[0]][start[1] + 1] == "7"):
        positions.append([start[0], start[1] + 1])
    pos1, pos2 = positions[0], positions[1]

    while True:
        distance += 1
        pos1, pos1_prev = get_next_pos(pos1, pos1_prev, scan)
        if pos1 == pos2:
            break
        pos2, pos2_prev = get_next_pos(pos2, pos2_prev, scan)
        if pos1 == pos2:
            break

    print(distance)


if __name__ == "__main__":
    part1()
