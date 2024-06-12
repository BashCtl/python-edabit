"""
List Up a List of Strings in a Proper Way


Given a list of strings (nouns), list them up in a complete sentence.

Examples
sentence(["orange", "apple", "pear"]) ➞ "An orange, an apple and a pear."

sentence(["keyboard", "mouse"]) ➞ "A keyboard and a mouse."

sentence(["car", "plane", "truck", "boat"]) ➞ "A car, a plane, a truck and a boat."
Notes
The sentence starts with a capital letter.
Do not change the order of the words.
A/An should be correct in all places.
Put commas between nouns, except between the last two (there you put "and").
The sentence ends with a .
There are at least two nouns given.
Every given word is lowercase.

"""

from unittest import TestCase


def sentence(nouns):
    def article(word):
        return "an" if word[0] in 'aeiou' else "a"

    nouns_with_articles = [f"{article(noun)} {noun}" for noun in nouns]

    if len(nouns) > 2:
        result = ', '.join(nouns_with_articles[:-1]) + f" and {nouns_with_articles[-1]}."
    else:
        result = f" and ".join(nouns_with_articles) + "."

    return result.capitalize()


TestCase().assertEqual(sentence(["banana", "apple", "orange"]), "A banana, an apple and an orange.")
TestCase().assertEqual(sentence(["car", "plane"]), "A car and a plane.")
TestCase().assertEqual(sentence(["fox", "wolf", "elephant", "cat"]), "A fox, a wolf, an elephant and a cat.")
TestCase().assertEqual(sentence(["mom", "dad"]), "A mom and a dad.")
TestCase().assertEqual(sentence(["school", "hospital", "library"]), "A school, a hospital and a library.")
TestCase().assertEqual(sentence(["aa", "ee", "ii", "oo", "uu", "vv", "tt", "qw", "zz"]), "An aa, an ee, an ii, an oo, an uu, a vv, a tt, a qw and a zz.")