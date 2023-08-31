def staircase(n):
    return "\n".join([("_" * (n - 1 - i)) + ("#" * (1 + i)) if n > 0
                      else ("_" * i) + ("#" * abs((n + i)))
                      for i in range(abs(n))])


print(staircase(3))
print(staircase(7))
print(staircase(2))
print(staircase(-8))