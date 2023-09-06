def valid_word_nest(word, nest):
    if nest.count(word)>1:
        return False
    while len(nest) > len(word):
        nest_temp = nest[:]
        nest = nest.replace(word, "")
        if len(nest) == len(nest_temp):
            break
    return word == nest


print(valid_word_nest("deep", "deep"))
print(valid_word_nest("novel", "nonnonovnovnovelelelvelovelvel"))
print(valid_word_nest("painter", "ppaintppapaipainterinternteraintererainter"))
print(valid_word_nest("broadcast", "broadcbroadcastbroadcastast"))