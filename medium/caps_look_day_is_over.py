def normalize(txt):
    words = txt.split(" ")
    t = " ".join([words[i].title() if i == 0 else words[i].lower() for i in range(0, len(words))]).strip()
    return txt if not txt.isupper() else "{}!".format(t)


print(normalize("CAPS LOCK DAY IS OVER"))
print(normalize("Today is not caps lock day."))
