def mark_maths(lst):
    lst2 = [eq for eq in lst if eval(eq.split("=")[0]) == int(eq.split("=")[1])]
    length1=len(lst)
    length2=len(lst2)
    return "{}%".format(round((length2 / length1) * 100))


print(mark_maths(["2+2=4", "3+2=5", "10-3=3", "5+5=10"]))
print(mark_maths(["2+3=5", "4+4=9", "3-1=2"]))
print(mark_maths(["2+1=1", "2-1=2", "1+2=-2", "2-1=0", "1-2=0", "2+1=2", "2-1=1", "1-2=0", "2+1=1", "1+2=-1", "1+2=1", "1+2=-1", "1-2=-2", "1-1=2", "1+2=-1", "1-1=2", "2-1=0", "1-2=-2", "2+1=-2", "1-1=-1", "1-1=1", "1+2=1", "1-1=2"]))