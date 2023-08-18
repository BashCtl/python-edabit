import datetime


def how_unlucky(y):
    count = 0
    for m in range(1, 13):
        year = datetime.datetime(y, m, 13)
        if year.weekday() == 4:
            count += 1
    return count

print(how_unlucky(2020))
