def collect(s, n):
    if len(s) < n:
        return []
    return sorted([s[:n]] + collect(s[n:], n))


print(collect("intercontinentalisationalism", 6))
print(collect("strengths", 3))