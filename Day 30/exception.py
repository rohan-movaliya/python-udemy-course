# Something that might cause an exception
try:
    file = open("rohan.txt")  # FileNotFoundError
    rohan_dict = {"enrollment_no": 2102031000126}
    print(rohan_dict["name"])

# Do this if there was an exception
except FileNotFoundError as error_message:
    file = open("rohan.txt", "w")
    file.write("I Love Python.")

except KeyError as error_message:
    rohan_dict["name"] = "Rohan Movaliya"

# Do this if there were no exception
else:
    content = file.read()
    print(content)
    print(rohan_dict["name"])

# Do this no matter what happans
finally:
    file.close()
    print("File was closed")
    print("Add 'name' key in dictionary")
