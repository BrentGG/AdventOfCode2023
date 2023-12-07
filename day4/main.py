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


def get_count(idx, matching_amount):
    count = 0
    for i in range(1, matching_amount[idx] + 1):
        if idx + i < len(matching_amount):
            count += get_count(idx + i, matching_amount)
    return count + 1


def part2():
    input_file = open("input.txt", "r")

    matching_amounts = []
    for line in input_file:
        line_split = line.replace("  ", " ").replace("\n", "").split(":")[1].split("|")
        winning_numbers = [int(x) for x in line_split[0].split(" ") if x != '']
        your_numbers = [int(x) for x in line_split[1].split(" ") if x != '']
        matching_amounts.append(len(set(winning_numbers) & set(your_numbers)))

    count = 0
    for idx in range(len(matching_amounts)):
        count += get_count(idx, matching_amounts)
    print(count)


if __name__ == '__main__':
    part2()
