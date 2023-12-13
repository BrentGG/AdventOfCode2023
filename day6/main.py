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


def binary_search(start, end, time, dist, first_half):
    if end - start == 1:
        if first_half:
            if (time - start) * start > dist:
                return start
            return end
        else:
            if (time - end) * end > dist:
                return end
            return end

    hold_time = start + int(((end - start) / 2))
    if ((time - hold_time) * hold_time > dist and first_half) or ((time - hold_time) * hold_time <= dist and not first_half):
        return binary_search(start, hold_time, time, dist, first_half)
    else:
        return binary_search(hold_time, end, time, dist, first_half)


def part2():
    input_file = open("input.txt", "r")

    time = int(input_file.readline().replace("\n", "").split(":")[1].replace(" ", ""))
    dist = int(input_file.readline().replace("\n", "").split(":")[1].replace(" ", ""))

    hold_time_min = int(time / 2)
    hold_time_max = hold_time_min
    if time % 2 != 0:
        hold_time_max += 1

    hold_time_min = binary_search(0, hold_time_min, time, dist, True)
    hold_time_max = binary_search(hold_time_max, time, time, dist, False)
    print(hold_time_max - hold_time_min)


if __name__ == "__main__":
    part2()
