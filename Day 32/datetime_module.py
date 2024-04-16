import datetime as dt

now = dt.datetime.now()
# 2024-04-12 11:58:28.577989
print("Year : ", now.year)
print("Month : ", now.month)
print("Day : ", now.day)
print("Hour : ", now.hour)
print("Minute : ", now.minute)
print("Second : ", now.second)
day_of_week = now.weekday()
print(day_of_week)

my_birth_date = dt.datetime(year=2004, month=5, day=6)
print(my_birth_date)
