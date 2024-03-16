from prettytable import PrettyTable

# Using add_row() method
table1 = PrettyTable(["Name", "RollNo", "Collage"])
table1.align = "l"
table1.add_row(["Rohan Movaliya", 210203100126, "ASOIT"])
table1.add_row(["Kevin Mangroliya", 210203100118, "ASOIT"])
table1.add_row(["Dhruvil Nathani", 210203100132, "SOCET"])
print(table1)
print("\n\n\n")
# Using add_column() method
table2 = PrettyTable()
table2.add_column("Name", ["Rohan Movaliya", "Kevin Mangroliya", "Dhruvil Nathani"])
table2.add_column("RollNo", [2102031000126, 2102031000118, 2102031000132])
table2.add_column("ollage", ["ASOIT", "ASOIT", "SOCET"])
print(table2)
