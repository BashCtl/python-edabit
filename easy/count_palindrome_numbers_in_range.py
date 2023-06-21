def count_palindromes(num1, num2):
    result = [x for x in range(num1, num2 + 1) if str(x) == str(x)[::-1]]
    return len(result)


print(count_palindromes(1, 10))
