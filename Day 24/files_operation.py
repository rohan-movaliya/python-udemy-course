# file = open("my_file.txt") # open the file
# message = file.read() # read the file
# print(message)
# file.close() # close the file


# READ OPERATION

# through with keyword open the file, don't need to clode the file, Is automatically close.
# here defalut mode="r" for only read the file
# with open("my_file.txt") as file:
#     message = file.read()
#     print(message)


# WRITE OPERATION

# mode= "w" that means write in the file, override the file all content
# with open("my_file.txt", mode="w") as file:
#     message = "I am in B.Tech(IT)."
#     file.write(message)

# mode= "a" that means write in the file, without override the file all content
# with open("my_file.txt", mode="a") as file:
#     message = "\nI am in B.Tech(IT)."
#     file.write(message)

# if mode="w" or "a" and open file dosen't exist then new file will generating.
# with open("my_.txt", mode="a") as file:
#     message = "I am in B.Tech(IT)."
#     file.write(message)
