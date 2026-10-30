# 1. Arithmetic Operators

# 2. Assignment Operators

num = int(input("Enter a number: "))
num += 1
print(f"After adding 1: {num}")
num -= 1
print(f"After subtracting 1: {num}")
num *= 2
print(f"After multiplyng by 2: {num}")
num /= 2
print(f"After dividing by 2: {num}")
num //= 2
print(f"After dividing by 2 - integer part: {num}")
num %= 2
print(f"After dividing by 2 - remainder: {num}")


# Comparison (Relational) Operators
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
print(f"{num1} > {num2} = {num1 > num2}")
print(f"{num1} >= {num2} = {num1 >= num2}")
print(f"{num1} equal to {num2} = {num1 == num2}")
print(f"{num1} not equal to {num2} = {num1 != num2}")
print(f"{num1} < {num2} = {num1 < num2}")
print(f"{num1} < {num2} = {num1 <= num2}")


# Logical Operators
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
print(f"{num1} > {num2} = {num1 > num2} and {num1} >= {num2} = {num1 >= num2}")
print(f"{num1} > {num2} = {num1 > num2} or {num1} >= {num2} = {num1 >= num2}")
print(f"reverse of: {num1} > {num2} = {not (num1 > num2)}")


# Bitwise Operators
num = int(input("Enter a number: "))
shift = int(input("Enter shift value: "))
print(f"{num} & {shift} = {num & shift}")
print(f"{num} | {shift} = {num | shift}")
print(f"Negation: -(n+1) = {~num}")
print(f"Left shift: x*(2^n) = {num << shift}")
print(f"Right shift: x/(2^n) = {num >> shift}")

# Membership Operators
numbers = [int(num) for num in input("Enter few numbers: ").split()]
print("32" in numbers)

# Identity Operators
num1 = 5
num2 = num1
print(num1 is num2)
print(num1 == num2)
print(id(num1), id(num2))

a = 3
b = 4
a *= 2
b -= a
print(a > b and b > 0)
