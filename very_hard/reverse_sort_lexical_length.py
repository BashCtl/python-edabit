def reverse_sort(txt):
    words = txt.split(" ")
    func = lambda a: (len(a),a.casefold())
    return " ".join(sorted(words, key=func, reverse=True))


print(reverse_sort("You've rocked the pragmatic world in the making!"))
print(reverse_sort("Tesh makes my world worth enjoying and living for."))
print(reverse_sort("Shaken by the bloody truth and crazy lies."))
