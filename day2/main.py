if __name__ == '__main__':
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
