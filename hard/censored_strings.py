def uncensor(txt, vowels):
    result = ""
    for i in range(len(txt)):
        if txt[i] == "*":
            result += vowels[0]
            vowels = vowels[1:]
        else:
            result +=txt[i]
    return result


print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))