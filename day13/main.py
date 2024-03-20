def part1():
    lines = open("input.txt", "r").readlines()

    total = 0
    pattern = []
    for idx, line in enumerate(lines):
        line = line.replace("\n", "")
        if line != "":
            pattern.append([c for c in line])
        if line == "" or idx == len(lines) - 1:
            mirror_idx = find_mirror(pattern)
            if mirror_idx >= 0:
                total += 100 * mirror_idx
                pattern = []
                continue
            pattern = list(zip(*pattern[::-1]))
            mirror_idx = find_mirror(pattern)
            if mirror_idx < 0:
                print("Something went wrong.")
            else:
                total += mirror_idx
            pattern = []

    print(total)


def find_mirror(pattern):
    for i in range(len(pattern) - 1):
        mirror = True
        for row in range(0, min(i, len(pattern) - i - 2) + 1):
            for col in range(len(pattern[0])):
                if pattern[i - row][col] != pattern[i + row + 1][col]:
                    mirror = False
                    break
            if not mirror:
                break
        if mirror:
            return i + 1
    return -1


def part2():
    lines = open("input.txt", "r").readlines()

    total = 0
    pattern = []
    for idx, line in enumerate(lines):
        line = line.replace("\n", "")
        if line != "":
            pattern.append([c for c in line])
        if line == "" or idx == len(lines) - 1:
            mirror_idx = find_mirror_2(pattern)
            if mirror_idx >= 0:
                total += 100 * mirror_idx
                pattern = []
                continue
            pattern = list(zip(*pattern[::-1]))
            mirror_idx = find_mirror_2(pattern)
            if mirror_idx < 0:
                print("Something went wrong.")
            else:
                total += mirror_idx
            pattern = []

    print(total)

def find_mirror_2(pattern):
    for i in range(len(pattern) - 1):
        diff = 0
        for row in range(0, min(i, len(pattern) - i - 2) + 1):
            for col in range(len(pattern[0])):
                if pattern[i - row][col] != pattern[i + row + 1][col]:
                    diff += 1
        if diff == 1:
            return i + 1
    return -1


if __name__ == "__main__":
    part2()