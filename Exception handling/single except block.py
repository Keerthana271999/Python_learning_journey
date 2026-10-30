# If handling code is same for multiple exceptions - go for single except block
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    print(f"{numerator} / {denominator}: {numerator/denominator}")
except (ZeroDivisionError, ValueError) as msg1:
    print("Message: Try dividing by non-zero values")


try:
    age = int(input("Enter your age: "))
    numbers = [10, 20, 30]
    print(numbers[age])
except (ValueError, IndexError) as msg1:
    print("Message: Enter a valid integer and an index within the list range")
finally:
    print("Program execution completed")


try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"Result: {num1 + num2}")
except (ValueError, TypeError) as msg1:
    print("Message: Invalid data type or input")
