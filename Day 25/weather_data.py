# # Using file handling method
# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# # Using csv library
# import csv
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     for row in data:
#         print(row)

# Using pandas
import pandas as pd
import statistics as st

data = pd.read_csv("weather_data.csv")
# print(data)
# print(data["day"])

# covert into dict
data_dict = data.to_dict()
# print(data_dict)

# convert into list
temp_list = data["temp"].to_list()

# print(data["temp"].mean())
# print(data["temp"].max())

# get data in column
# print(data["temp"])
# print(data.temp)

# get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9 / 5 + 32
# print(monday_temp_F)


# create datafram from scratch
data_dict = {
    "Name": ["Rohan", "Kevin", "Yash"],
    "city": ["Ahmedabad", "Surat", "Rafaliya"],
}
df = pd.DataFrame(data_dict)
# generate csv file of dataframe
df.to_csv("new_file.csv")
