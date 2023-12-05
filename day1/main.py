if __name__ == '__main__':
    inputFile = open("input.txt", "r")
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    calValSum = 0
    for line in inputFile:
        val = "aa"
        indices = [-1, -1]
        for idx, char in enumerate(line):
            if char.isdigit() and (idx < indices[0] or indices[0] < 0):
                indices[0] = idx
                val = char + val[1]
            if char.isdigit() and (idx > indices[1] or indices[1] < 0):
                indices[1] = idx
                val = val[0] + char
        for idx, digit in enumerate(digits):
            found = line.find(digit)
            if found >= 0 and (indices[0] < 0 or found < indices[0]):
                indices[0] = found
                val = str(idx + 1) + val[1]
            found = line.rfind(digit)
            if found >= 0 and (indices[1] < 0 or found > indices[1]):
                indices[1] = found
                val = val[0] + str(idx + 1)
        calValSum += int(val)
    print(calValSum)
