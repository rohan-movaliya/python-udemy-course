with open("file_1.txt") as file_1:
    num_list_1 = file_1.readlines()

with open("file_2.txt") as file_1:
    num_list_2 = file_1.readlines()

# result is a list which contains common between num_list_1 and num_list_2
result = [int(num) for num in num_list_1 if num in num_list_2]

print(f"Common in Both list : {result}")
