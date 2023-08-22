import re


def is_parsel_tongue(sentence):
    return all([re.match(r"\b(\[a-zA-Z]*|)([sS]{2,}|[^sS])[a-zA-Z]*\b", word)
                for word in sentence.strip().split(" ")])


print(is_parsel_tongue("Sshe ssselects to eat that apple. "))
print(is_parsel_tongue("She ssselects to eat that apple. "))
print(is_parsel_tongue("Beatrice samples lemonade"))
print(is_parsel_tongue("You ssseldom sssspeak sso boldly, ssso messmerizingly."))