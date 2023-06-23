def shared_letters(txt1, txt2):
    return len([i for i in set(txt1) if i in set(txt2)])


print(shared_letters("apple", "meaty"))
print(shared_letters("fan", "forsook"))
print(shared_letters("spout", "shout"))