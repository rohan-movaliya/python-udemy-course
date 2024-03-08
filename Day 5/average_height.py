student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
student_count = 0
for student_height in student_heights:
    total_height += student_height
    student_count += 1

print(round(total_height / student_count))
