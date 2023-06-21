import re


def format_date(date):
    return re.sub(r"(\d+)/(\d+)/(\d+)", r"\3\2\1", date)


print(format_date("11/12/2019"))
