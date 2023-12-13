from functools import cmp_to_key


def calc_score(hand):
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
    for i in range(len(item1)):
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
    face_cards = ["T", "J", "Q", "K", "A"]

    for line in input_file:
        split = line.replace("\n", "").split(" ")
        hand = []
        for card in split[0]:
            if card.isdigit():
                hand.append(int(card))
            else:
                hand.append(9 + face_cards.index(card) + 1)
        score = calc_score(hand)
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
    part1()
