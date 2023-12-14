def part1():
    input_file = open("input.txt", "r")

    sum_values = 0
    for line in input_file:
        levels = []
        values_str = line.replace("\n", "").split(" ")
        values = [int(value) for value in values_str]
        levels.append(values)

        level_idx = 0
        while True:
            new_level = []
            for i in range(len(levels[level_idx]) - 1):
                new_level.append(levels[level_idx][i + 1] - levels[level_idx][i])
            levels.append(new_level)
            level_idx += 1
            all_zero = True
            for val in new_level:
                if val != 0:
                    all_zero = False
                    break
            if all_zero:
                break

        levels[-1].append(0)
        for i in range(len(levels) - 2, -1, -1):
            levels[i].append(levels[i][-1] + levels[i + 1][-1])
        sum_values += levels[0][-1]

    print(sum_values)


def part2():
    input_file = open("input.txt", "r")

    sum_values = 0
    for line in input_file:
        levels = []
        values_str = line.replace("\n", "").split(" ")
        values = [int(value) for value in values_str]
        levels.append(values)

        level_idx = 0
        while True:
            new_level = []
            for i in range(len(levels[level_idx]) - 1):
                new_level.append(levels[level_idx][i + 1] - levels[level_idx][i])
            levels.append(new_level)
            level_idx += 1
            all_zero = True
            for val in new_level:
                if val != 0:
                    all_zero = False
                    break
            if all_zero:
                break

        levels[-1].insert(0, 0)
        for i in range(len(levels) - 2, -1, -1):
            levels[i].insert(0, levels[i][0] - levels[i + 1][0])
        sum_values += levels[0][0]

    print(sum_values)


if __name__ == "__main__":
    part2()
