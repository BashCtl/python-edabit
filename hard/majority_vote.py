def majority_vote(lst):
    unique = set(lst)
    m = 0
    result = ""
    for x in unique:
        total = lst.count(x)
        if total == m:
            return None
        elif total > m:
            m = total
            result = x
    return result if len(result)>0 else None


print(majority_vote(["A", "A", "A", "B", "C", "A"]))

print(majority_vote(["A", "B"]))
print(majority_vote([]))
