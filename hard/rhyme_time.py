import re


def does_rhyme(txt1, txt2):
    txt1 = re.sub("[^aioue ]", "", txt1.lower())
    txt2 = re.sub("[^aioue ]", "", txt2.lower())
    t1 = txt1.split(" ")[-1]
    t2 = txt2.split(" ")[-1]
    return t2.endswith(t1)


print(does_rhyme("Sam I am!", "Green eggs and ham."))
print(does_rhyme("You are off to the races", "a splendid day."))
