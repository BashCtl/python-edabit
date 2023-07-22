def censor_string(txt, lst, char):
    return " ".join([word if word not in lst else char * len(word) for word in txt.split(" ")])


print(censor_string("Today is a Wednesday!", ["Today", "a"], "-"))