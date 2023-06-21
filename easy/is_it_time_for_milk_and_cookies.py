import datetime


def time_for_milk_and_cookies(date):
    return date.day == 24 and date.month == 12


print(time_for_milk_and_cookies(datetime.date(2013, 12, 24)))
print(time_for_milk_and_cookies(datetime.date(2013, 1, 24)))
