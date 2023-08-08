def last_name_lensort(names):
    sort_func = lambda name: (len(name.split(" ")[1]), name.split(" ")[1])
    names = sorted(names, key=sort_func)
    return names


names_list = [
    "Jennifer Figueroa",
    "Heather Mcgee",
    "Amanda Schwartz",
    "Nicole Yoder",
    "Melissa Hoffman"
]

print(last_name_lensort(names_list))

names2 = ["Hitagi Senjougahara", "Edward Elric", "Light Yagami", "Rintaro Okabe", "Kurisu Makise"]
print(last_name_lensort(names2))

# ["Edward Elric","Rintaro Okabe","Kurisu Makise","Light Yagami","Hitagi Senjougahara"]
