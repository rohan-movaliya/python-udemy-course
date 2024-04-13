import pandas

# DATA DICTIONARY
student_dict = {"student": ["Rohan", "Shubham", "Parth"], "score": [56, 76, 98]}

# 1] LOOPING THROUGH DICTIONARY
for (key, value) in student_dict.items():
    print(key)
    print(value)

# USING PANDAS LIBRARY
student_data = pandas.DataFrame(student_dict)
print(student_data)

# LOOP THROUGH DATA FRAME
for (key, value) in student_data.items():
    print(key)
    print(value)

# LOOP THROUGH ROW OF DATA FRAME
for (index, row) in student_data.iterrows():
    print(row)
    print(row.student)
    print(row.score)
