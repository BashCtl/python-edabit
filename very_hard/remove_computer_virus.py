import re


def remove_virus(files):
    lst = files.split(":")
    pattern = r" (?!\bantivirus\.exe|\bnotvirus\.exe)(\b\w*virus\.exe|\b\w*malware\.exe),?"
    lst[1] = re.sub(pattern, "", lst[1]).rstrip(", ")
    lst[1] = lst[1] if lst[1] else " Empty"
    return ":".join(lst)


print(remove_virus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe "))
print(remove_virus("PC Files: spotifysetup.exe, virus.exe, dog.jpg"))
print(remove_virus("PC Files: notvirus.exe, funnycat.gif"))
print(remove_virus("PC Files: virus.exe, bestmalware.exe, memzvirus.exe"))
