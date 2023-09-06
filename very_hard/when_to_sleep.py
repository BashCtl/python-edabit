from datetime import datetime


def bed_time(*times):
    ftime = "%H:%M"
    time_deltas = [datetime.strptime(t[0], ftime) - datetime.strptime(t[1], ftime) for t in times]
    return ["{:02}:{:02}".format(int(d.seconds // 3600), int((d.seconds % 3600) // 60)) for d in time_deltas]


print(bed_time(["07:50", "07:50"]))
print(bed_time(["06:15", "10:00"], ["08:00", "10:00"], ["09:30", "10:00"]))
