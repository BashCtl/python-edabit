from datetime import datetime, timedelta


def week_after(d):
    date = datetime.strptime(d, "%d/%m/%Y").date() + timedelta(days=7)
    return date.strftime("%d/%m/%Y")


print(week_after("12/03/2020"))
