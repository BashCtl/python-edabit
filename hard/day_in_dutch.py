"""
The Day in Dutch

Write a method that when passed a date as "dd mm yyyy"
and returns the date's weekday name in the Dutch culture.

Examples
weekday_dutch("21 9 1970") ➞ "maandag"

weekday_dutch("2 9 1945") ➞ "zondag"

weekday_dutch("9 11 2001") ➞ "dinsdag"

"""
import datetime
import calendar
import locale


def weekday_dutch(date):
    days = {0:'maandag',
           1:'dinsdag',
           2:'woensdag',
           3:'donderdag',
           4:'vrijdag',
           5:'zaterdag',
           6:'zondag',}
    day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return days[day]


# def weekday_dutch(date):
#     locale.setlocale(locale.LC_ALL, "nl_NL")
#     day = datetime.datetime.strptime(date, "%d %m %Y").weekday()
#     return calendar.day_name[day]


print(weekday_dutch("21 9 1970"))
print(weekday_dutch("2 9 1945"))
