def emphasise(txt):
    return " ".join([word[:1].upper()+word[1:].lower() for word in txt.split(' ')])


print(emphasise("hello world"))
print(emphasise("GOOD MORNING"))
print(emphasise("99 red balloons!"))