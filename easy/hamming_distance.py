def hamming_distance(txt1, txt2):
    result = 0
    for i in range(len(txt1)):
        if txt1[i] != txt2[i]:
            result += 1
    return result


print(hamming_distance("abcde", "bcdef"))
print(hamming_distance("abcde", "abcde"))
print(hamming_distance("strong", "strung"))
