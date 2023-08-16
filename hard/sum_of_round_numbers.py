def sum_round(num):
    str_num = str(num)
    l = len(str_num)
    return " ".join([str_num[i] + "".zfill(l - i - 1) for i in range(l - 1, -1, -1) if str_num[i]!="0"])


print(sum_round(101))
