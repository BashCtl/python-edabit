def wash_hands(N, nM):
    total_seconds = 21 * 30 * N * nM
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return "{} minutes and {} seconds".format(minutes, seconds)


print(wash_hands(7, 9))
