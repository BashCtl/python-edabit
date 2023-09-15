from datetime import datetime


def sort_dates(lst, mode):
    pattern = "%d-%m-%Y_%H:%M"
    is_reverse = False if mode=="ASC" else True
    return sorted(lst, key=lambda d: (datetime.strptime(d, pattern).date().year,
                                      datetime.strptime(d,pattern).date().month,
                                      datetime.strptime(d,pattern).date().day,
                                      datetime.strptime(d,pattern).time().hour,
                                      datetime.strptime(d,pattern).time().minute), reverse=is_reverse)


# print(sort_dates(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "ASC"))
# # print(datetime.strptime("10-02-2018_12:30", "%d-%m-%Y_%H:%M"))
dates1 = [
	'18-10-2016_12:09', '01-12-2017_20:32', '18-10-2016_12:04',
	'19-10-2017_16:20', '18-10-2017_16:19', '18-10-2016_16:19'
]
print(sort_dates(dates1, "DSC"))