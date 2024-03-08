row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
position_x = int(position[0]) - 1
position_y = int(position[1]) - 1

map[position_x][position_y] = "X"


print(f"{row1}\n{row2}\n{row3}")
