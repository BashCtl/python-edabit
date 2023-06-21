def get_student_names(students):
    return sorted([value for value in students.values()])


print(get_student_names({
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
}))