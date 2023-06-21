def are_true(a, b):
    return "both" if a and b else "first" if a else "second" if b else "neither"

	# if a == True:
	# 	if b == True:
	# 		return "both"
	# 	else:
	# 		return "first"
	# elif b = True:
	# 	return "second"
	# else:
	# 	return "neither"


print(are_true(True, True))
print(are_true(True, False))
print(are_true(False, False))
print(are_true(False, True))