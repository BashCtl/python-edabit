import datetime


def get_days(date1, date2):
    return (date2 - date1).days


print(get_days(datetime.date(2019, 6, 14), datetime.date(2019, 6, 20)))
