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
            for rng in mp:
                if rng[1] <= number < rng[1] + rng[2]:
                    number = number - rng[1] + rng[0]
        locations.append(number)
    print(min(locations))


def doMapping(maps, map_idx, start, end):
    if map_idx >= len(maps):
        return start
    for j in range(len(maps[map_idx])):
        dest_start = maps[map_idx][j][0]
        dest_end = dest_start + maps[map_idx][j][2] - 1
        src_start = maps[map_idx][j][1]
        src_end = src_start + maps[map_idx][j][2] - 1
        if src_start <= start <= src_end:
            if end <= src_end:
                new_start = dest_start + (start - src_start)
                new_end = dest_start + (end - src_start)
                return doMapping(maps, map_idx + 1, new_start, new_end)
            else:
                new_start_1 = dest_start + (start - src_start)
                new_end_1 = dest_end
                result_1 = doMapping(maps, map_idx + 1, new_start_1, new_end_1)
                new_start_2 = src_end + 1
                new_end_2 = end
                result_2 = doMapping(maps, map_idx, new_start_2, new_end_2)
                return min([result_1, result_2])
    return doMapping(maps, map_idx + 1, start, end)


def part2():
    input_file = open("input.txt", "r")

    seeds = []
    maps = []
    map_idx = -1
    for idx, line in enumerate(input_file):
        if idx == 0:
            seeds = [int(x) for x in line.replace("\n", "").split(": ")[1].split(" ")]
        else:
            if line[0].isalpha():
                map_idx += 1
                maps.append([])
            elif line[0].isdigit():
                maps[map_idx].append([int(x) for x in line.replace("\n", "").split(" ")])

    locations = []
    for i in range(0, len(seeds), 2):
        seed_start = seeds[i]
        seed_end = seed_start + seeds[i + 1] - 1
        locations.append(doMapping(maps, 0, seed_start, seed_end))

    print(min(locations))


if __name__ == '__main__':
    part2()
