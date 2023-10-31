"""
pigLatin 3.0

Write a function that converts a sentence into pig latin.

Rules for converting to pig latin:

For words that begin with a vowel (a, e, i, o, u), add "way".
Otherwise, move all letters before the first vowel to the end and add "ay".
For simplicity, no punctuation will be present in the inputs.

Examples
pig_latin_sentence("this is pig latin") ➞ "isthay isway igpay atinlay"

pig_latin_sentence("wall street journal") ➞ "allway eetstray ournaljay"

Notes
All letters will be in lowercase.
"""
import re


def vowel_index(word):
    for i, v in enumerate(word):
        if v in "aeiou":
            return i


def pig_latin_sentence(sentence):
    words = sentence.split(" ")
    for i, word in enumerate(words):
        pattern = r"^[aeiou].*$"
        if re.findall(pattern, word):
            word = word + "way"
            words[i] = word
        else:
            index = vowel_index(word)
            word = word[index:] + word[:index] + "ay"
            words[i] = word
    return " ".join(words)


print(pig_latin_sentence("this is pig latin"))
print(pig_latin_sentence("wall street journal"))
