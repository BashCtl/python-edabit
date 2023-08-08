def consecutive_sum(n):
    return ((n&(n-1)) and n) >0


print(consecutive_sum(5))
print(consecutive_sum(64))
