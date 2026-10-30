print("money hiding")
lockers = [
    ["🔒", "🔒", "🔒"],
    ["🔒", "🔒", "🔒"],
    ["🔒", "🔒", "🔒"]
]

print(f"Lockers available:\n{lockers}")
position = int(input("Enter the position where you want to hid your money: "))
row = str(position)[0]
column = str(position)[1]

row_selected = int(row)
column_selected = int(column)

lockers[row_selected-1][column_selected-1] = "💵"
for row in lockers:
    print(" ".join(map(str, row)))

print(f"Locker selected: {lockers}")
