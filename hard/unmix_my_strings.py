def unmix(txt):
    return "".join([txt[i:i + 2][::-1] for i in range(0, len(txt), 2)])


print(unmix("123456"))
print(unmix("hTsii  s aimex dpus rtni.g"))