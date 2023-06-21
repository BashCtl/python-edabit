lst1 = ["John", "Mary", "Jane"]
# lst2 = [yourlisthere]
# lst3 = [yourlisthere]

template = "My {elem} are: {}, {} and {}."

print(template.format(*lst1, elem="friends"))