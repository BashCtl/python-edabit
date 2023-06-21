def mood_today(mood="neutral"):
    return "Today, I am feeling {}".format(mood)


print(mood_today("happy"))
print(mood_today("sad"))
print(mood_today())
