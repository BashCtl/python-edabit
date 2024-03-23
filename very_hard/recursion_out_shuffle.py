"""
Recursion: The Out-Shuffle

An out-shuffle, also known as an out faro shuffle or a perfect shuffle,
is a controlled method for shuffling playing cards.
It is performed by splitting the deck into two equal halves
and interleaving them together perfectly,
with the condition that the top card of the deck remains in place.

Using an array to represent a deck of cards, an out-shuffle looks like:

[1, 2, 3, 4, 5, 6, 7, 8] ➞ [1, 5, 2, 6, 3, 7, 4, 8]
// Card 1 remains in the first position.
If we repeat the process, the deck eventually returns to original order:

Shuffle 1:

[1, 2, 3, 4, 5, 6, 7, 8] ➞ [1, 5, 2, 6, 3, 7, 4, 8]
Shuffle 2:

[1, 5, 2, 6, 3, 7, 4, 8] ➞ [1, 3, 5, 7, 2, 4, 6, 8]
Shuffle 3:

[1, 3, 5, 7, 2, 4, 6, 8] ➞ [1, 2, 3, 4, 5, 6, 7, 8]
// Back where we started.
Write a function that takes a positive even integer representing
the number of the cards in a deck, and returns the number
of out-shuffles required to return the deck to its original order.

Examples
shuffle_count(8) ➞ 3

shuffle_count(14) ➞ 12

shuffle_count(52) ➞ 8

Notes
The number of cards is always even and greater than one.
Thus, the smallest possible deck size is two.

"""


def shuffle_count(num, temp=[]):
    if len(temp) == 0:
        temp = [i for i in range(2, num)]
    mid = len(temp) // 2
    shuffled = []
    for x, y in zip(temp[:mid], temp[mid:]):
        shuffled.append(y)
        shuffled.append(x)
    if shuffled == sorted(shuffled):
        temp.clear()
        return 1
    return 1 + shuffle_count(num, shuffled)



from unittest import TestCase

num_vector, res_vector = [2, 8, 14, 26, 52, 70, 104, 208], [1, 3, 12, 20, 8, 22, 51, 66]
for i, n in enumerate(num_vector):
    TestCase().assertEqual(shuffle_count(n), res_vector[i])
