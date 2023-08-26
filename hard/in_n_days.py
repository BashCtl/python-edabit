def after_n_days(days, n):
    count_day = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
    days_week = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
    return [count_day[days_week[day] + n] if (days_week[day] + n) <= 6
            else count_day[(days_week[day] + n) % 7]
            for day in days]


print(after_n_days(["Thursday", "Monday"], 4))
print(after_n_days(["Sunday", "Sunday", "Sunday"], 1))