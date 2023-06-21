def sum_odd_and_even(lst):
    even = sum([n for n in lst if n % 2 == 0])
    odd = sum([n for n in lst if n % 2 != 0])
    return [even, odd]


print(sum_odd_and_even([1, 2, 3, 4, 5, 6]))
print(sum_odd_and_even([-1, -2, -3, -4, -5, -6]))
print(sum_odd_and_even([0, 0]))
