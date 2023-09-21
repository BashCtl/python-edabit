from datetime import timedelta, datetime


def time_adjust(now, hrs, mins, sec):
    now = [int(t) for t in now.split(":")]
    date = datetime(2000, 12, 12, now[0], now[1], now[2]) + timedelta(hours=hrs, minutes=mins, seconds=sec)
    return date.time().strftime("%H:%M:%S")


print(time_adjust("01:00:00", 1, 30, 10))
print(time_adjust("00:00:00", 72, 120, 120))