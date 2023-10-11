def inverter(txt, type):
    lst = txt.split(" ")
    if type == "P":
        return " ".join([lst[i].capitalize() for i in range(len(lst) - 1, -1, -1)]).capitalize()
    elif type == "W":
        return " ".join([w[::-1] for w in lst]).capitalize()


print(inverter("This is Valhalla", "P"))
print(inverter("One fine day to start", "W"))
