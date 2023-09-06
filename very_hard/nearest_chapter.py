def nearest_chapter(chapt, page):
    diff = {k: abs(v - page) for k, v in chapt.items()}
    if list(diff.values()).count(min(diff.values())) > 1:
        equal_val = {k: v for k, v in diff.items() if min(diff.values()) == v}
        filtered = {k:v for k,v in chapt.items() if k in equal_val}
        return max(filtered, key=filtered.get)
    return min(diff, key=diff.get)


print(nearest_chapter({
    "Chapter 1": 1,
    "Chapter 2": 15,
    "Chapter 3": 37
}, 10))

print(nearest_chapter({
    "Chapter 1a": 1,
    "Chapter 1b": 5
}, 3))

print(nearest_chapter({
  "New Beginnings" : 1,
  "Strange Developments" : 62,
  "The End?" : 194,
  "The True Ending" : 460
}, 200))