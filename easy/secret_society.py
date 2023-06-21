def society_name(friends):
    friends = sorted(friends)
    return "".join([x[:1] for x in friends])


print(society_name(["Adam", "Sarah", "Malcolm"]))
