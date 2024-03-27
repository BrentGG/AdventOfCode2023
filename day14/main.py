import tqdm
import copy


def part1():
    lines = open("input.txt", "r").readlines()
    platform = []
    load = 0
    for line in lines:
        line = line.replace("\n", "")
        platform.append(["." for i in range(len(line))])
        for col, char in enumerate(line):
            if char == "O":
                for row in range(len(platform) - 1, -1, -1):
                    if platform[row][col] != ".":
                        row += 1
                        break
                platform[row][col] = "O"
                load += len(lines) - row
            else:
                platform[-1][col] = char
    print(load)


def part2():
    lines = open("input.txt", "r").readlines()
    platform = []
    history = []
    for line in lines:
        line = line.replace("\n", "")
        platform.append([c for c in line])
    cycles_left = 1000000000
    loop = False
    for cycle in tqdm.tqdm(range(1000000000)):
        history.append(copy.deepcopy(platform))
        for dir in range(4):
            north(platform)
            temp = list(zip(*platform[::-1]))
            platform = [list(row) for row in temp]
        cycles_left -= 1
        if history.__contains__(platform) and not loop:
            history.reverse()
            idx = history.index(platform)
            history.reverse()
            cycles_left = (1000000000 - idx) % (cycle - idx)
            loop = True
        if cycles_left <= 0:
            break
    load = 0
    for row in range(len(platform)):
        count = 0
        for col in platform[row]:
            if col == "O":
                count += 1
        load += (len(platform) - row) * count
    print(load)


def north(platform):
    for row in range(1, len(platform)):
        for col in range(len(platform[0])):
            if platform[row][col] == "O":
                for i in range(row - 1, -1, -1):
                    if platform[i][col] != ".":
                        i += 1
                        break
                platform[row][col] = "."
                platform[i][col] = "O"
    return platform


if __name__ == "__main__":
    part2()