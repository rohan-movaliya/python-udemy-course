student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}
for key in student_scores:
    mark = student_scores[key]
    if mark >= 91 and mark <= 100:
        student_grades[key] = "Outstanding"
    elif mark >= 81 and mark <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif mark >= 71 and mark <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"


print(student_grades)
