def age_difference(f_age, s_age):
    difference = f_age - s_age
    difference *= 2
    return abs(f_age - difference)


print(age_difference(36, 7))
print(age_difference(55, 30))
