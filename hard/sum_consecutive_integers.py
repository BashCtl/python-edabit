"""
Sum Consecutive Integers

Create a function that takes a list of integers (positive / negative) and return
the sum of the numbers that repeat consecutively (return your result as a list).

Examples
sum_consecutives([0, 7, 7, 7, 5, 4, 9, 9, 0]) ➞ [0, 21, 5, 4, 18, 0]

sum_consecutives([4, 4, 5, 6, 8, 8, 8]) ➞ [8, 5, 6, 24]

sum_consecutives([-5, -5, 7, 7, 12, 0]) ➞ [-10, 14, 12, 0]


"""


def sum_consecutives(lst):
    result = []
    temp = lst[0]
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            temp += lst[i]
        else:
            result.append(temp)
            temp = lst[i]
    result.append(temp)

    return result


# print(sum_consecutives([0, 7, 7, 7, 5, 4, 9, 9, 0]))
# print(sum_consecutives([-5, -5, 7, 7, 12, 0]))
print(sum_consecutives([4, 4, 5, 6, 8, 8, 8]))
