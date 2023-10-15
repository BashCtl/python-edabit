def can_build(txt1, txt2):
    txt1 = txt1.replace(" ","")
    txt2 = txt2.replace(" ","")
    for l in txt2:
        if l in txt1:
            txt1 = txt1.replace(l, "", 1)
        if len(txt1) ==0:
            return True
    return False


print(can_build("got 2 go", "gogogo 2 today"))
print(can_build("sit on top", "its a moo point"))
print(can_build("long high add or", "highway road go long"))
print(can_build("fill tuck mid", "truck falls dim"))

