import random

names = ["Rohan", "Dhruvil", "Ayush", "Meet", "Darshan", "Shubham"]

# new_dict = {new_key:new_value for item in list}
student_score = {student_name: random.randint(1, 100) for student_name in names}
print(student_score)

# new_dict = {new_key:new_value for(key,value) in dict.items() if test}
passed_students = {
    student: score for (student, score) in student_score.items() if score >= 60
}
print(passed_students)
