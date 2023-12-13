from functools import cmp_to_key


def calc_score_1(hand):
    seen = []
    three_of_kind = 0
    two_of_kind = 0
    for card in hand:
        if not seen.__contains__(card):
            count = hand.count(card)
            if count == 5:
                return 6
            elif count == 4:
                return 5
            elif count == 3:
                three_of_kind += 1
                if two_of_kind > 0:
                    return 4
            elif count == 2:
                two_of_kind += 1
                if three_of_kind > 0:
                    return 4
            seen.append(card)
        else:
            seen.append(card)
    if three_of_kind > 0:
        return 3
    if two_of_kind > 1:
        return 2
    if two_of_kind > 0:
        return 1
    return 0


def hand_compare(item1, item2):
    for i in range(len(item1) - 1):
        if item1[i] > item2[i]:
            return 1
        elif item1[i] < item2[i]:
            return -1
    return 0


def part1():
    input_file = open("input.txt", "r")

    hands = []
    for i in range(7):
        hands.append([])
    order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

    for line in input_file:
        split = line.replace("\n", "").split(" ")
        hand = []
        for card in split[0]:
            hand.append(order.index(card))
        score = calc_score_1(hand)
        hand.append(int(split[1]))
        hands[score].append(hand)

    for i in range(len(hands)):
        hands[i].sort(key=cmp_to_key(hand_compare))

    rank = 1
    total = 0
    for hand_group in hands:
        for hand in hand_group:
            total += rank * hand[-1]
            rank += 1

    print(total)


def calc_score_2(hand):
    amounts = [0 for i in range(13)]
    for card in hand:
        amounts[card] += 1
    joker_amount = amounts[0]
    amounts[0] = 0
    amounts.sort(reverse=True)
    amounts[0] += joker_amount
    highest_amount = amounts[0]
    second_highest_amount = amounts[1]
    if highest_amount == 5:
        return 6
    elif highest_amount == 4:
        return 5
    elif highest_amount == 3 and second_highest_amount == 2:
        return 4
    elif highest_amount == 3:
        return 3
    elif highest_amount == 2 and amounts.count(2) == 2:
        return 2
    elif highest_amount == 2:
        return 1
    elif highest_amount == 1:
        return 0
    return 0


def part2():
    input_file = open("input.txt", "r")

    hands = []
    for i in range(7):
        hands.append([])
    order = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

    for line in input_file:
        split = line.replace("\n", "").split(" ")
        hand = []
        for card in split[0]:
            hand.append(order.index(card))
        score = calc_score_2(hand)
        hand.append(int(split[1]))
        hands[score].append(hand)

    for i in range(len(hands)):
        hands[i].sort(key=cmp_to_key(hand_compare))
    rank = 1
    total = 0
    for hand_group in hands:
        for hand in hand_group:
            total += rank * hand[-1]
            rank += 1

    print(total)


if __name__ == "__main__":
    part2()
