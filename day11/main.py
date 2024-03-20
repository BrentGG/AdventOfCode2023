def part1():
    input_file = open("input.txt", "r")

    empty_rows = []
    empty_cols = []
    galaxies = []
    for row, line in enumerate(input_file):
        line = line.replace("\n", "")
        if len(empty_cols) == 0:
            empty_cols = [True for i in range(len(line))]
        empty = True
        for col, char in enumerate(line):
            if char != ".":
                galaxies.append([row, col])
                empty_cols[col] = False
                empty = False
        empty_rows.append(empty)

    total = 0
    count = 0
    for i in range(len(galaxies) - 1):
        r1, c1 = galaxies[i][0], galaxies[i][1]
        for j in range(i + 1, len(galaxies)):
            r2, c2 = galaxies[j][0], galaxies[j][1]
            rows = abs(r1 - r2) + sum(empty_rows[min(r1 ,r2):max(r1, r2)])
            cols = abs(c1 - c2) + sum(empty_cols[min(c1 ,c2):max(c1, c2)])
            total += rows + cols
            count += 1

    print(total)


def part2():
    input_file = open("input.txt", "r")

    empty_rows = []
    empty_cols = []
    galaxies = []
    for row, line in enumerate(input_file):
        line = line.replace("\n", "")
        if len(empty_cols) == 0:
            empty_cols = [True for i in range(len(line))]
        empty = True
        for col, char in enumerate(line):
            if char != ".":
                galaxies.append([row, col])
                empty_cols[col] = False
                empty = False
        empty_rows.append(empty)

    total = 0
    count = 0
    for i in range(len(galaxies) - 1):
        r1, c1 = galaxies[i][0], galaxies[i][1]
        for j in range(i + 1, len(galaxies)):
            r2, c2 = galaxies[j][0], galaxies[j][1]
            rows = abs(r1 - r2) + (sum(empty_rows[min(r1, r2):max(r1, r2)]) * (1000000 - 1))
            cols = abs(c1 - c2) + (sum(empty_cols[min(c1, c2):max(c1, c2)]) * (1000000 - 1))
            total += rows + cols
            count += 1

    print(total)


if __name__ == "__main__":
    part2()