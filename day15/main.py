def part1():
    seq = open("input.txt", "r").read().replace("\n", "").split(",")

    total = 0
    for step in seq:
        value = 0
        for char in step:
            value += ord(char)
            value *= 17
            value %= 256
        total += value
    print(total)

def part2():
    pass


if __name__ == "__main__":
    part1()