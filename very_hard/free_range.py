"""
Free Range


Create a function which converts an ordered number list into
a list of ranges (represented as strings). Note how some lists have some numbers missing.

Examples
numbers_to_ranges([1, 2, 3, 4, 5]) ➞ ["1-5"]

numbers_to_ranges([3, 4, 5, 10, 11, 12]) ➞ ["3-5", "10-12"]

numbers_to_ranges([1, 2, 3, 4, 99, 100]) ➞ ["1-4", "99-100"]

numbers_to_ranges([1, 3, 4, 5, 6, 7, 8]) ➞ ["1", "3-8"]

Notes
If there are no numbers consecutive to a number in the list, represent it as only the string version of that number (see example #4).
Return an empty list if the given list is empty.

"""


def numbers_to_ranges(numbers):
    ranges = []
    if len(numbers) == 0:
        return ranges

    start = numbers[0]
    end = numbers[0]

    for num in numbers[1:]:
        if num == end + 1:
            end = num
        else:
            if start == end:
                ranges.append(str(start))
            else:
                ranges.append("{}-{}".format(start, end))
            start = num
            end = num

    if start == end:
        ranges.append(str(start))
    else:
        ranges.append("{}-{}".format(start, end))

    return ranges
