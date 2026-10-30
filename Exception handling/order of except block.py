# actually, order of except block matters since Arithmetic error is parent class of Zero division error it can handle its child classes also

# Hence, here we get Arithmetic error
'''try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    print(f"{numerator} / {denominator}: {numerator/denominator}")
except ArithmeticError as msg2:
    print(f"Exception name: ArithmeticError")
    print("Message: Numerator and Denominator must be numbers")
except ZeroDivisionError as msg1:
    print(f"Exception name: ZeroDivisionError")
    print("Message: Try dividing by non-zero values")'''

# Hence, here we get zero division error
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    print(f"{numerator} / {denominator}: {numerator/denominator}")
except ZeroDivisionError as msg1:
    print(f"Exception name: ZeroDivisionError")
    print("Message: Try dividing by non-zero values")
except ArithmeticError as msg2:
    print(f"Exception name: ArithmeticError")
    print("Message: Numerator and Denominator must be numbers")
