from collections import Counter


def get_notes_distribution(students):
    counter = Counter()
    for student in students:
        counter.update(list(filter(lambda n: 0 < n < 6, student['notes'])))
    return dict(counter)


print(get_notes_distribution([
    {
        "name": "Steve",
        "notes": [5, 5, 3, -1, 6]
    },
    {
        "name": "John",
        "notes": [3, 2, 5, 0, -3]
    }
]))
