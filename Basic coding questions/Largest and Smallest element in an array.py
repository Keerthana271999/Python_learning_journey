# largest and smallest element in an array
numbers = [int(num) for num in input("Enter few numbers: ").split()]

largest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
for num in numbers:
    if num < smallest:
        smallest = num
print(f"Largest element in {numbers}: {largest}")
print(f"Smallest element in {numbers}: {smallest}")
