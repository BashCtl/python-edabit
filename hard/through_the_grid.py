from math import factorial


def grid_pos(lst):
    return (factorial(sum(lst))//factorial(max(lst)))//factorial(min(lst))


print(grid_pos([1,1]))
print(grid_pos([6, 4]))
print(grid_pos([5, 5]))