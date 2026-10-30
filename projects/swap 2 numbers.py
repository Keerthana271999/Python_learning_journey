num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
print(f"Before swapping: num1 - {num1}, num2 - {num2}")
num1, num2 = num2, num1
print(f"After swapping: num1 - {num1}, num2 - {num2}")

print()

# using arithmetic operators
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
print(f"Before swapping: num1 - {num1}, num2 - {num2}")
num1 = num1+num2
num2 = num1-num2
num1 = num1-num2
print(f"After swapping: num1 - {num1}, num2 - {num2}")

print()

# using 3rd variable
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
print(f"Before swapping: num1 - {num1}, num2 - {num2}")
temp = num1
num1 = num2
num2 = temp
print(f"Before swapping: num1 - {num1}, num2 - {num2}")
