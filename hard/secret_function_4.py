def secret(txt):
    items = txt.split(".")
    return "<{0} class='{1}'></{0}>".format(items[0], " ".join(items[1:]))


print(secret("p.one.two.three"))