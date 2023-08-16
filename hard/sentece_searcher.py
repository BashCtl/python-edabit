import re


def sentence_searcher(txt, word):
    pattern = r"(([ \w]+| ){}([ \w]+\.|.))".format(word)
    return re.search(pattern, txt, re.IGNORECASE).group(1).strip() \
        if re.search(pattern, txt, re.IGNORECASE) else ""


txt = "I have a cat. I have a mat. Things are going swell."

print(sentence_searcher(txt, "have"))
print(sentence_searcher(txt, "MAT"))
print(sentence_searcher(txt, "things"))
