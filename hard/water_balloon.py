def pop(state):
    mid = len(state) // 2
    for i in range(1, mid):
        state[mid - i] = state[mid] - i
        state[mid + i] = state[mid] - i
    return state


print(pop([0, 0, 0, 0, 4, 0, 0, 0, 0]))
print(pop([0]))
print(pop([0, 0, 0, 3, 0, 0, 0]))
print(pop([0, 0, 2, 0, 0]))