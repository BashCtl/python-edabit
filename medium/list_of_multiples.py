def list_of_multiples(num, length):
    return [x for x in range(num, num * (length + 1), num)]


print(list_of_multiples(7, 5))
print(list_of_multiples(12, 10))
print(list_of_multiples(17, 6))
