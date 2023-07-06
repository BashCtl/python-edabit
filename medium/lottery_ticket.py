def lottery(ticket, win):
    wins = sum([sum([1 if ord(i) == item[1] else 0 for i in item[0]]) for item in ticket])
    return "Winner!" if wins >= win else "Loser!"


print(lottery([["YYW", 70], ["WXK", 65], ["RPDI", 88]], 2))
print(lottery([["KG", 80], ["NTBBVZ", 79], ["CI", 73], ["AGXMEE", 74], ["IU", 68], ["VOSP" , 84]], 1))
