# Default except block must be at last since except block order matters if it at first even thoght there is a matching except block it wont be executed and also get synteax error
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
except:
    print("Message: provide int values")


try:
    result = 10 / 0
except TypeError:
    print("Caught a TypeError!")
except KeyError:
    print("Caught a KeyError!")
except:
    print("Default except block executed: An unexpected error occurred!")


data = {"name": "Alice"}

try:
    result = data["age"] + 5
except TypeError:
    print("Caught a TypeError: Cannot add string and integer.")
except:
    print("Default except block executed: An unexpected error occurred!")
