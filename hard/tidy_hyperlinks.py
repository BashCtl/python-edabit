def tidy_link(url, name, hover_text=None):
    if hover_text:
        return '[{}]({} "{}")'.format(name, url, hover_text)
    return '[{}]({})'.format(name, url)


print(tidy_link("https://edabit.com/challenges", "this", "Go to the challenges!"))
