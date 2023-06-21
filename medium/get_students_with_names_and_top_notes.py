def top_note(student):
    notes = student.popitem()[1]
    student.update({"top_note": max(notes)})
    return student


print(top_note({"name": "John", "notes": [3, 5, 4]}))
