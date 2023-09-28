def validate_swaps(lst, txt):
    result = []
    count = 0
    for word in lst:
        if len(word) == len(txt):
            for i in range(len(txt)):
                if word[i] != txt[i]:
                    count += 1
                if word.count(word[i]) != txt.count(word[i]):
                    count += 1
            result.append(count <= 2)
            count = 0
        else:
            result.append(False)
    return result


print(validate_swaps(["BACDE", "EBCDA", "BCDEA", "ACBED"], "ABCDE"))
print(validate_swaps(["32145", "12354", "15342", "12543"], "12345"))
print(validate_swaps(['9786', '9788', '97865', '7689'], '9768'))
