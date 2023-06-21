def index_of_caps(word):
    return [i for i in range(len(word)) if word[i].isupper()]


print(index_of_caps("eDaBiT"))
