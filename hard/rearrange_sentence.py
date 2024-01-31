"""
Rearrange the Sentence

Given a sentence with numbers representing a word's location embedded within each word,
return the sorted sentence.

Examples
rearrange("is2 Thi1s T4est 3a") ➞ "This is a Test"

rearrange("4of Fo1r pe6ople g3ood th5e the2") ➞ "For the good of the people"

rearrange(" ") ➞ " "

Notes
Only the integers 1-9 will be used.


"""
import re


def rearrange(sentence):
    sentence = sentence.strip()
    if not sentence:
        return sentence
    words = sentence.split(" ")

    words = sorted(words, key=lambda w: int(re.sub(r"[^\d]", "", w)))
    return " ".join(list(map(lambda w: re.sub(r"\d", "", w), words)))


print(rearrange(" "))
print(rearrange("is2 Thi1s T4est 3a"))
