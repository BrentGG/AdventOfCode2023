import tqdm
import copy


def part1():
    file = open("input.txt", "r")

    total = 0
    for line in tqdm.tqdm(file, total=1000):
        line = line.replace("\n", "").split(" ")
        groups = [int(c) for c in line[1].split(",")]
        row = [c for c in line[0]]
        for arrangement in traverse(row, 0):
            if calc_groups(arrangement) == groups:
                total += 1

    print(total)


def traverse(row, idx):
    if idx >= len(row) or not row[idx:].__contains__("?"):
        return [row]
    first_q = row[idx:].index("?") + idx
    options = []
    row_cp = copy.deepcopy(row)
    row_cp[first_q] = "."
    options.extend(traverse(row_cp, first_q + 1))
    row_cp = copy.deepcopy(row)
    row_cp[first_q] = "#"
    options.extend(traverse(row_cp, first_q + 1))
    return options


def calc_groups(row):
    groups = []
    count = 0
    for col in row:
        if col == "." and count > 0:
            groups.append(count)
            count = 0
        elif col == "#":
            count += 1
    if count > 0:
        groups.append(count)
    return groups


def part2():
    pass


if __name__ == "__main__":
    part1()
