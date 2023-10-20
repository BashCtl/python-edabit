def checker_board(n, el1, el2):
    if el1 == el2:
        return "invalid"
    result = []
    for i in range(n):
        temp = []
        for j in range(n):
            if (i + j) % 2 == 0:
                temp.append(el1)
            else:
                temp.append(el2)
        result.append(temp)
    return result

print(checker_board(2, 7, 6))
print(checker_board(3, "A", "B"))
