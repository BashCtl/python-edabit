def add_str_nums(num1, num2):
    try:
        num1 = 0 if len(num1) == 0 else int(num1)
        num2 = 0 if len(num2) == 0 else int(num2)
        return str(num1 + num2)
    except ValueError:
        return "-1"


print(add_str_nums("4", "5"))
print(add_str_nums("abcdefg", "3"))
print(add_str_nums("1", ""))