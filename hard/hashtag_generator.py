def generate_hashtag(txt):
    txt = txt.title().replace(" ", "")
    if len(txt) > 139 or len(txt) == 0:
        return False
    return "#" + txt


print(generate_hashtag("    Hello     world   "))
print(generate_hashtag(""))
print(generate_hashtag("Edabit Is Great"))