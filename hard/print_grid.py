def printgrid(rows, cols):
    result = []
    for r in range(1, rows + 1):
        inner = [r]
        for i in range(1, cols):
            inner.append(inner[i - 1] + rows)
        result.append(inner)
    return result


print(printgrid(3, 6))
