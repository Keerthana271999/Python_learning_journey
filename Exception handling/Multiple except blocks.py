try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    print(f"{numerator} / {denominator}: {numerator/denominator}")
except ZeroDivisionError as msg1:
    print(f"Exception name: {msg1.__class__.__name__}")
    print(f"Error description: {msg1}")
    print("Message: Try dividing by non-zero values")
except ValueError as msg2:
    print(f"Exception name: {msg2.__class__.__name__}")
    print(f"Error description: {msg2}")
    print("Message: Numerator and Denominator must be numbers")
