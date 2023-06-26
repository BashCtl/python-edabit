import re


def reverse_words(words):
    words = re.sub(" +", " ", words)
    words = words.split(" ")
    return " ".join(words[::-1]).strip()


print(reverse_words("the sky is blue"))
print(reverse_words("  hello world!  "))
print(reverse_words("a good   example"))