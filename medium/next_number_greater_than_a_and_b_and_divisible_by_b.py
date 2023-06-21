def divisible_by_b(a, b):
    number = a + 1
    while True:
        if number % b == 0:
            return number
        number += 1


print(divisible_by_b(17, 8))
print(divisible_by_b(98, 3))
