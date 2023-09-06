import re


def dakiti(sentence):
    words = sentence.split()
    words = sorted(words, key=lambda w: int(re.findall("\d",w)[0]))
    return re.sub("\d",""," ".join(words))

print(dakiti("worl2d hell1o "))
print(dakiti("en5tere y2a bab1y y3o 4me s6e not7a cuand8o 9me-ves"))