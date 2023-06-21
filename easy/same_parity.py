def parity_analysis(num):
    numbers = [int(x) for x in str(num)]
    if len(numbers) == 1:
        return True
    return (num % 2 != 0 and sum(numbers) % 2 != 0) \
        or (num % 2 == 0 and sum(numbers) % 2 == 0)


print(parity_analysis(243))
print(parity_analysis(12))
