def special_reverse_string(txt):
    arr = [a for sub in txt.split() for a in sub]
    space_indexes = [i for i in range(len(txt)) if txt[i] == " "]
    last_index = len(arr) - 1
    for i in range(len(arr) // 2):
        first = arr[i]
        last = arr[last_index - i]
        arr[i] = last.upper() if first.isupper() else last.lower()
        arr[last_index - i] = first.upper() if last.isupper() else first.lower()
    arr = [item for item in arr if item != " "]
    for i in space_indexes:
        arr.insert(i, " ")
    return "".join(arr)


# print(special_reverse_string("UPPER lower"))
# print(special_reverse_string("1 23 456"))
# print(special_reverse_string("addition(3, 2) = 5"))
print(special_reverse_string("Hello World!"))
# print(special_reverse_string("Where's your dog Daisy?"))  # ?ysiadg odru oys 'erehw
# print(special_reverse_string(
#     "It's known that CSS means Cascading Style Sheets"))  # Stee hsely tsgn IDA csacs Naemsscta Htnwo Nks'ti
