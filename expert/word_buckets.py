"""
Word Buckets

Write a function that divides a phrase into word buckets,
with each bucket containing n or fewer characters.
Only include full words inside each bucket.

Examples
split_into_buckets("she sells sea shells by the sea", 10)
➞ ["she sells", "sea shells", "by the sea"]

split_into_buckets("the mouse jumped over the cheese", 7)
➞ ["the", "mouse", "jumped", "over", "the", "cheese"]

split_into_buckets("fairy dust coated the air", 20)
➞ ["fairy dust coated", "the air"]

split_into_buckets("a b c d e", 2)
➞ ["a", "b", "c", "d", "e"]

Spaces count as one character.
Trim beginning and end spaces for each word bucket (see final example).
If buckets are too small to hold a single word, return an empty list: []
The final goal isn't to return just the words with a length equal (or lower) to the given n,
but to return the entire given phrase bucketized (if possible).
So, for the specific case of "by" the only word with a proper length,
the phrase can't be bucketized, and the returned list has to be empty.
"""
import textwrap


def split_into_buckets(phrase, n):
    result = []
    words = phrase.split(" ")
    if any([len(word) > n for word in words]):
        return []
    while len(words) > 0:
        bucket = []
        while len(words) > 0:
            bucket.append(words[0])
            if len("".join(bucket)) > n:
                bucket = bucket[:-1]
                break
            bucket.append(" ")
            words = words[1:]
        result.append("".join(bucket).strip())
    return result


print(split_into_buckets("she sells sea shells by the sea", 2), [])
print(split_into_buckets("ab bc cd", 1), [])
print(split_into_buckets("she sells sea shells by the sea", 10), ["she sells", "sea shells", "by the sea"])
print(split_into_buckets("the mouse jumped over the cheese", 7), ["the", "mouse", "jumped", "over", "the", "cheese"])
print(split_into_buckets("fairy dust coated the air", 20), ["fairy dust coated", "the air"])
print(split_into_buckets("do the hokey pokey", 6), ["do the", "hokey", "pokey"])
print(split_into_buckets("do the hokey pokey", 12), ["do the hokey", "pokey"])
print(split_into_buckets("rich magnificent trees dotted the landscape", 12), ["rich", "magnificent", "trees dotted", "the", "landscape"])
print(split_into_buckets("rich magnificent trees dotted the landscape", 15), ["rich", "magnificent", "trees dotted", "the landscape"])
print(split_into_buckets("rich magnificent trees dotted the landscape", 18), ["rich magnificent", "trees dotted the", "landscape"])
print(split_into_buckets("rich magnificent trees dotted the landscape", 22), ["rich magnificent trees", "dotted the landscape"])
print(split_into_buckets("rich magnificent trees dotted the landscape", 40), ["rich magnificent trees dotted the", "landscape"])
print(split_into_buckets("rich magnificent trees dotted the landscape", 43), ["rich magnificent trees dotted the landscape"])
print(split_into_buckets("beep bo bee bop bee bo bo bop", 6), ["beep", "bo bee", "bop", "bee bo", "bo bop"])
print(split_into_buckets("beep bo bee bop bee bo bo bop", 10), ["beep bo", "bee bop", "bee bo bo", "bop"])
print(split_into_buckets("a b c d e", 3), ["a b", "c d", "e"])
print(split_into_buckets("a b c d e", 2), ["a", "b", "c", "d", "e"])
print(split_into_buckets("a b c d e", 1), ["a", "b", "c", "d", "e"])
