def char_at_pos(r, s):
    switch = 0 if s == "even" else 1
    lst = [r[i] for i in range(len(r)) if (len(r) - i) & 1 == switch]
    return lst if type(r) == list else "".join(lst)


print(char_at_pos([2, 4, 6, 8, 10], "even"))
print(char_at_pos("EDABIT", "odd"))
print(char_at_pos(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "odd"))
print(["A", "B", "T", "A", "I", "Y"])
