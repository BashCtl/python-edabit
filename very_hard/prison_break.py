def freed_prisoners(prison):
    if prison[0] == 1:
        count = 0
        for i in range(0, len(prison)):
            if prison[i] == 1:
                count += 1
                prison = [1 if i == 0 else 0 for i in prison]
        return count
    else:
        return 0


print(freed_prisoners([1, 1, 0, 0, 0, 1, 0]))
print(freed_prisoners([1, 1, 1]))
print(freed_prisoners([0, 0, 0]))
print(freed_prisoners([0, 1, 1, 1]))