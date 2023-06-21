def chatroom_status(users):
    if not users:
        return "no one online"
    elif len(users) == 1:
        return f"{users[0]} online"
    elif len(users) == 2:
        return f"{users[0]}and {users[1]} online"
    else:
        return f"{users[0]}, {users[1]} and {len(users) - 2} more online"


print(chatroom_status([]))
print(chatroom_status(["paRIE_to"]))
print(chatroom_status(["s234f", "mailbox2"]))
print(chatroom_status(["pap_ier44", "townieBOY", "panda321", "motor_bike5", "sandwichmaker833", "violinist91"]))
