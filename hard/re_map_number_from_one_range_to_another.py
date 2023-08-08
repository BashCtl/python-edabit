def remap(value, low1, high1, low2, high2):
    try:
        return low2 + ((high2 - low2) / (high1 - low1)) * (value - low1)
    except Exception:
        return 0


print(remap(7, 2, 12, 0, 100))
