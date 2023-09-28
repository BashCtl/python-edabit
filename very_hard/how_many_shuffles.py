def shuffle_count(num):
    lst = [i for i in range(2, num)]
    count = 0
    temp = shuffle(lst, len(lst) // 2)
    count+=1
    while temp != lst:
        count += 1
        temp = shuffle(temp, len(lst) // 2)

    return count


def shuffle(items, mid):
    result = []
    for x, y in zip(items[:mid], items[mid:]):
        result.append(y)
        result.append(x)
    return result


print(shuffle_count(8))
print(shuffle_count(14))
print(shuffle_count(52))
