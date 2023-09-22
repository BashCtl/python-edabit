def word_to_decimal(word):
    word = word.lower()
    nums = [ord(l) - ord("a") + 1 for l in word]
    max_num = max(nums)
    base = max_num + 10
    representative = list(map(lambda a: a + 9, nums))
    length = len(representative)
    return sum([n*base**(length-i-1)for i,n in enumerate(representative)])


print(word_to_decimal("Edabit"))
print(word_to_decimal("Python"))
