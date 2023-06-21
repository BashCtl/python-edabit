def next_in_line(lst, num):
    if lst:
        lst.pop(0)
        lst.append(num)
        return lst
    return "No list has been selected"


print(next_in_line([5, 6, 7, 8, 9], 1))
print(next_in_line([], 6))
