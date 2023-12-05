def part1():
    inputFile = open("input.txt", "r")

    colors = ["red", "green", "blue"]
    config = [12, 13, 14]

    indexSum = 0
    for line in inputFile:
        possible = True
        splitByColon = line.split(":")
        gameIdx = int(splitByColon[0].split(" ")[1])
        splitByColon[1] = splitByColon[1].replace(",", "")
        splitByColon[1] = splitByColon[1].replace("\n", "")
        for roundOfGame in splitByColon[1].split(";"):
            cubes = roundOfGame[1:].split(" ")
            for i in range(0, len(cubes), 2):
                for idx, color in enumerate(colors):
                    if color == cubes[i + 1] and int(cubes[i]) > config[idx]:
                        possible = False
                        break
                if not possible:
                    break
            if not possible:
                break
        if possible:
            indexSum += gameIdx
    print(indexSum)


def part2():
    inputFile = open("input.txt", "r")

    colors = ["red", "green", "blue"]

    powerSum = 0
    for line in inputFile:
        maximum = [0, 0, 0]
        splitByColon = line.split(":")
        splitByColon[1] = splitByColon[1].replace(",", "")
        splitByColon[1] = splitByColon[1].replace("\n", "")
        for roundOfGame in splitByColon[1].split(";"):
            cubes = roundOfGame[1:].split(" ")
            for i in range(0, len(cubes), 2):
                for idx, color in enumerate(colors):
                    if color == cubes[i + 1]:
                        if int(cubes[i]) > maximum[idx]:
                            maximum[idx] = int(cubes[i])
        powerSum += maximum[0] * maximum[1] * maximum[2]
    print(powerSum)


if __name__ == '__main__':
    part2()
