"""
Get Student with Best Test Avg.
Given a dictionary with students and the grades that they made on the tests that they took,
determine which student has the best Test Average. The key will be the student's name
and the value will be a list of their grades. You will only have to return the student's name.
You do not need to return their Test Average.

Examples
get_best_student({
  "John": [100, 90, 80],
  "Bob": [100, 70, 80]
}) ➞ "John"

# John's avg = 90
# Bob's avg = 83.33

get_best_student({
  "Susan": [67, 84, 75, 63],
  "Mike": [87, 98, 64, 71],
  "Jim": [90, 58, 73, 86]
}) ➞ "Mike"

Notes
All students in a dictionary will have the same amount of test scores.
So no student will have taken more tests than another.

"""


def get_best_student(grades):
    f = lambda g: sum([v for v in grades[g]])
    return max(grades, key=f)


print(get_best_student({
  "John": [100, 90, 80],
  "Bob": [100, 70, 80]
}))

print(get_best_student(
{
  "Susan": [67, 84, 75, 63],
  "Mike": [87, 98, 64, 71],
  "Jim": [90, 58, 73, 86]
}
))

print(get_best_student({
	"Tim": [93, 84, 49, 71, 76, 83],
  "Nick": [88, 91, 74, 72, 63, 68],
  "Brad": [100, 94, 72, 64, 58, 81],
	"Annie": [79, 93, 82, 82, 63, 87]
}))

print(get_best_student({
	"Eddie": [65, 85, 72, 76],
  "Brock": [55, 97, 82, 91],
  "Jessica": [78, 62, 79, 99]
}))