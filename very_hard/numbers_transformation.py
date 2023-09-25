"""
Numbers Transformation

You are given two positive integers n and m.
You have to perform some basic mathematical operations on n to obtain m.
These are your options:
(n-1)/2   - if (n-1) is divisible by 2
n/2       - if n is divisible by 2
n*2

Create a function that returns the minimum number of steps required to transform n into m.

Examples
number_transform(2, 8) ➞ 2
// 2 * 2 = 4
// 4 * 2 = 8

number_transform(9, 2) ➞ 2
// (9-1) / 2 = 4
// 4 / 2 = 2

number_transform(1024, 1024) ➞ 0

m will always be a power of 2.
"""

def number_transform(n, m):
    steps = 0
    while n != m:
        if n != 1 and (n - 1) % 2 == 0:
            n = (n - 1) / 2
            steps += 1
        elif n > m:
            n /= 2
            steps += 1
        else:
            n *= 2
            steps += 1
    return steps


print(number_transform(2, 8))
print(number_transform(9, 2))
print(number_transform(1024, 1024))
print(number_transform(2, 4))
print(number_transform(3, 8))
print(number_transform(4,16))
print(number_transform(4096, 2))
