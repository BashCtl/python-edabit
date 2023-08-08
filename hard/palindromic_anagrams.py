def is_palindrome_possible(txt):
    count_map = dict()
    for i in range(len(txt)):
        if txt[i] in count_map:
            count_map[txt[i]] += 1
        else:
            count_map[txt[i]] = 1
    odd = 0
    for v in count_map.values():
        if v & 1 == 1:
            odd += 1
    if odd > 1 or odd == 1 and len(txt) & 1 == 0:
        return False
    return True


print(is_palindrome_possible("rearcac"))
print(is_palindrome_possible("palindrome"))
