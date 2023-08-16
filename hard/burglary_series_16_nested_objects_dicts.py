def determine_who_cursed_the_most(d:dict):
    me = sum([item["me"] for item in d.values()])
    spouse = sum([item["spouse"] for item in d.values()])
    return "DRAW!" if me == spouse else "ME!" if me > spouse else "SPOUSE!"


print(determine_who_cursed_the_most({
    "round1": {"me": 10, "spouse": 5},
    "round2": {"me": 5, "spouse": 10},
    "round3": {"me": 10, "spouse": 10}}))
