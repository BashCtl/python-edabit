import re


def anna_likes(boy):
    temp = re.sub("[^aeiouAEIOU]", "", boy)
    return len(temp) * 2 == len(boy)


print(anna_likes("David"))
print(anna_likes("Samuel"))
print(anna_likes("Gary"))
print(anna_likes("Joshua"))
print(anna_likes("Edward"))
print(anna_likes("Anna"))
