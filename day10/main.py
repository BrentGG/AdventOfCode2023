""" Bit of a mess :( """

import copy


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


def flood(pos, scan):
    if pos[1] - 1 >= 0 and scan[pos[0]][pos[1] - 1] == ".":
        scan[pos[0]][pos[1] - 1] = "I"
        scan = flood([pos[0], pos[1] - 1], scan)
    if pos[1] + 1 < len(scan[0]) and scan[pos[0]][pos[1] + 1] == ".":
        scan[pos[0]][pos[1] + 1] = "I"
        scan = flood([pos[0], pos[1] + 1], scan)
    if pos[0] - 1 >= 0 and scan[pos[0] - 1][pos[1]] == ".":
        scan[pos[0] - 1][pos[1]] = "I"
        scan = flood([pos[0] - 1, pos[1]], scan)
    if pos[0] + 1 < len(scan) and scan[pos[0] + 1][pos[1]] == ".":
        scan[pos[0] + 1][pos[1]] = "I"
        scan = flood([pos[0] + 1, pos[1]], scan)
    return scan


def part2():
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

    loop = [start.copy(), pos1.copy(), pos2.copy()]
    while True:
        pos1, pos1_prev = get_next_pos(pos1, pos1_prev, scan)
        loop.append(pos1.copy())
        if pos1[0] < pos1_prev[0] and pos1[1] - 1 >= 0 and scan[pos1[0]][pos1[1] - 1] == ".":
            scan[pos1[0]][pos1[1] - 1] = "I"
        elif pos1[0] > pos1_prev[0] and pos1[1] + 1 < len(scan[0]) and scan[pos1[0]][pos1[1] + 1] == ".":
            scan[pos1[0]][pos1[1] + 1] = "I"
        elif pos1[1] < pos1_prev[1] and pos1[0] - 1 > 0 and scan[pos1[0] - 1][pos1[1]] == ".":
            scan[pos1[0] - 1][pos1[1]] = "I"
        elif pos1[1] > pos1_prev[1] and pos1[0] + 1 < len(scan) and scan[pos1[0] + 1][pos1[1]] == ".":
            scan[pos1[0] + 1][pos1[1]] = "I"
        if pos1 == pos2:
            break
        pos2, pos2_prev = get_next_pos(pos2, pos2_prev, scan)
        loop.append(pos2.copy())
        if pos2[0] < pos2_prev[0] and pos2[1] - 1 >= 0 and scan[pos2[0]][pos2[1] - 1] == ".":
            scan[pos2[0]][pos2[1] - 1] = "I"
        elif pos2[0] > pos2_prev[0] and pos2[1] + 1 < len(scan[0]) and scan[pos2[0]][pos2[1] + 1] == ".":
            scan[pos2[0]][pos2[1] + 1] = "I"
        elif pos2[1] < pos2_prev[1] and pos2[0] - 1 > 0 and scan[pos2[0] - 1][pos2[1]] == ".":
            scan[pos2[0] - 1][pos2[1]] = "I"
        elif pos2[1] > pos2_prev[1] and pos2[0] + 1 < len(scan) and scan[pos2[0] + 1][pos2[1]] == ".":
            scan[pos2[0] + 1][pos2[1]] = "I"
        if pos1 == pos2:
            break

    for row in range(len(scan)):
        for col in range(len(scan[0])):
            if scan[row][col] == "I":
                scan = flood([row, col], scan)

    for row in range(len(scan)):
        for col in range(len(scan[0])):
            if loop.__contains__([row, col]) or scan[row][col] == "I":
                print(scan[row][col], end="")
            else:
                print(".", end="")
        print("")
        

def get_next_pos_v2(pos, prev, scan):
    temp = [pos[0], pos[1]]
    char = scan[pos[1]][pos[0]]
    turn = 0  # 0 = no turn, -1 = left, 1 = right
    left = []
    right = []
    if char == "|":
        left = [[pos[0] - 1, pos[1]]]
        right = [[pos[0] + 1, pos[1]]]
        if pos[1] + 1 == prev[1]:
            pos[1] -= 1
        else:
            left, right = right, left
            pos[1] += 1
    elif char == "-":
        left = [[pos[0], pos[1] + 1]]
        right = [[pos[0], pos[1] - 1]]
        if pos[0] + 1 == prev[0]:
            pos[0] -= 1
        else:
            left, right = right, left
            pos[0] += 1
    elif char == "L":
        left = [[pos[0] + 1, pos[1] - 1]]
        right = [[pos[0] - 1, pos[1]], [pos[0] - 1, pos[1] + 1], [pos[0], pos[1] + 1]]
        if pos[1] - 1 == prev[1]:
            pos[0] += 1
            turn = -1
        else:
            left, right = right, left
            pos[1] -= 1
            turn = 1
    elif char == "7":
        left = [[pos[0] - 1, pos[1] + 1]]
        right = [[pos[0], pos[1] - 1], [pos[0] + 1, pos[1] - 1], [pos[0] + 1, pos[1]]]
        if pos[1] + 1 == prev[1]:
            pos[0] -= 1
            turn = -1
        else:
            left, right = right, left
            pos[1] += 1
            turn = 1
    elif char == "J":
        left = [[pos[0], pos[1] + 1], [pos[0] - 1, pos[1] + 1], [pos[0] - 1, pos[1]]]
        right = [[pos[0] - 1, pos[1] - 1]]
        if pos[1] - 1 == prev[1]:
            pos[0] -= 1
            turn = 1
        else:
            left, right = right, left
            pos[1] -= 1
            turn = -1
    elif char == "F":
        left = [[pos[0] - 1, pos[1]], [pos[0] - 1, pos[1] - 1], [pos[0], pos[1] - 1]]
        right = [[pos[0] + 1, pos[1] + 1]]
        if pos[1] + 1 == prev[1]:
            pos[0] += 1
            turn = 1
        else:
            left, right = right, left
            pos[1] += 1
            turn = -1
    return pos, temp, turn, left, right


def part2_v2():
    input_file = open("input.txt", "r")

    scan = []
    start = [0, 0]
    for row, line in enumerate(input_file):
        line = line.replace("\n", "")
        vals = []
        for col, char in enumerate(line):
            vals.append(char)
            if char == "S":
                start = [col, row]
        scan.append(vals)

    positions = []
    if start[1] - 1 >= 0 and (scan[start[1] - 1][start[0]] == "|" or scan[start[1] - 1][start[0]] == "7" or scan[start[1] - 1][start[0]] == "F"):
        positions.append([start[0], start[1] - 1])
    if start[1] + 1 < len(scan) and (scan[start[1] + 1][start[0]] == "|" or scan[start[1] + 1][start[0]] == "J" or scan[start[1] + 1][start[0]] == "L"):
        positions.append([start[0], start[1] + 1])
    if start[0] - 1 >= 0 and (scan[start[1]][start[0] - 1] == "-" or scan[start[1]][start[0] - 1] == "L" or scan[start[1]][start[0] - 1] == "F"):
        positions.append([start[0] - 1, start[1]])
    if start[0] + 1 < len(scan[0]) and (scan[start[1]][start[0] + 1] == "-" or scan[start[1]][start[0] + 1] == "J" or scan[start[1]][start[0] + 1] == "7"):
        positions.append([start[0] + 1, start[1]])
    pos1, pos2 = positions[0], positions[1]

    if pos1[0] == pos2[0]:
        scan[start[1]][start[0]] = "|"
    elif pos1[1] == pos2[1]:
        scan[start[1]][start[0]] = "-"
    elif pos1[1] == start[1]:
        if pos1[0] < start[0]:
            if pos2[1] < pos1[1]:
                scan[start[1]][start[0]] = "J"
            elif pos2[1] > pos1[1]:
                scan[start[1]][start[0]] = "7"
        if pos1[0] > start[0]:
            if pos2[1] < pos1[1]:
                scan[start[1]][start[0]] = "L"
            elif pos2[1] > pos1[1]:
                scan[start[1]][start[0]] = "F"
    elif pos1[0] == start[0]:
        if pos1[1] < start[1]:
            if pos2[0] < pos1[0]:
                scan[start[1]][start[0]] = "J"
            elif pos2[0] > pos1[0]:
                scan[start[1]][start[0]] = "L"
        if pos1[1] > start[1]:
            if pos2[0] < pos1[0]:
                scan[start[1]][start[0]] = "7"
            elif pos2[0] > pos1[0]:
                scan[start[1]][start[0]] = "F"

    pos1_prev = copy.deepcopy(pos2)
    pos1 = copy.deepcopy(start)
    loop = [pos1.copy(), pos2.copy()]
    lefts = []
    rights = []
    turns = 0
    while True:
        pos1, pos1_prev, turn, left, right = get_next_pos_v2(pos1, pos1_prev, scan)
        turns += turn
        for point in left:
            if 0 <= point[0] < len(scan[0]) and 0 <= point[1] < len(scan[1]):
                lefts.append(point)
        for point in right:
            if 0 <= point[0] < len(scan[0]) and 0 <= point[1] < len(scan[1]):
                rights.append(point)
        loop.append(pos1.copy())
        if pos1 == pos2:
            break

    inside = rights if turns > 0 else lefts
    i = 0
    while i < len(inside):
        if inside[i + 1:].__contains__(inside[i]) or loop.__contains__(inside[i]):
            del inside[i]
        else:
            i += 1

    visited = copy.deepcopy(inside)
    for point in inside:
        flooding(loop, point, visited, len(scan), len(scan[0]))
    print(len(visited))



def flooding(loop, point, visited, rows, cols):
    if not visited.__contains__(point):
        visited.append(point)
    for col in range(point[0] - 1, point[0] + 2):
        for row in range(point[1] - 1, point[1] + 2):
            if point == [col, row] or visited.__contains__([col, row]) or loop.__contains__([col, row]):
                continue
            if col < 0 or col >= cols or row < 0 or row >= rows:
                continue
            flooding(loop, [col, row], visited, rows, cols)




if __name__ == "__main__":
    part2_v2()
