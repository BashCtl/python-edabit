"""
How Many Boxes?

You work in a factory, and your job is to take items from a conveyor belt and pack them into boxes. Each box can hold a maximum of 10 kgs. Given a list containing the weight (in kg) of each item, how many boxes would you need to pack all of the items?

Example
boxes([2, 1, 2, 5, 4, 3, 6, 1, 1, 9, 3, 2]) ➞ 5

# Box 1 = [2, 1, 2, 5] (10kg)
# Box 2 = [4, 3] (7kg)
# Box 3 = [6, 1, 1] (8kg)
# Box 4 = [9] (9kg)
# Box 5 = [3, 2] (5kg)
Notes
There will always be a minimum of 1 item to pack. All items will weigh less than or equal to 10 kgs, and need to be packed in the order that they arrive.


"""


from unittest import TestCase


def boxes(weights):
    box = 0
    count = 0
    for weight in weights:
        if box + weight <= 10:
            box += weight
        else:
            count += 1
            box = weight
    if box > 0:
        count += 1

    return count


TestCase().assertEqual(boxes([7, 1, 2, 6, 1, 2, 3, 5, 9, 2, 1, 2, 5]), 5)
TestCase().assertEqual(boxes([2, 7, 1, 3, 3, 4, 7, 4, 1, 8, 2]), 5)
TestCase().assertEqual(boxes([1, 3, 3, 3, 2, 1, 1, 9, 7, 10, 8, 6, 1, 2, 9]), 8)
TestCase().assertEqual(boxes([4, 1, 2, 3, 5, 5, 1, 9]), 3)
TestCase().assertEqual(boxes([3, 1, 2, 7, 2, 6, 1]), 3)
TestCase().assertEqual(boxes([4, 6, 1, 9, 6, 1, 1, 9, 2, 9]), 6)
TestCase().assertEqual(boxes([2, 2, 10, 10, 1, 5, 2]), 4)
TestCase().assertEqual(boxes([9, 6, 2, 3, 1, 2, 4, 8, 3, 1, 3]), 5)
TestCase().assertEqual(boxes([2, 5, 1, 6, 2, 9, 5, 2, 1, 6, 1, 6, 6, 1]), 7)
TestCase().assertEqual(boxes([1, 2, 3, 2, 6, 4, 1]), 3)
TestCase().assertEqual(boxes([1, 1, 2, 1, 2, 10, 2, 2, 5, 1, 5]), 4)
TestCase().assertEqual(boxes([8, 3, 2, 1, 1, 2, 1, 3, 2, 1]), 3)
TestCase().assertEqual(boxes([1, 5, 3, 1, 2, 3, 2, 6, 3, 1, 3, 8, 1]), 5)
TestCase().assertEqual(boxes([8, 1, 1, 4, 7, 2, 1, 3, 1, 9, 7, 1, 5, 1, 1]), 7)
TestCase().assertEqual(boxes([2, 3, 4, 10, 1, 2, 5, 1, 1, 1, 1, 8, 2, 1]), 5)
TestCase().assertEqual(boxes([4, 6, 7, 3, 2, 2, 3, 1, 2, 2, 10, 3, 2]), 6)
TestCase().assertEqual(boxes([9, 2, 3, 4, 1, 3, 1, 1, 3]), 3)
TestCase().assertEqual(boxes([6, 2, 1, 9, 1, 8, 2, 8, 6, 6]), 6)
TestCase().assertEqual(boxes([6, 9, 3, 8, 10, 4, 7]), 7)
TestCase().assertEqual(boxes([4, 3, 1, 1, 1, 4, 7, 2, 1, 10, 1, 3, 8]), 6)
TestCase().assertEqual(boxes([10]), 1)
