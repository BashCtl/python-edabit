def make_rug(m, n, s="#"):
    return [s*n for _ in range(m)]


print(make_rug(3,5,"#"))