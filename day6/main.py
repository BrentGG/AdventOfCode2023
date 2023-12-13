def part1():
    input_file = open("input.txt", "r")

    times = []
    for part in input_file.readline().replace("\n", "").split(" "):
        if part.isnumeric():
            times.append(int(part))
    dists = []
    for part in input_file.readline().replace("\n", "").split(" "):
        if part.isnumeric():
            dists.append(int(part))

    product = 1
    for i in range(len(times)):
        count = 1
        hold_time_min = int(times[i] / 2)
        hold_time_max = hold_time_min
        if times[i] % 2 != 0:
            hold_time_max += 1
            count += 1
        while True:
            old_count = count
            hold_time_min -= 1
            hold_time_max += 1
            if (times[i] - hold_time_min) * hold_time_min > dists[i]:
                count += 1
            if (times[i] - hold_time_max) * hold_time_max > dists[i]:
                count += 1
            if count == old_count:
                break
        product *= count

    print(product)


if __name__ == "__main__":
    part1()
