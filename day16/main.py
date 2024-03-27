import copy


def part1():
    file = open("input.txt", "r")

    grid = []
    for line in file:
        line = line.replace("\n", "")
        grid.append([char for char in line])

    energized = []
    direction_hist = []
    propagate(grid, energized, direction_hist, 0, 0, "right")
    print(len(energized))


def propagate(grid, energized, direction_hist, start_x, start_y, direction):
    dir = copy.deepcopy(direction)
    x, y = copy.deepcopy(start_x), copy.deepcopy(start_y)
    while True:
        if not energized.__contains__((x, y)):
            energized.append((x, y))
            direction_hist.append([dir])
        else:
            idx = energized.index((x, y))
            if direction_hist[idx].__contains__(dir):
                return
            else:
                direction_hist[idx].append(dir)
        if grid[y][x] == "\\":
            if dir == "up":
                dir = "left"
            elif dir == "down":
                dir = "right"
            elif dir == "left":
                dir = "up"
            elif dir == "right":
                dir = "down"
        elif grid[y][x] == "/":
            if dir == "up":
                dir = "right"
            elif dir == "down":
                dir = "left"
            elif dir == "left":
                dir = "down"
            elif dir == "right":
                dir = "up"
        elif grid[y][x] == "|":
            if dir == "left" or dir == "right":
                propagate(grid, energized, direction_hist, x, y, "up")
                dir = "down"
        elif grid[y][x] == "-":
            if dir == "up" or dir == "down":
                propagate(grid, energized, direction_hist, x, y, "left")
                dir = "right"
        if dir == "up":
            y -= 1
        elif dir == "down":
            y += 1
        elif dir == "left":
            x -= 1
        elif dir == "right":
            x += 1
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return



def part2():
    pass


if __name__ == "__main__":
    part1()