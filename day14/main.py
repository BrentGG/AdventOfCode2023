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
    pass


if __name__ == "__main__":
    part1()