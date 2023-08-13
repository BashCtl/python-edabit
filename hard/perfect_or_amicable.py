def num_type(n):
    sum_div = sum_divisors(n)
    if sum_div == n:
        return "Perfect"
    elif sum_divisors(sum_div) == n:
        return "Amicable"
    return "Neither"


def sum_divisors(n):
    return sum([x for x in range(1, n) if n % x == 0])


print(num_type(6))
print(num_type(2924))
print(num_type(5010))
