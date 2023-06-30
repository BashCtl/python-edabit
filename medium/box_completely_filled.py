def completely_filled(lst):
    result =[" " not in line[1:-1] for line in lst[1:-1]]
    return all(result)


lst1 = [
  "#####",
  "#***#",
  "#***#",
  "#***#",
  "#####"
]

print(completely_filled(lst1))

lst2 = [
  "#####",
  "#* *#",
  "#***#",
  "#***#",
  "#####"
]
print(completely_filled(lst2))