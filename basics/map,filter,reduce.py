from functools import reduce

numbers = [int(num) for num in input("Enter few numbers: ").split()]
even = list(filter(lambda num: num % 2 == 0, numbers))
print(f"Even numbers of {numbers}: {even}")

print()

# Write a Python program using the filter() function and a lambda expression to extract all the numbers greater than 50 from a given list.   Example list: [10, 55, 32, 75, 90, 41, 68]
numbers = [10, 55, 32, 75, 90, 41, 68]
greater_50 = list(filter(lambda num: num > 50, numbers))
print(f"Numbers >50 among {numbers}: {greater_50}")

print()

double = list(map(lambda num: num*2, even))
print(f"Double of {even}: {double}")

print()

total = reduce(lambda num1, num2: num1+num2, double)
print(f"sum of {double}: {total}")

# To demonstrate your understanding of map() and reduce(), write a one-line Python expression that calculates the sum of cubes of all numbers in a list.   Example list 👉 [2, 3, 4]
numbers = [2, 3, 4]
cube = list(map(lambda num: num**3, numbers))
print(f"cubes of {numbers}: {cube}")

print()

total = reduce(lambda num1, num2: num1+num2, cube)
print(f"sum of {cube}: {total}")
