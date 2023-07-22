from datetime import date


def has_friday_13(month, year):
    d = date(year, month, 13)
    return d.weekday() == 4


print(has_friday_13(3, 2020))
