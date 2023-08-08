from datetime import datetime


def get_day(day):
    date =datetime.strptime(day,"%m/%d/%Y")
    return date.strftime("%A")


print(get_day("12/07/2016"))
