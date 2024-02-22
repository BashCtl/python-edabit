"""
Recursion: Multiplication by Addition

Create a function that returns the product of two integers.
This process of multiplication can be achieved via repetitive addition, thus, the process can be done recursively.

Examples
multiply(10, 2) ➞ 20

multiply(-51, -4) ➞ 204

multiply(3, 9) ➞ 27

multiply(-21, 5) ➞ -105

multiply(1024, 7) ➞ 7168

multiply(273, -6) ➞ -1638

Notes
You're expected to solve this challenge using a recursive approach.


"""

def multiply(x, y, flag=None):
    if y == 0:
        return 0
    if flag is None:
        if x < 0 and y < 0:
            flag = False
            x = abs(x)
        elif y < 0:
            flag = True
            x = -x

    y = y - 1 if y > 0 else y + 1
    return x + multiply(x, y, flag)


print(multiply(10, 2))
print(multiply(-51, -4))
print(multiply(-21, 5))
print(multiply(273, -6))
