def greet_people(names):
    return ", ".join([f'Hello {name}' for name in names]) if len(names)>0 else ""


print(greet_people(["Joe"]))
print(greet_people(["Angela", "Joe"]))
print(greet_people(["Frank", "Angela", "Joe"]))
print(greet_people([]))
#
# def greet_people(names):
# 	if len(names)>0:
# 			return ", ".join([f'Hello {name}' for name in names])
# 	else:
# 		return ""