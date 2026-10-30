print("Number of digits calculator")
number = int(input("Enter a number: "))
digits = 0
for digit in str(number):
    digits += 1
print(f"{number} as {digits} in it")
