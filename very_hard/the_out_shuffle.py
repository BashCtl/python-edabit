def shuffle(cards):
    result = [cards[0]]
    mid = len(cards) // 2
    for a, b in zip(cards[1:mid], cards[mid:len(cards) - 1]):
        result.append(b)
        result.append(a)
    result.append(cards[-1])
    return result


def shuffle_count(num):
    deck = [i for i in range(1, num + 1)]
    temp_deck = shuffle(deck)
    count = 1
    while deck != temp_deck:
        count += 1
        temp_deck = shuffle(temp_deck)

    return count


print(shuffle_count(8))
print(shuffle_count(14))
print(shuffle_count(2))
