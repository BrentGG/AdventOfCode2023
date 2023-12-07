def performMapping(inp, mp):
    for rng in mp:
        if rng[1] <= inp < rng[1] + rng[2]:
            return inp - rng[1] + rng[0]
    return inp


def part1():
    input_file = open("input.txt", "r")

    seeds = []
    maps = []
    mapIdx = -1
    for idx, line in enumerate(input_file):
        if idx == 0:
            seeds = [int(x) for x in line.replace("\n", "").split(": ")[1].split(" ")]
        else:
            if not line[0].isdigit():
                mapIdx += 1
                maps.append([])
            elif line[0].isdigit():
                maps[mapIdx].append([int(x) for x in line.replace("\n", "").split(" ")])

    locations = []
    for seed in seeds:
        number = seed
        for mp in maps:
            number = performMapping(number, mp)
        locations.append(number)
    print(min(locations))


if __name__ == '__main__':
    part1()
