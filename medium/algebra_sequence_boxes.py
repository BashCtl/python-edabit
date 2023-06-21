def box_seq(step):
    return sum([3 if k % 2 != 0 else -1 for k in range(1, step + 1)])


print(box_seq(0))
print(box_seq(1))
print(box_seq(2))