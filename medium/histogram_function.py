def histogram(lst, char):
    return "\n".join([char * i for i in lst])


print(histogram([1, 3, 4], "#"))