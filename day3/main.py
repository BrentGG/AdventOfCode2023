def part1():
    input_file = open("input.txt", "r")

    schematic = []
    for line in input_file:
        schematic.append(line.replace("\n", ""))

    partNumberSum = 0
    for row, line in enumerate(schematic):
        is_number = False
        number = ""
        has_symbol = False
        for col, char in enumerate(line):
            if char.isdigit():
                is_number = True
                number += char
                if not has_symbol:
                    for i in range(col - 1, col + 2):
                        for j in range(row - 1, row + 2):
                            if 0 < i < len(schematic[0]) and 0 < j < len(schematic):
                                if not schematic[j][i].isdigit() and not schematic[j][i] == '.':
                                    has_symbol = True
                                    break
                        if has_symbol:
                            break
            if not char.isdigit() or col == len(line) - 1:
                if is_number:
                    if has_symbol:
                        partNumberSum += int(number)
                    is_number = False
                    number = ""
                    has_symbol = False
    print(partNumberSum)


if __name__ == '__main__':
    part1()
