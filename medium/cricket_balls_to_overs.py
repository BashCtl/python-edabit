def total_overs(balls):
    overs = balls // 6
    bowled = balls - overs*6
    return overs if bowled == 0 else float("{}.{}".format(overs, bowled))


print(total_overs(2400))
print(total_overs(164))
print(total_overs(945))
print(total_overs(5))