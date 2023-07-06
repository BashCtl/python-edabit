def countdown(n, txt):
    count = ". ".join([str(i) for i in range(n, 0, -1)])
    return "{}. {}!".format(count, txt.upper())


print(countdown(10, "Blast Off"))
