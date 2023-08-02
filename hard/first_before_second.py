def first_before_second(s, first, second):
    return s.index(second) > s.rfind(first)


print(first_before_second("a rabbit jumps joyfully", "a", "j"))
print(first_before_second("happy birthday", "a", "y"))
