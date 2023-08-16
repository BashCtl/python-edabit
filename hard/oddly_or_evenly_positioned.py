def char_at_pos(r, s):
    if s == "even":
        result = [c for i, c in enumerate(r) if (i + 1) & 1 == 0]
    else:
        result = [c for i, c in enumerate(r) if (i + 1) & 1 != 0]
    return result if type(r) == list else "".join(result)


print(char_at_pos([2, 4, 6, 8, 10], "even"))
print(char_at_pos("EDABIT", "odd"))