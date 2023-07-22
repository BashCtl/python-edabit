def fact_of_fact(n):
    result = 1
    while n > 1:
        result *= factorial(n)
        n -= 1
    return result


def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)


print(fact_of_fact(4))
print(fact_of_fact(5))
