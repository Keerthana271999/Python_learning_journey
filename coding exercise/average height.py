print("Average height calculator")
heights = [float(height)
           for height in input("Enter few heights (feet): ").split()]
print(f"List of heights: {heights}")
total_height = number_of_heights = 0
for height in heights:
    total_height += height
    number_of_heights += 1
    average = total_height/number_of_heights
print(f"Average height: {average}")
