def showdown(p1, p2):
    index1 = p1.index("B")
    index2 = p2.index("B")
    if index1 < index2:
        return "p1"
    elif index2 < index1:
        return "p2"
    return "tie"
