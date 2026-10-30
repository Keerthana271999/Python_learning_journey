import os


def calculation():
    new_calculation = True
    num1 = int(input("Enter 1st number: "))
    while new_calculation:
        operator = input("choose an operator (+ / - / * / /): ")
        num2 = int(input("Enter next number: "))
        if operator == "+":
            res = num1+num2
            print(f"{num1} {operator} {num2} = {num1+num2}")
        elif operator == "-":
            res = num1-num2
            print(f"{num1} {operator} {num2} = {num1-num2}")
        elif operator == "*":
            res = num1*num2
            print(f"{num1} {operator} {num2} = {num1*num2}")
        elif operator == "/":
            res = num1/num2
            print(f"{num1} {operator} {num2} = {num1/num2}")
        else:
            print("Invalid operator")
            exit()
        repeat = input(
            f"enter y to continue with {res}, n to start new calculation,x to exit: ").lower()
        if repeat == "y":
            new_calculation = True
            num1 = res
        elif repeat == "x":
            new_calculation = False
            break
        else:
            os.system("cls")
            calculation()


calculation()
