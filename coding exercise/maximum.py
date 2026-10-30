print("maximum number checker")
numbers = [int(number) for number in input("Enter few numbers: ").split()]
maximum = 0
for num in numbers:
    if num > maximum:
        maximum = num
print(f"Maximum of {numbers}: {maximum}")
