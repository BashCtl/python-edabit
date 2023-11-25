from unittest import TestCase


def overlap(s1, s2):
    shared_count = 0
    for i in range(1, min(len(s1), len(s2))):
        if s1[-i:] == s2[:i]:
            shared_count = i

    return shared_count


def join(lst):
    result = lst[0]
    shared = []
    for i in range(1, len(lst)):
        shared_index = overlap(lst[i - 1], lst[i])
        if shared_index != 0:
            shared.append(shared_index)
            result += lst[i][shared_index:]

    return ["".join(result), min(shared)] if len(shared) > 0 else ["".join(lst), 0]


TestCase().assertEqual(join(["happy", "python", "honey", "yelp", "plank", "lanky"]),
                       ["happythoneyelplanky", 1])
TestCase().assertEqual(join(["move", "over", "very"]), ["movery", 3])
TestCase().assertEqual(join(["oven", "envier", "erase", "serious"]), ["ovenvieraserious", 2])
TestCase().assertEqual(join(["to", "ops", "psy", "syllable"]), ["topsyllable", 1])
TestCase().assertEqual(join(["aaa", "bbb", "ccc", "ddd"]), ["aaabbbcccddd", 0])
TestCase().assertEqual(join(["abcde", "bcdefghi", "efghi", "fghij", "ghijklmnop"]), ["abcdefghijklmnop", 4])
TestCase().assertEqual(join(["aab", "abcccd", "cdeeef", "effff"]), ["aabcccdeeeffff", 2])
