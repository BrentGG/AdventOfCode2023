if __name__ == '__main__':
    inputFile = open("input.txt", "r")

    calValSum = 0
    for line in inputFile:
        val = "aa"
        for i in range(len(line)):
            if not val[0].isdigit() and line[i].isdigit():
                val = line[i] + val[1]
            if not val[1].isdigit() and line[len(line) - 1 - i].isdigit():
                val = val[0] + line[len(line) - 1 - i]
            if val.isnumeric():
                calValSum += int(val)
                break
    print(calValSum)
