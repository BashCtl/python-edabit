def number_pairs(txt):
    numbers = txt.split(" ")[1:]
    return sum([numbers.count(n) // 2 if numbers.count(n) >= 2 else 0 for n in set(numbers)])


print(number_pairs("9 10 20 20 10 10 30 50 10 20"))
print(number_pairs("4 2 3 4 1"))