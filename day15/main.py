def part1():
    seq = open("input.txt", "r").read().replace("\n", "").split(",")

    total = 0
    for step in seq:
        value = 0
        for char in step:
            value += ord(char)
            value *= 17
            value %= 256
        total += value
    print(total)


class Lens():
    def __init__(self, label, focal_length):
        self.label = label
        self.focal_length = focal_length

def find_lens(box, label):
    for idx, lens in enumerate(box):
        if lens.label == label:
            return idx
    return -1

def part2():
    seq = open("input.txt", "r").read().replace("\n", "").split(",")

    boxes = [[] for i in range(256)]
    for step in seq:
        box = 0
        operator_idx = step.find("=")
        if operator_idx < 0:
            operator_idx = step.find("-")
        label = step[:operator_idx]
        for char in label:
            box += ord(char)
            box *= 17
            box %= 256
        if step[operator_idx] == "=":
            idx = find_lens(boxes[box], label)
            if idx >= 0:
                boxes[box][idx].focal_length = int(step[-1])
            else:
                boxes[box].append(Lens(label, int(step[-1])))
        elif step[operator_idx] == "-":
            idx = find_lens(boxes[box], label)
            if idx >= 0:
                del boxes[box][idx]

    total = 0
    for box_idx, box in enumerate(boxes):
        for slot_idx, lens in enumerate(box):
            total += (box_idx + 1) * (slot_idx + 1) * lens.focal_length
    print(total)


if __name__ == "__main__":
    part2()