def eda_bit(start, end):
    result = []
    for item in range(start, end + 1):
        if item % 3 == 0 and item % 5 == 0 or item == 0:
            result.append("EdaBit")
        elif item % 3 == 0:
            result.append("Eda")
        elif item % 5 == 0:
            result.append("Bit")
        else:
            result.append(item)
    return result


print(eda_bit(0, 10))
