"""
Get Students with Names and Top Notes II


Get Students with Names and Top Notes II
Create a function that takes a list of dictionaries like [{ "name": "John", "notes": [3, 5, 4]}, { "name": "Mich", "notes": [1, 3, 5]}] and returns a list of dictionaries like [{ "name": "John", "top_note": 5 }, {"name": "Mich", "top_note": 5}].

If a student has no notes (an empty list), return top_note: 0.

Examples
get_name_and_top_note([{ "name": "John", "notes": [2, 4, 5]}, { "name": "Mich", "notes": [1, 3, 5]}])  ➞ [{ "name": "John", "top_note": 5 }, {"name": "Mich", "top_note": 5}]

get_name_and_top_note([{ "name": "Paul", "notes": []}, {"name": "Victoria", "notes": [3, 4, 2, 1]}])  ➞ [{ "name": "Paul", "top_note": 0 }, {"name": "Victoria", "top_note": 4}]


"""

from unittest import TestCase


def get_name_and_top_note(students):
    return [{"name": student["name"],
             "top_note": max(student["notes"], default=0)}
            for student in students]


TestCase().assertEqual(
    get_name_and_top_note([{'name': "John", 'notes': [2, 4, 5]}, {'name': "Mich", 'notes': [1, 3, 5]}]),
    [{'name': "John", 'top_note': 5}, {'name': 'Mich', 'top_note': 5}])
TestCase().assertEqual(
    get_name_and_top_note([{'name': "Paul", 'notes': []}, {'name': 'Victoria', 'notes': [3, 4, 2, 1]}]),
    [{'name': "Paul", 'top_note': 0}, {'name': 'Victoria', 'top_note': 4}])
TestCase().assertEqual(get_name_and_top_note([{'name': "Victor", 'notes': [1, 3, 2]}]),
                       [{'name': "Victor", 'top_note': 3}])
TestCase().assertEqual(get_name_and_top_note([{'name': "Brandy", 'notes': [2, 4, 1]}]),
                       [{'name': "Brandy", 'top_note': 4}])
TestCase().assertEqual(
    get_name_and_top_note([{'name': "Vicky", 'notes': [3, 2]}, {'name': "Sanders", 'notes': [1, 1, 1]}]),
    [{'name': "Vicky", 'top_note': 3}, {'name': 'Sanders', 'top_note': 1}])
TestCase().assertEqual(get_name_and_top_note([{'name': "Marcus", 'notes': [1, 0, 1]}]),
                       [{'name': "Marcus", 'top_note': 1}])
TestCase().assertEqual(get_name_and_top_note([{'name': "Solo", 'notes': []}]), [{'name': "Solo", 'top_note': 0}])
