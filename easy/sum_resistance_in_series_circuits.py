def series_resistance(lst):
    s = sum(lst)
    om = "ohms" if s > 1 else "ohm"
    return "{} {}".format(s, om)


print(series_resistance([1, 5, 6, 3]))
print(series_resistance([0.5, 0.5]))
