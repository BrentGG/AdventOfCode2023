import math


def part1():
    input_file = open("input.txt", "r")

    point_total = 0
    for line in input_file:
        line_split = line.replace("  ", " ").replace("\n", "").split(":")[1].split("|")
        winning_numbers = [int(x) for x in line_split[0].split(" ") if x != '']
        your_numbers = [int(x) for x in line_split[1].split(" ") if x != '']
        matching_amount = len(set(winning_numbers) & set(your_numbers))
        if matching_amount > 0:
            point_total += int(math.pow(2, matching_amount - 1))
    print(point_total)


if __name__ == '__main__':
    part1()
