"""
Combined Vector Sequence

The goal is to test if a consecutive sequence is formed.
A consecutive sequence is defined as sequence of incrementing numbers (e.g. 1, 2, 3 or 5, 6, 7, 8).
The twist is that you have to consider the combination of vectors as shown.

[3 5 1 -5 ]  =>  [3+4  5+3  1+8  15-5]  =  [7 8 9 10]  =>  true
[4 3 8 15]

Also important is that the vectors can be of different sizes,
where excess numbers in the longer one will be paired with 0s from the other one.

[2 2 2  ]  =>  [2+5  2+6  2+7  10+0]  = [ 7 8 9 10]  =>  true
[5 6 7 10]

Notes
Each array has at least two elements.
"""
from itertools import zip_longest


def has_consecutive_series(v1, v2):
    combined = [x + y for x, y in zip_longest(v1, v2, fillvalue=0)]
    return sorted(combined) == list(range(min(combined), max(combined)+1))


print(has_consecutive_series([1, 2, 3], [1, 1, 1]))
print(has_consecutive_series([1, 2, 3], [1, 2, 1]))
print(has_consecutive_series([4, 6, -5, 8, 4], [-2, -3, 9, -3, 2]))
