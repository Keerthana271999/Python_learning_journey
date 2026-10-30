num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
choice = input("Enter operator: ")
match choice:
    case "+":
        print(f"Sum of {num1} and {num2}: {num1+num2}")
    case "+":
        print(f"Sum of {num1} and {num2}: {num1+num2}")
    case "-":
        print(f"Difference of {num1} and {num2}: {num1-num2}")
    case "*":
        print(f"Product of {num1} and {num2}: {num1*num2}")
    case "/":
        print(f"Quotient of {num1} / {num2}: {num1//num2}")
    case _:
        print("Invalid choice")
