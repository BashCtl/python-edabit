def pluralize(lst):
    return {word if lst.count(word) == 1 else word + "s" for word in lst}


print(pluralize(["cow", "pig", "cow", "cow"]))
print(pluralize(["table", "table", "table"]))